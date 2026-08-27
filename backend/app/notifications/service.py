import logging
from typing import List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from app.core.database import AsyncSessionLocal
from app.core.events import event_bus, EventType
from app.notifications.models import Notification, NotificationChannel
from app.notifications.schemas import NotificationCreate

logger = logging.getLogger(__name__)


class NotificationService:
    @staticmethod
    async def create(db: AsyncSession, req: NotificationCreate) -> Notification:
        notif = Notification(
            user_id=req.user_id,
            title=req.title,
            message=req.message,
            channel=req.channel,
            link_url=req.link_url,
            metadata_json=req.metadata_json,
            is_read=False
        )
        db.add(notif)
        await db.commit()
        await db.refresh(notif)
        return notif

    @staticmethod
    async def list_for_user(db: AsyncSession, user_id: str, unread_only: bool = False) -> List[Notification]:
        stmt = select(Notification).where(Notification.user_id == user_id, Notification.is_deleted == False)
        if unread_only:
            stmt = stmt.where(Notification.is_read == False)
        stmt = stmt.order_by(Notification.created_at.desc()).limit(50)
        res = await db.execute(stmt)
        return list(res.scalars().all())

    @staticmethod
    async def mark_read(db: AsyncSession, notification_id: str, user_id: str) -> None:
        await db.execute(
            update(Notification)
            .where(Notification.id == notification_id, Notification.user_id == user_id)
            .values(is_read=True)
        )
        await db.commit()


# Event listeners setup
async def handle_user_registered(payload: Dict[str, Any]):
    user_id = payload.get("user_id")
    if not user_id:
        return
    async with AsyncSessionLocal() as db:
        await NotificationService.create(
            db,
            NotificationCreate(
                user_id=user_id,
                title="Welcome to Fashion Marketplace! 👗✨",
                message="Complete your Fashion DNA and Size Profile to receive curated outfit recommendations.",
                channel=NotificationChannel.IN_APP,
                link_url="/profile/fashion-dna"
            )
        )


async def handle_order_created(payload: Dict[str, Any]):
    user_id = payload.get("user_id")
    order_num = payload.get("order_number")
    if not user_id:
        return
    async with AsyncSessionLocal() as db:
        await NotificationService.create(
            db,
            NotificationCreate(
                user_id=user_id,
                title="Order Placed! 🛍️",
                message=f"Your order {order_num} has been placed. Complete payment to begin vendor fulfillment.",
                channel=NotificationChannel.IN_APP,
                link_url=f"/orders/{payload.get('order_id')}"
            )
        )


# Register listeners to event bus
event_bus.subscribe(EventType.USER_REGISTERED, handle_user_registered)
event_bus.subscribe(EventType.ORDER_CREATED, handle_order_created)
