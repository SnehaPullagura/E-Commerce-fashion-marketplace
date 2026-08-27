import enum
from typing import Optional
from datetime import datetime
from sqlalchemy import (
    String, Boolean, Float, JSON, ForeignKey, Enum as SQLEnum, Text, DateTime
)
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base_model import BaseModel, get_utc_now


class PaymentGatewayType(str, enum.Enum):
    MOCK = "MOCK"
    RAZORPAY = "RAZORPAY"
    STRIPE = "STRIPE"
    UPI = "UPI"
    COD = "COD"


class PaymentTxStatus(str, enum.Enum):
    INITIATED = "INITIATED"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"
    PARTIALLY_REFUNDED = "PARTIALLY_REFUNDED"


class PaymentTransaction(BaseModel):
    __tablename__ = "payment_transactions"

    order_id: Mapped[str] = mapped_column(String(36), ForeignKey("orders.id", ondelete="RESTRICT"), nullable=False, index=True)
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="RESTRICT"), nullable=False, index=True)
    transaction_reference: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    idempotency_key: Mapped[Optional[str]] = mapped_column(String(100), unique=True, index=True, nullable=True)

    payment_gateway: Mapped[PaymentGatewayType] = mapped_column(SQLEnum(PaymentGatewayType), default=PaymentGatewayType.MOCK, nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    currency: Mapped[str] = mapped_column(String(10), default="INR", nullable=False)
    status: Mapped[PaymentTxStatus] = mapped_column(SQLEnum(PaymentTxStatus), default=PaymentTxStatus.INITIATED, nullable=False, index=True)

    payment_method: Mapped[str] = mapped_column(String(50), default="UPI", nullable=False)
    gateway_order_id: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    gateway_payment_id: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    gateway_signature: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    gateway_response: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
    error_message: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)


class Refund(BaseModel):
    __tablename__ = "refunds"

    order_id: Mapped[str] = mapped_column(String(36), ForeignKey("orders.id", ondelete="RESTRICT"), nullable=False, index=True)
    sub_order_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    payment_transaction_id: Mapped[str] = mapped_column(String(36), ForeignKey("payment_transactions.id", ondelete="RESTRICT"), nullable=False)
    refund_reference: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    reason: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="PROCESSED", nullable=False) # INITIATED, PROCESSED, FAILED
    processed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=get_utc_now, nullable=False)
