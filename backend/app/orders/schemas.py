from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from app.orders.models import OrderStatus, PaymentStatus


class CheckoutRequest(BaseModel):
    shipping_address_id: str
    billing_address_id: Optional[str] = None
    payment_method: str = "UPI" # UPI, CARD, COD, NETBANKING
    coupon_code: Optional[str] = None
    customer_notes: Optional[str] = None


class OrderItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    product_id: str
    variant_id: str
    product_title: str
    product_slug: str
    brand_name: Optional[str] = None
    image_url: Optional[str] = None
    selected_size: str
    selected_color: str
    sku: str
    quantity: int
    unit_price: float
    total_price: float


class SubOrderOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    vendor_id: str
    sub_order_number: str
    subtotal: float
    shipping_fee: float
    commission_rate: float
    commission_amount: float
    vendor_payout: float
    status: OrderStatus
    tracking_number: Optional[str] = None
    courier_name: Optional[str] = None
    items: List[OrderItemOut] = []


class OrderStatusHistoryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    from_status: Optional[str] = None
    to_status: str
    note: Optional[str] = None
    created_at: datetime


class OrderOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    user_id: str
    order_number: str
    total_amount: float
    subtotal: float
    shipping_fee: float
    discount_amount: float
    coupon_code: Optional[str] = None
    status: OrderStatus
    payment_status: PaymentStatus
    payment_method: str
    shipping_address_snapshot: Dict[str, Any]
    billing_address_snapshot: Dict[str, Any]
    notes: Optional[str] = None
    created_at: datetime
    sub_orders: List[SubOrderOut] = []
    items: List[OrderItemOut] = []
    status_history: List[OrderStatusHistoryOut] = []


class UpdateOrderStatusRequest(BaseModel):
    status: OrderStatus
    note: Optional[str] = None
    tracking_number: Optional[str] = None
    courier_name: Optional[str] = None
