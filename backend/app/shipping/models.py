import enum
from typing import List, Optional
from datetime import datetime
from sqlalchemy import (
    String, Boolean, Float, DateTime, ForeignKey, Enum as SQLEnum, Text
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import BaseModel, get_utc_now


class ShipmentStatus(str, enum.Enum):
    LABEL_CREATED = "LABEL_CREATED"
    PICKED_UP = "PICKED_UP"
    IN_TRANSIT = "IN_TRANSIT"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERED = "DELIVERED"
    FAILED = "FAILED"
    RETURNED = "RETURNED"


class CourierType(str, enum.Enum):
    MOCK_EXPRESS = "MOCK_EXPRESS"
    BLUEDART = "BLUEDART"
    DELHIVERY = "DELHIVERY"
    FEDEX = "FEDEX"
    DTDC = "DTDC"


class Shipment(BaseModel):
    __tablename__ = "shipments"

    sub_order_id: Mapped[str] = mapped_column(String(36), ForeignKey("sub_orders.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    courier: Mapped[CourierType] = mapped_column(SQLEnum(CourierType), default=CourierType.MOCK_EXPRESS, nullable=False)
    waybill_number: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    shipping_label_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    status: Mapped[ShipmentStatus] = mapped_column(SQLEnum(ShipmentStatus), default=ShipmentStatus.LABEL_CREATED, nullable=False, index=True)
    estimated_delivery: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    actual_delivery: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    tracking_events: Mapped[List["TrackingEvent"]] = relationship("TrackingEvent", back_populates="shipment", cascade="all, delete-orphan")


class TrackingEvent(BaseModel):
    __tablename__ = "tracking_events"

    shipment_id: Mapped[str] = mapped_column(String(36), ForeignKey("shipments.id", ondelete="CASCADE"), nullable=False, index=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    location: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    event_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=get_utc_now, nullable=False)

    shipment: Mapped["Shipment"] = relationship("Shipment", back_populates="tracking_events")
