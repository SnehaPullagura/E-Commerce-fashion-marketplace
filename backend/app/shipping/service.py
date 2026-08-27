import random
from datetime import datetime, timedelta, timezone
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.core.exceptions import NotFoundException, BadRequestException
from app.core.events import event_bus, EventType
from app.orders.models import SubOrder, OrderStatus, OrderStatusHistory
from app.shipping.models import Shipment, TrackingEvent, ShipmentStatus, CourierType
from app.shipping.schemas import CreateShipmentRequest


class ShippingService:
    @staticmethod
    async def create_shipment(
        db: AsyncSession, req: CreateShipmentRequest
    ) -> Shipment:
        stmt = select(SubOrder).where(SubOrder.id == req.sub_order_id)
        res = await db.execute(stmt)
        sub_order = res.scalar_one_or_none()
        if not sub_order:
            raise NotFoundException("Sub-order not found")

        # Check existing
        ship_stmt = select(Shipment).where(Shipment.sub_order_id == req.sub_order_id)
        ship_res = await db.execute(ship_stmt)
        if ship_res.scalar_one_or_none():
            raise BadRequestException("Shipment already exists for this sub-order")

        random_wb = random.randint(100000000, 999999999)
        courier_code = req.courier.value
        waybill = f"{courier_code[:3]}-{random_wb}"
        est_delivery = datetime.now(timezone.utc) + timedelta(days=4)

        shipment = Shipment(
            sub_order_id=sub_order.id,
            courier=req.courier,
            waybill_number=waybill,
            shipping_label_url=f"https://labels.marketplace.com/print/{waybill}.pdf",
            status=ShipmentStatus.LABEL_CREATED,
            estimated_delivery=est_delivery
        )
        db.add(shipment)
        await db.flush()

        # Add initial tracking event
        initial_event = TrackingEvent(
            shipment_id=shipment.id,
            status=ShipmentStatus.LABEL_CREATED.value,
            location="Vendor Fulfillment Hub",
            description="Shipping label created. Package ready for courier pickup."
        )
        db.add(initial_event)

        # Update SubOrder
        sub_order.tracking_number = waybill
        sub_order.courier_name = req.courier.value
        sub_order.status = OrderStatus.PACKED

        history = OrderStatusHistory(
            order_id=sub_order.order_id,
            sub_order_id=sub_order.id,
            from_status=OrderStatus.CONFIRMED.value,
            to_status=OrderStatus.PACKED.value,
            note=f"Shipment created with waybill {waybill}"
        )
        db.add(history)
        await db.commit()

        await event_bus.publish(
            EventType.SHIPMENT_CREATED,
            {"sub_order_id": sub_order.id, "waybill_number": waybill, "courier": courier_code}
        )

        return await ShippingService.get_by_sub_order(db, sub_order.id)

    @staticmethod
    async def add_tracking_milestone(
        db: AsyncSession, shipment_id: str, status_val: ShipmentStatus, location: str, description: str
    ) -> TrackingEvent:
        stmt = select(Shipment).options(selectinload(Shipment.tracking_events)).where(Shipment.id == shipment_id)
        res = await db.execute(stmt)
        shipment = res.scalar_one_or_none()
        if not shipment:
            raise NotFoundException("Shipment not found")

        shipment.status = status_val
        event = TrackingEvent(
            shipment_id=shipment.id,
            status=status_val.value,
            location=location,
            description=description
        )
        db.add(event)

        if status_val == ShipmentStatus.DELIVERED:
            shipment.actual_delivery = datetime.now(timezone.utc)
            # Update sub_order to DELIVERED
            so_stmt = select(SubOrder).where(SubOrder.id == shipment.sub_order_id)
            so_res = await db.execute(so_stmt)
            sub_order = so_res.scalar_one()
            sub_order.status = OrderStatus.DELIVERED

            history = OrderStatusHistory(
                order_id=sub_order.order_id,
                sub_order_id=sub_order.id,
                to_status=OrderStatus.DELIVERED.value,
                note="Package delivered to customer."
            )
            db.add(history)

            await event_bus.publish(
                EventType.ORDER_DELIVERED,
                {"sub_order_id": sub_order.id, "order_id": sub_order.order_id}
            )

        await db.commit()
        return event

    @staticmethod
    async def get_by_sub_order(db: AsyncSession, sub_order_id: str) -> Shipment:
        stmt = (
            select(Shipment)
            .options(selectinload(Shipment.tracking_events))
            .where(Shipment.sub_order_id == sub_order_id)
        )
        res = await db.execute(stmt)
        shipment = res.scalar_one_or_none()
        if not shipment:
            raise NotFoundException("Shipment not found for this sub-order")
        return shipment
