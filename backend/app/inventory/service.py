from datetime import datetime, timedelta, timezone
from typing import List, Tuple, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from app.core.config import settings
from app.core.exceptions import BadRequestException, NotFoundException
from app.core.events import event_bus, EventType
from app.inventory.models import (
    InventoryItem,
    InventoryReservation,
    InventoryTransaction,
    ReservationStatus,
    InventoryTxType,
)


class InventoryService:
    @staticmethod
    async def get_or_create_item(
        db: AsyncSession,
        variant_id: str,
        sku: str,
        vendor_id: str,
        initial_stock: int = 100,
        warehouse_location: Optional[str] = "Main Warehouse"
    ) -> InventoryItem:
        stmt = select(InventoryItem).where(InventoryItem.variant_id == variant_id)
        res = await db.execute(stmt)
        item = res.scalar_one_or_none()

        if not item:
            item = InventoryItem(
                variant_id=variant_id,
                sku=sku,
                vendor_id=vendor_id,
                physical_stock=initial_stock,
                reserved_stock=0,
                warehouse_location=warehouse_location
            )
            db.add(item)
            await db.flush()

            # Record initial inbound transaction
            tx = InventoryTransaction(
                variant_id=variant_id,
                transaction_type=InventoryTxType.INBOUND,
                quantity=initial_stock,
                balance_after=initial_stock,
                note="Initial stock initialization"
            )
            db.add(tx)
            await db.commit()
            await db.refresh(item)

        return item

    @staticmethod
    async def adjust_stock(
        db: AsyncSession, variant_id: str, quantity_delta: int, reason: str
    ) -> InventoryItem:
        stmt = select(InventoryItem).where(InventoryItem.variant_id == variant_id)
        res = await db.execute(stmt)
        item = res.scalar_one_or_none()
        if not item:
            raise NotFoundException("Inventory item not found")

        item.physical_stock += quantity_delta
        if item.physical_stock < 0:
            raise BadRequestException("Physical stock cannot be negative")

        tx = InventoryTransaction(
            variant_id=variant_id,
            transaction_type=InventoryTxType.ADJUSTMENT if quantity_delta > 0 else InventoryTxType.SALE,
            quantity=quantity_delta,
            balance_after=item.physical_stock,
            note=reason
        )
        db.add(tx)
        await db.commit()
        await db.refresh(item)
        return item

    @staticmethod
    async def reserve_stock(
        db: AsyncSession, order_id: str, items: List[Tuple[str, int]] # (variant_id, qty)
    ) -> bool:
        """2-Phase Reservation: Atomically verifies and locks inventory"""
        expiry = datetime.now(timezone.utc) + timedelta(minutes=settings.STOCK_RESERVATION_EXPIRY_MINUTES)

        # 1. Verification phase
        for variant_id, qty in items:
            stmt = select(InventoryItem).where(InventoryItem.variant_id == variant_id)
            res = await db.execute(stmt)
            inv = res.scalar_one_or_none()

            # Auto-initialize if item not tracked yet
            if not inv:
                inv = await InventoryService.get_or_create_item(
                    db, variant_id=variant_id, sku=f"SKU-{variant_id[:8]}", vendor_id="default-vendor", initial_stock=50
                )

            available = inv.physical_stock - inv.reserved_stock
            if available < qty:
                raise BadRequestException(f"Insufficient stock for variant {inv.sku}. Only {available} available.")

        # 2. Reservation phase
        for variant_id, qty in items:
            stmt = select(InventoryItem).where(InventoryItem.variant_id == variant_id)
            res = await db.execute(stmt)
            inv = res.scalar_one()

            inv.reserved_stock += qty

            reservation = InventoryReservation(
                order_id=order_id,
                variant_id=variant_id,
                quantity=qty,
                status=ReservationStatus.ACTIVE,
                expires_at=expiry
            )
            db.add(reservation)

            tx = InventoryTransaction(
                variant_id=variant_id,
                transaction_type=InventoryTxType.RESERVATION,
                quantity=qty,
                reference_id=order_id,
                balance_after=inv.physical_stock - inv.reserved_stock,
                note=f"Stock reserved for Order {order_id}"
            )
            db.add(tx)

        await db.commit()
        await event_bus.publish(EventType.INVENTORY_RESERVED, {"order_id": order_id, "item_count": len(items)})
        return True

    @staticmethod
    async def commit_reservation(db: AsyncSession, order_id: str) -> None:
        """Payment confirmed: Deduct physical stock and clear reserved hold"""
        stmt = select(InventoryReservation).where(
            InventoryReservation.order_id == order_id,
            InventoryReservation.status == ReservationStatus.ACTIVE
        )
        res = await db.execute(stmt)
        reservations = list(res.scalars().all())

        for r in reservations:
            r.status = ReservationStatus.COMMITTED

            inv_stmt = select(InventoryItem).where(InventoryItem.variant_id == r.variant_id)
            inv_res = await db.execute(inv_stmt)
            inv = inv_res.scalar_one_or_none()
            if inv:
                inv.physical_stock -= r.quantity
                inv.reserved_stock -= r.quantity

                tx = InventoryTransaction(
                    variant_id=r.variant_id,
                    transaction_type=InventoryTxType.SALE,
                    quantity=-r.quantity,
                    reference_id=order_id,
                    balance_after=inv.physical_stock,
                    note=f"Sale finalized for Order {order_id}"
                )
                db.add(tx)

        await db.commit()

    @staticmethod
    async def release_reservation(db: AsyncSession, order_id: str) -> None:
        """Payment failed or cancelled: Release reserved hold back to pool"""
        stmt = select(InventoryReservation).where(
            InventoryReservation.order_id == order_id,
            InventoryReservation.status == ReservationStatus.ACTIVE
        )
        res = await db.execute(stmt)
        reservations = list(res.scalars().all())

        for r in reservations:
            r.status = ReservationStatus.RELEASED

            inv_stmt = select(InventoryItem).where(InventoryItem.variant_id == r.variant_id)
            inv_res = await db.execute(inv_stmt)
            inv = inv_res.scalar_one_or_none()
            if inv:
                inv.reserved_stock -= r.quantity

                tx = InventoryTransaction(
                    variant_id=r.variant_id,
                    transaction_type=InventoryTxType.RELEASE,
                    quantity=r.quantity,
                    reference_id=order_id,
                    balance_after=inv.physical_stock - inv.reserved_stock,
                    note=f"Reservation released for Order {order_id}"
                )
                db.add(tx)

        await db.commit()
        await event_bus.publish(EventType.INVENTORY_RELEASED, {"order_id": order_id})
