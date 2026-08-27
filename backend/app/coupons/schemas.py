from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from app.coupons.models import DiscountType


class CouponBase(BaseModel):
    code: str
    description: Optional[str] = None
    discount_type: DiscountType = DiscountType.PERCENTAGE
    discount_value: float
    min_order_amount: float = 0.0
    max_discount_amount: Optional[float] = None
    start_date: datetime
    end_date: datetime
    usage_limit: Optional[int] = None
    per_user_limit: int = 1
    vendor_id: Optional[str] = None
    category_id: Optional[str] = None
    is_first_order_only: bool = False
    is_active: bool = True


class CouponCreate(CouponBase):
    pass


class CouponUpdate(BaseModel):
    description: Optional[str] = None
    discount_type: Optional[DiscountType] = None
    discount_value: Optional[float] = None
    min_order_amount: Optional[float] = None
    max_discount_amount: Optional[float] = None
    end_date: Optional[datetime] = None
    usage_limit: Optional[int] = None
    per_user_limit: Optional[int] = None
    is_active: Optional[bool] = None


class CouponOut(CouponBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    used_count: int
    created_at: datetime


class ApplyCouponRequest(BaseModel):
    code: str
    cart_amount: float
    vendor_id: Optional[str] = None
    category_id: Optional[str] = None


class ApplyCouponResponse(BaseModel):
    is_valid: bool
    code: str
    discount_amount: float
    message: str
