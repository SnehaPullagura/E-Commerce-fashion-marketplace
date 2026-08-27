import enum
from datetime import datetime
from typing import Optional
from sqlalchemy import (
    String, Boolean, Integer, DateTime, ForeignKey, Enum as SQLEnum, Text
)
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base_model import BaseModel, get_utc_now


class ReservationStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    COMMITTED = "COMMITTED"
    RELEASED = "RELEASED"


class InventoryTxType(str, enum.Enum):
    INBOUND = "INBOUND"
    RESERVATION = "RESERVATION"
    SALE = "SALE"
    RELEASE = "RELEASE"
    RESTOCK = "RESTOCK"
    RETURN = "RETURN"
    ADJUSTMENT = "ADJUSTMENT"


class InventoryItem(BaseModel):
    __tablename__ = "inventory_items"

    variant_id: Mapped[str] = mapped_column(String(36), ForeignKey("product_variants.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    sku: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    vendor_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    physical_stock: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    reserved_stock: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    low_stock_threshold: Mapped[int] = mapped_column(Integer, default=5, nullable=False)
    warehouse_location: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    @property
    def available_stock(self) -> int:
        return max(0, self.physical_stock - self.reserved_stock)


class InventoryReservation(BaseModel):
    __tablename__ = "inventory_reservations"

    order_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    variant_id: Mapped[str] = mapped_column(String(36), ForeignKey("product_variants.id", ondelete="CASCADE"), nullable=False, index=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[ReservationStatus] = mapped_column(SQLEnum(ReservationStatus), default=ReservationStatus.ACTIVE, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class InventoryTransaction(BaseModel):
    __tablename__ = "inventory_transactions"

    variant_id: Mapped[str] = mapped_column(String(36), ForeignKey("product_variants.id", ondelete="CASCADE"), nullable=False, index=True)
    transaction_type: Mapped[InventoryTxType] = mapped_column(SQLEnum(InventoryTxType), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False) # Can be positive or negative
    reference_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True) # Order ID or Adjustment note
    balance_after: Mapped[int] = mapped_column(Integer, nullable=False)
    note: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
