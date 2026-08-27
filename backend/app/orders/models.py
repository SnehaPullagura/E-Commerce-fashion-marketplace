import enum
from typing import List, Optional
from datetime import datetime
from sqlalchemy import (
    String, Boolean, Float, Integer, JSON, ForeignKey, Enum as SQLEnum, Text, DateTime
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import BaseModel, get_utc_now


class OrderStatus(str, enum.Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    PROCESSING = "PROCESSING"
    PACKED = "PACKED"
    SHIPPED = "SHIPPED"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"
    RETURN_REQUESTED = "RETURN_REQUESTED"
    RETURNED = "RETURNED"
    REFUNDED = "REFUNDED"


class PaymentStatus(str, enum.Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"
    PARTIALLY_REFUNDED = "PARTIALLY_REFUNDED"


class Order(BaseModel):
    __tablename__ = "orders"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="RESTRICT"), nullable=False, index=True)
    order_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False) # e.g. FM-2026-98124

    total_amount: Mapped[float] = mapped_column(Float, nullable=False) # Final paid amount
    subtotal: Mapped[float] = mapped_column(Float, nullable=False)
    shipping_fee: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    discount_amount: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    coupon_code: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    status: Mapped[OrderStatus] = mapped_column(SQLEnum(OrderStatus), default=OrderStatus.PENDING, nullable=False, index=True)
    payment_status: Mapped[PaymentStatus] = mapped_column(SQLEnum(PaymentStatus), default=PaymentStatus.PENDING, nullable=False, index=True)
    payment_method: Mapped[str] = mapped_column(String(50), default="UPI", nullable=False) # UPI, CARD, COD, NETBANKING

    shipping_address_snapshot: Mapped[dict] = mapped_column(JSON, nullable=False)
    billing_address_snapshot: Mapped[dict] = mapped_column(JSON, nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # Relationships
    sub_orders: Mapped[List["SubOrder"]] = relationship("SubOrder", back_populates="order", cascade="all, delete-orphan")
    items: Mapped[List["OrderItem"]] = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    status_history: Mapped[List["OrderStatusHistory"]] = relationship("OrderStatusHistory", back_populates="order", cascade="all, delete-orphan")


class SubOrder(BaseModel):
    """Split order per vendor for independent fulfillment and settlement"""
    __tablename__ = "sub_orders"

    order_id: Mapped[str] = mapped_column(String(36), ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, index=True)
    vendor_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    sub_order_number: Mapped[str] = mapped_column(String(60), unique=True, index=True, nullable=False) # e.g. FM-2026-98124-V1

    subtotal: Mapped[float] = mapped_column(Float, nullable=False)
    shipping_fee: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    commission_rate: Mapped[float] = mapped_column(Float, default=15.0, nullable=False) # %
    commission_amount: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    vendor_payout: Mapped[float] = mapped_column(Float, nullable=False) # subtotal - commission_amount

    status: Mapped[OrderStatus] = mapped_column(SQLEnum(OrderStatus), default=OrderStatus.PENDING, nullable=False, index=True)
    tracking_number: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    courier_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    # Relationships
    order: Mapped["Order"] = relationship("Order", back_populates="sub_orders")
    items: Mapped[List["OrderItem"]] = relationship("OrderItem", back_populates="sub_order")


class OrderItem(BaseModel):
    __tablename__ = "order_items"

    order_id: Mapped[str] = mapped_column(String(36), ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, index=True)
    sub_order_id: Mapped[str] = mapped_column(String(36), ForeignKey("sub_orders.id", ondelete="CASCADE"), nullable=False, index=True)
    product_id: Mapped[str] = mapped_column(String(36), ForeignKey("products.id", ondelete="RESTRICT"), nullable=False, index=True)
    variant_id: Mapped[str] = mapped_column(String(36), ForeignKey("product_variants.id", ondelete="RESTRICT"), nullable=False, index=True)

    product_title: Mapped[str] = mapped_column(String(255), nullable=False)
    product_slug: Mapped[str] = mapped_column(String(280), nullable=False)
    brand_name: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    image_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    selected_size: Mapped[str] = mapped_column(String(30), nullable=False)
    selected_color: Mapped[str] = mapped_column(String(50), nullable=False)
    sku: Mapped[str] = mapped_column(String(100), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)
    total_price: Mapped[float] = mapped_column(Float, nullable=False)

    order: Mapped["Order"] = relationship("Order", back_populates="items")
    sub_order: Mapped["SubOrder"] = relationship("SubOrder", back_populates="items")


class OrderStatusHistory(BaseModel):
    __tablename__ = "order_status_history"

    order_id: Mapped[str] = mapped_column(String(36), ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, index=True)
    sub_order_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    from_status: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    to_status: Mapped[str] = mapped_column(String(50), nullable=False)
    note: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    changed_by: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)

    order: Mapped["Order"] = relationship("Order", back_populates="status_history")
