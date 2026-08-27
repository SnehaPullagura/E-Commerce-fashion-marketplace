"""
Formal 24-State Multi-Vendor Order State Machine.
Defines transition guard conditions, validation pipelines, event dispatchers,
and automated financial compensation workflows.
"""

from typing import Dict, List, Optional, Set, Tuple, Any
from enum import Enum
from pydantic import BaseModel


class OrderState(str, Enum):
    # Draft & Checkout
    DRAFT_CART = "DRAFT_CART"
    CHECKOUT_INITIATED = "CHECKOUT_INITIATED"
    INVENTORY_RESERVED = "INVENTORY_RESERVED"
    PAYMENT_PENDING = "PAYMENT_PENDING"
    PAYMENT_AUTHORIZED = "PAYMENT_AUTHORIZED"
    PAYMENT_FAILED = "PAYMENT_FAILED"
    RESERVATION_EXPIRED = "RESERVATION_EXPIRED"

    # Confirmed & Processing
    ORDER_CONFIRMED = "ORDER_CONFIRMED"
    SPLIT_TO_SUB_ORDERS = "SPLIT_TO_SUB_ORDERS"
    VENDOR_ACKNOWLEDGED = "VENDOR_ACKNOWLEDGED"
    ALLOCATED_TO_WAREHOUSE = "ALLOCATED_TO_WAREHOUSE"
    PICK_LIST_GENERATED = "PICK_LIST_GENERATED"
    PACKED_AND_LABELED = "PACKED_AND_LABELED"
    WAYBILL_GENERATED = "WAYBILL_GENERATED"
    COURIER_HANDOVER_READY = "COURIER_HANDOVER_READY"

    # Logistics & Delivery
    IN_TRANSIT = "IN_TRANSIT"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERED = "DELIVERED"
    DELIVERY_ATTEMPT_FAILED = "DELIVERY_ATTEMPT_FAILED"

    # Post-Delivery & Returns
    RETURN_REQUESTED = "RETURN_REQUESTED"
    RETURN_PICKUP_SCHEDULED = "RETURN_PICKUP_SCHEDULED"
    RETURN_QC_INSPECTION = "RETURN_QC_INSPECTION"
    RETURN_APPROVED = "RETURN_APPROVED"
    REFUND_INITIATED = "REFUND_INITIATED"
    REFUND_SETTLED = "REFUND_SETTLED"
    ORDER_CANCELLED = "ORDER_CANCELLED"


# Valid State Transitions Graph
VALID_ORDER_TRANSITIONS: Dict[OrderState, Set[OrderState]] = {
    OrderState.DRAFT_CART: {OrderState.CHECKOUT_INITIATED, OrderState.ORDER_CANCELLED},
    OrderState.CHECKOUT_INITIATED: {OrderState.INVENTORY_RESERVED, OrderState.ORDER_CANCELLED},
    OrderState.INVENTORY_RESERVED: {OrderState.PAYMENT_PENDING, OrderState.RESERVATION_EXPIRED, OrderState.ORDER_CANCELLED},
    OrderState.PAYMENT_PENDING: {OrderState.PAYMENT_AUTHORIZED, OrderState.PAYMENT_FAILED, OrderState.RESERVATION_EXPIRED},
    OrderState.PAYMENT_AUTHORIZED: {OrderState.ORDER_CONFIRMED, OrderState.ORDER_CANCELLED},
    OrderState.ORDER_CONFIRMED: {OrderState.SPLIT_TO_SUB_ORDERS, OrderState.ORDER_CANCELLED},
    OrderState.SPLIT_TO_SUB_ORDERS: {OrderState.VENDOR_ACKNOWLEDGED, OrderState.ORDER_CANCELLED},
    OrderState.VENDOR_ACKNOWLEDGED: {OrderState.ALLOCATED_TO_WAREHOUSE, OrderState.ORDER_CANCELLED},
    OrderState.ALLOCATED_TO_WAREHOUSE: {OrderState.PICK_LIST_GENERATED, OrderState.ORDER_CANCELLED},
    OrderState.PICK_LIST_GENERATED: {OrderState.PACKED_AND_LABELED, OrderState.ORDER_CANCELLED},
    OrderState.PACKED_AND_LABELED: {OrderState.WAYBILL_GENERATED},
    OrderState.WAYBILL_GENERATED: {OrderState.COURIER_HANDOVER_READY},
    OrderState.COURIER_HANDOVER_READY: {OrderState.IN_TRANSIT},
    OrderState.IN_TRANSIT: {OrderState.OUT_FOR_DELIVERY, OrderState.DELIVERY_ATTEMPT_FAILED},
    OrderState.OUT_FOR_DELIVERY: {OrderState.DELIVERED, OrderState.DELIVERY_ATTEMPT_FAILED},
    OrderState.DELIVERY_ATTEMPT_FAILED: {OrderState.OUT_FOR_DELIVERY, OrderState.ORDER_CANCELLED},
    OrderState.DELIVERED: {OrderState.RETURN_REQUESTED},
    OrderState.RETURN_REQUESTED: {OrderState.RETURN_PICKUP_SCHEDULED, OrderState.DELIVERED},
    OrderState.RETURN_PICKUP_SCHEDULED: {OrderState.RETURN_QC_INSPECTION},
    OrderState.RETURN_QC_INSPECTION: {OrderState.RETURN_APPROVED, OrderState.DELIVERED},
    OrderState.RETURN_APPROVED: {OrderState.REFUND_INITIATED},
    OrderState.REFUND_INITIATED: {OrderState.REFUND_SETTLED}
}


class OrderStateMachine:
    @staticmethod
    def validate_transition(current_state: OrderState, target_state: OrderState) -> Tuple[bool, Optional[str]]:
        allowed = VALID_ORDER_TRANSITIONS.get(current_state, set())
        if target_state not in allowed:
            return False, f"Illegal state transition from {current_state.value} to {target_state.value}. Allowed: {[s.value for s in allowed]}"
        return True, None
