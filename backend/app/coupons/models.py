import enum
from datetime import datetime
from typing import Optional
from sqlalchemy import (
    String, Boolean, Float, Integer, DateTime, ForeignKey, Enum as SQLEnum
)
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base_model import BaseModel, get_utc_now


class DiscountType(str, enum.Enum):
    PERCENTAGE = "PERCENTAGE"
    FIXED = "FIXED"


class Coupon(BaseModel):
    __tablename__ = "coupons"

    code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False) # e.g. "FASHION10", "FESTIVE500"
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    discount_type: Mapped[DiscountType] = mapped_column(SQLEnum(DiscountType), default=DiscountType.PERCENTAGE, nullable=False)
    discount_value: Mapped[float] = mapped_column(Float, nullable=False) # e.g., 10.0 (10%) or 500.0 (Rs.500)
    min_order_amount: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    max_discount_amount: Mapped[Optional[float]] = mapped_column(Float, nullable=True) # Cap for percentage discount

    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=get_utc_now, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    usage_limit: Mapped[Optional[int]] = mapped_column(Integer, nullable=True) # Total global usages allowed
    used_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    per_user_limit: Mapped[int] = mapped_column(Integer, default=1, nullable=False)

    vendor_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True) # Vendor-specific coupon
    category_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("categories.id", ondelete="SET NULL"), nullable=True, index=True)
    is_first_order_only: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, index=True)


class CouponUsage(BaseModel):
    __tablename__ = "coupon_usages"

    coupon_id: Mapped[str] = mapped_column(String(36), ForeignKey("coupons.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    order_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    discount_applied: Mapped[float] = mapped_column(Float, nullable=False)
