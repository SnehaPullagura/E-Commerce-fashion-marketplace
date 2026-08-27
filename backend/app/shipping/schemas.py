from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.shipping.models import ShipmentStatus, CourierType


class TrackingEventOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    status: str
    location: str
    description: str
    event_time: datetime


class ShipmentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    sub_order_id: str
    courier: CourierType
    waybill_number: str
    shipping_label_url: Optional[str] = None
    status: ShipmentStatus
    estimated_delivery: Optional[datetime] = None
    actual_delivery: Optional[datetime] = None
    created_at: datetime
    tracking_events: List[TrackingEventOut] = []


class CreateShipmentRequest(BaseModel):
    sub_order_id: str
    courier: CourierType = CourierType.MOCK_EXPRESS
