import random
from datetime import datetime, timezone
from typing import List, Optional, Tuple, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload

from app.core.config import settings
from app.core.exceptions import NotFoundException, BadRequestException, ForbiddenException
from app.core.events import event_bus, EventType
from app.users.models import User, UserAddress
from app.users.service import UserService
from app.cart.models import Cart
from app.cart.service import CartService
from app.coupons.service import CouponService
from app.inventory.service import InventoryService
from app.orders.models import (
    Order,
    SubOrder,
    OrderItem,
    OrderStatusHistory,
    OrderStatus,
    PaymentStatus,
)
from app.orders.schemas import CheckoutRequest, UpdateOrderStatusRequest


class OrderService:
    @staticmethod
    async def create_order_from_cart(
        db: AsyncSession, user: User, req: CheckoutRequest
    ) -> Order:
        cart = await CartService.get_or_create_cart(db, user_id=user.id)
        formatted_cart = await CartService.get_formatted_cart(db, cart)

        if not formatted_cart.items:
            raise BadRequestException("Cannot checkout with an empty cart")

        # 1. Address Snapshots
        shipping_addr_stmt = select(UserAddress).where(UserAddress.id == req.shipping_address_id, UserAddress.user_id == user.id)
        res_addr = await db.execute(shipping_addr_stmt)
        shipping_addr = res_addr.scalar_one_or_none()
        if not shipping_addr:
            raise NotFoundException("Shipping address not found")

        shipping_snapshot = {
            "full_name": shipping_addr.full_name,
            "phone_number": shipping_addr.phone_number,
            "street_address": shipping_addr.street_address,
            "landmark": shipping_addr.landmark,
            "city": shipping_addr.city,
            "state": shipping_addr.state,
            "postal_code": shipping_addr.postal_code,
            "country": shipping_addr.country
        }
        billing_snapshot = shipping_snapshot

        # 2. Apply Coupon if provided
        discount_amount = 0.0
        coupon_code = req.coupon_code
        if coupon_code:
            coupon_res = await CouponService.validate_and_apply(
                db, code=coupon_code, cart_amount=formatted_cart.subtotal, user_id=user.id
            )
            if coupon_res.is_valid:
                discount_amount = coupon_res.discount_amount
            else:
                coupon_code = None

        total_amount = max(0.0, formatted_cart.subtotal - discount_amount + formatted_cart.shipping_fee)

        # 3. Create Parent Order
        year = datetime.now(timezone.utc).year
        random_suffix = random.randint(100000, 999999)
        order_number = f"FM-{year}-{random_suffix}"

        order = Order(
            user_id=user.id,
            order_number=order_number,
            total_amount=round(total_amount, 2),
            subtotal=formatted_cart.subtotal,
            shipping_fee=formatted_cart.shipping_fee,
            discount_amount=discount_amount,
            coupon_code=coupon_code,
            status=OrderStatus.PENDING,
            payment_status=PaymentStatus.PENDING,
            payment_method=req.payment_method,
            shipping_address_snapshot=shipping_snapshot,
            billing_address_snapshot=billing_snapshot,
            notes=req.customer_notes
        )
        db.add(order)
        await db.flush()

        # 4. Create Multi-Vendor Sub-Orders and Order Items
        reservation_items: List[Tuple[str, int]] = []

        for idx, vg in enumerate(formatted_cart.vendor_groups, start=1):
            sub_order_num = f"{order_number}-V{idx}"
            comm_rate = settings.DEFAULT_COMMISSION_PERCENTAGE
            comm_amt = round((vg.vendor_subtotal * comm_rate) / 100.0, 2)
            vendor_payout = round(vg.vendor_subtotal - comm_amt, 2)

            sub_order = SubOrder(
                order_id=order.id,
                vendor_id=vg.vendor_id,
                sub_order_number=sub_order_num,
                subtotal=vg.vendor_subtotal,
                shipping_fee=vg.shipping_fee,
                commission_rate=comm_rate,
                commission_amount=comm_amt,
                vendor_payout=vendor_payout,
                status=OrderStatus.PENDING
            )
            db.add(sub_order)
            await db.flush()

            for item in vg.items:
                order_item = OrderItem(
                    order_id=order.id,
                    sub_order_id=sub_order.id,
                    product_id=item.product_id,
                    variant_id=item.variant_id,
                    product_title=item.product_title,
                    product_slug=item.product_slug,
                    brand_name=item.brand_name,
                    image_url=item.image_url,
                    selected_size=item.size,
                    selected_color=item.color_name,
                    sku=f"SKU-{item.variant_id[:8]}",
                    quantity=item.quantity,
                    unit_price=item.unit_price,
                    total_price=item.item_subtotal
                )
                db.add(order_item)
                reservation_items.append((item.variant_id, item.quantity))

        # Initial status history
        history = OrderStatusHistory(
            order_id=order.id,
            to_status=OrderStatus.PENDING.value,
            note="Order created and awaiting payment confirmation.",
            changed_by=user.id
        )
        db.add(history)
        await db.commit()

        # 5. Execute 2-Phase Inventory Reservation
        await InventoryService.reserve_stock(db, order_id=order.id, items=reservation_items)

        # 6. Clear shopping cart
        await CartService.clear_cart(db, cart)

        # Publish Order Created Event
        await event_bus.publish(
            EventType.ORDER_CREATED,
            {"order_id": order.id, "order_number": order.order_number, "total_amount": order.total_amount, "user_id": user.id}
        )

        return await OrderService.get_by_id(db, order.id)

    @staticmethod
    async def get_by_id(db: AsyncSession, order_id: str, user_id: Optional[str] = None) -> Order:
        stmt = (
            select(Order)
            .options(
                selectinload(Order.items),
                selectinload(Order.sub_orders).selectinload(SubOrder.items),
                selectinload(Order.status_history)
            )
            .where(Order.id == order_id, Order.is_deleted == False)
        )
        if user_id:
            stmt = stmt.where(Order.user_id == user_id)

        res = await db.execute(stmt)
        order = res.scalar_one_or_none()
        if not order:
            raise NotFoundException("Order not found")
        return order

    @staticmethod
    async def list_user_orders(db: AsyncSession, user_id: str) -> List[Order]:
        stmt = (
            select(Order)
            .options(
                selectinload(Order.items),
                selectinload(Order.sub_orders).selectinload(SubOrder.items)
            )
            .where(Order.user_id == user_id, Order.is_deleted == False)
            .order_by(Order.created_at.desc())
        )
        res = await db.execute(stmt)
        return list(res.scalars().all())

    @staticmethod
    async def list_vendor_sub_orders(db: AsyncSession, vendor_id: str) -> List[SubOrder]:
        stmt = (
            select(SubOrder)
            .options(selectinload(SubOrder.items), selectinload(SubOrder.order))
            .where(SubOrder.vendor_id == vendor_id, SubOrder.is_deleted == False)
            .order_by(SubOrder.created_at.desc())
        )
        res = await db.execute(stmt)
        return list(res.scalars().all())

    @staticmethod
    async def update_sub_order_status(
        db: AsyncSession, sub_order_id: str, req: UpdateOrderStatusRequest, vendor_id: Optional[str] = None
    ) -> SubOrder:
        stmt = (
            select(SubOrder)
            .options(selectinload(SubOrder.order), selectinload(SubOrder.items))
            .where(SubOrder.id == sub_order_id, SubOrder.is_deleted == False)
        )
        if vendor_id:
            stmt = stmt.where(SubOrder.vendor_id == vendor_id)

        res = await db.execute(stmt)
        sub_order = res.scalar_one_or_none()
        if not sub_order:
            raise NotFoundException("Sub-order not found")

        old_status = sub_order.status
        sub_order.status = req.status
        if req.tracking_number:
            sub_order.tracking_number = req.tracking_number
        if req.courier_name:
            sub_order.courier_name = req.courier_name

        # Add history
        history = OrderStatusHistory(
            order_id=sub_order.order_id,
            sub_order_id=sub_order.id,
            from_status=old_status.value,
            to_status=req.status.value,
            note=req.note or f"Sub-order updated to {req.status.value}"
        )
        db.add(history)
        await db.commit()
        await db.refresh(sub_order)
        return sub_order
