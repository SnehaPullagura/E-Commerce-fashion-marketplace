from typing import List, Optional
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import User, UserRole
from app.authentication.dependencies import get_current_user_optional, require_roles
from app.coupons.schemas import (
    CouponOut,
    CouponCreate,
    ApplyCouponRequest,
    ApplyCouponResponse,
)
from app.coupons.service import CouponService

router = APIRouter(prefix="/coupons", tags=["Promotional Coupons"])


@router.get("", response_model=List[CouponOut])
async def list_available_coupons(db: AsyncSession = Depends(get_db)):
    return await CouponService.list_active(db)


@router.post("/apply", response_model=ApplyCouponResponse)
async def apply_coupon_to_cart(
    req: ApplyCouponRequest,
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    user_id = current_user.id if current_user else None
    return await CouponService.validate_and_apply(
        db,
        code=req.code,
        cart_amount=req.cart_amount,
        user_id=user_id,
        vendor_id=req.vendor_id,
        category_id=req.category_id
    )


@router.post(
    "",
    response_model=CouponOut,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN]))]
)
async def create_coupon(coupon_in: CouponCreate, db: AsyncSession = Depends(get_db)):
    return await CouponService.create(db, coupon_in)
