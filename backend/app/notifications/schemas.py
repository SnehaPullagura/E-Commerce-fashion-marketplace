from typing import Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.notifications.models import NotificationChannel


class NotificationCreate(BaseModel):
    user_id: str
    title: str
    message: str
    channel: NotificationChannel = NotificationChannel.IN_APP
    link_url: Optional[str] = None
    metadata_json: Dict[str, Any] = {}


class NotificationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    user_id: str
    title: str
    message: str
    channel: NotificationChannel
    link_url: Optional[str] = None
    is_read: bool
    metadata_json: Dict[str, Any] = {}
    created_at: datetime
