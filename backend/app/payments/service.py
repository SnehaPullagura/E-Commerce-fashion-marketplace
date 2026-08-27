import random
import uuid
from datetime import datetime, timezone
from typing import Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload

from app.core.config import settings
from app.core.exceptions import NotFoundException, BadRequestException
from app.core.events import event_bus, EventType
from app.users.models import User
from app.orders.models import Order, SubOrder, OrderStatus, PaymentStatus, OrderStatusHistory
from app.orders.service import OrderService
from app.inventory.service import InventoryService
from app.coupons.service import CouponService
from app.payments.models import PaymentTransaction, Refund, PaymentGatewayType, PaymentTxStatus
from app.payments.schemas import InitiatePaymentRequest, PaymentInitiateResponse, VerifyPaymentWebhook, RefundRequest


class PaymentService:
    @staticmethod
    async def initiate_payment(
        db: AsyncSession, user: User, req: InitiatePaymentRequest
    ) -> PaymentInitiateResponse:
        order = await OrderService.get_by_id(db, req.order_id, user_id=user.id)
        if order.payment_status == PaymentStatus.PAID:
            raise BadRequestException("Order is already paid")

        year = datetime.now(timezone.utc).year
        random_id = random.randint(1000000, 9999999)
        txn_ref = f"TXN-{year}-{random_id}"

        txn = PaymentTransaction(
            order_id=order.id,
            user_id=user.id,
            transaction_reference=txn_ref,
            payment_gateway=req.gateway,
            amount=order.total_amount,
            currency="INR",
            status=PaymentTxStatus.INITIATED,
            payment_method=req.payment_method,
            gateway_order_id=f"order_mock_{random_id}",
            gateway_response={"status": "created"}
        )
        db.add(txn)
        await db.commit()

        await event_bus.publish(
            EventType.PAYMENT_INITIATED,
            {"transaction_reference": txn_ref, "order_id": order.id, "amount": order.total_amount}
        )

        return PaymentInitiateResponse(
            transaction_reference=txn_ref,
            order_id=order.id,
            amount=order.total_amount,
            currency="INR",
            gateway=req.gateway,
            gateway_order_id=txn.gateway_order_id,
            razorpay_key_id="rzp_test_mock_key" if req.gateway == PaymentGatewayType.RAZORPAY else None
        )

    @staticmethod
    async def process_payment_callback(
        db: AsyncSession, req: VerifyPaymentWebhook
    ) -> Dict[str, Any]:
        stmt = (
            select(PaymentTransaction)
            .where(PaymentTransaction.transaction_reference == req.transaction_reference)
        )
        res = await db.execute(stmt)
        txn = res.scalar_one_or_none()
        if not txn:
            raise NotFoundException("Payment transaction not found")

        order_stmt = select(Order).options(selectinload(Order.sub_orders)).where(Order.id == txn.order_id)
        order_res = await db.execute(order_stmt)
        order = order_res.scalar_one()

        if req.status == PaymentTxStatus.SUCCESS:
            txn.status = PaymentTxStatus.SUCCESS
            txn.gateway_payment_id = req.gateway_payment_id or f"pay_mock_{uuid.uuid4().hex[:10]}"
            txn.gateway_signature = req.gateway_signature
            txn.gateway_response = req.gateway_payload

            # 1. Update Order & Sub-Orders
            order.payment_status = PaymentStatus.PAID
            order.status = OrderStatus.CONFIRMED

            for so in order.sub_orders:
                so.status = OrderStatus.CONFIRMED

            # Add history
            history = OrderStatusHistory(
                order_id=order.id,
                to_status=OrderStatus.CONFIRMED.value,
                note="Payment confirmed successfully via " + txn.payment_method
            )
            db.add(history)
            await db.commit()

            # 2. Finalize 2-Phase Inventory Reservation
            await InventoryService.commit_reservation(db, order_id=order.id)

            # 3. Record coupon usage if applied
            if order.coupon_code:
                # Find coupon
                from app.coupons.models import Coupon
                c_stmt = select(Coupon).where(Coupon.code == order.coupon_code)
                c_res = await db.execute(c_stmt)
                coupon_obj = c_res.scalar_one_or_none()
                if coupon_obj:
                    await CouponService.record_usage(
                        db,
                        coupon_id=coupon_obj.id,
                        user_id=order.user_id,
                        order_id=order.id,
                        discount_applied=order.discount_amount
                    )

            # 4. Dispatch Payment Completed Event
            await event_bus.publish(
                EventType.PAYMENT_COMPLETED,
                {
                    "order_id": order.id,
                    "transaction_reference": txn.transaction_reference,
                    "amount": txn.amount,
                    "user_id": order.user_id
                }
            )

            return {"success": True, "status": "PAID", "order_id": order.id}

        else:
            # Payment failed
            txn.status = PaymentTxStatus.FAILED
            order.payment_status = PaymentStatus.FAILED

            history = OrderStatusHistory(
                order_id=order.id,
                to_status=OrderStatus.PENDING.value,
                note="Payment attempt failed."
            )
            db.add(history)
            await db.commit()

            # Release inventory reservation back
            await InventoryService.release_reservation(db, order_id=order.id)

            await event_bus.publish(
                EventType.PAYMENT_FAILED,
                {"order_id": order.id, "transaction_reference": txn.transaction_reference}
            )

            return {"success": False, "status": "FAILED", "order_id": order.id}

    @staticmethod
    async def process_refund(db: AsyncSession, req: RefundRequest) -> Refund:
        # Find successful transaction
        stmt = select(PaymentTransaction).where(
            PaymentTransaction.order_id == req.order_id,
            PaymentTransaction.status == PaymentTxStatus.SUCCESS
        )
        res = await db.execute(stmt)
        txn = res.scalar_one_or_none()
        if not txn:
            raise BadRequestException("No successful payment found for this order to refund")

        ref_number = f"REF-{datetime.now(timezone.utc).year}-{random.randint(100000, 999999)}"
        refund = Refund(
            order_id=req.order_id,
            sub_order_id=req.sub_order_id,
            payment_transaction_id=txn.id,
            refund_reference=ref_number,
            amount=req.amount,
            reason=req.reason,
            status="PROCESSED"
        )
        db.add(refund)

        # Update order status
        order_stmt = select(Order).where(Order.id == req.order_id)
        order_res = await db.execute(order_stmt)
        order = order_res.scalar_one()
        order.payment_status = PaymentStatus.REFUNDED
        order.status = OrderStatus.REFUNDED

        await db.commit()
        await db.refresh(refund)

        await event_bus.publish(
            EventType.REFUND_COMPLETED,
            {"refund_id": refund.id, "order_id": req.order_id, "amount": req.amount}
        )

        return refund
