import asyncio
import logging
from typing import Any, Callable, Coroutine, Dict, List, Union
from enum import Enum

logger = logging.getLogger(__name__)


class EventType(str, Enum):
    # Order & Shipping Events
    ORDER_CREATED = "ORDER_CREATED"
    ORDER_CONFIRMED = "ORDER_CONFIRMED"
    ORDER_CANCELLED = "ORDER_CANCELLED"
    SHIPMENT_CREATED = "SHIPMENT_CREATED"
    ORDER_SHIPPED = "ORDER_SHIPPED"
    ORDER_DELIVERED = "ORDER_DELIVERED"
    RETURN_REQUESTED = "RETURN_REQUESTED"
    RETURN_COMPLETED = "RETURN_COMPLETED"

    # Payment Events
    PAYMENT_INITIATED = "PAYMENT_INITIATED"
    PAYMENT_COMPLETED = "PAYMENT_COMPLETED"
    PAYMENT_FAILED = "PAYMENT_FAILED"
    REFUND_COMPLETED = "REFUND_COMPLETED"

    # Inventory Events
    INVENTORY_RESERVED = "INVENTORY_RESERVED"
    INVENTORY_RELEASED = "INVENTORY_RELEASED"
    STOCK_LOW = "STOCK_LOW"
    STOCK_OUT = "STOCK_OUT"

    # Product Events
    PRODUCT_CREATED = "PRODUCT_CREATED"
    PRODUCT_UPDATED = "PRODUCT_UPDATED"
    PRICE_CHANGED = "PRICE_CHANGED"

    # User & Engagement Events
    USER_REGISTERED = "USER_REGISTERED"
    REVIEW_CREATED = "REVIEW_CREATED"
    PRICE_DROP = "PRICE_DROP"


EventHandler = Callable[[Dict[str, Any]], Coroutine[Any, Any, None]]


class EventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[EventHandler]] = {}

    def subscribe(self, event_type: Union[EventType, str], handler: EventHandler) -> None:
        key = event_type.value if isinstance(event_type, EventType) else str(event_type)
        if key not in self._subscribers:
            self._subscribers[key] = []
        self._subscribers[key].append(handler)
        logger.debug("Subscribed %s to event %s", handler.__name__, key)

    async def publish(self, event_type: Union[EventType, str], payload: Dict[str, Any]) -> None:
        key = event_type.value if isinstance(event_type, EventType) else str(event_type)
        handlers = self._subscribers.get(key, [])
        logger.info("Event published: %s with %d subscribers", key, len(handlers))

        for handler in handlers:
            try:
                # Run handler safely as background task or coroutine
                asyncio.create_task(self._safe_execute(handler, payload, key))
            except Exception as e:
                logger.error("Error scheduling event handler %s for %s: %s", getattr(handler, "__name__", "unknown"), key, str(e))

    async def _safe_execute(self, handler: EventHandler, payload: Dict[str, Any], key: str) -> None:
        try:
            await handler(payload)
        except Exception as e:
            logger.error("Error executing handler %s for event %s: %s", getattr(handler, "__name__", "unknown"), key, str(e), exc_info=True)


event_bus = EventBus()
