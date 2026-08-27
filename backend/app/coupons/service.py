from datetime import datetime, timezone
from typing import List, Optional, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, func

from app.core.exceptions import NotFoundException, ConflictException, BadRequestException
from app.coupons.models import Coupon, CouponUsage, DiscountType
from app.coupons.schemas import CouponCreate, CouponUpdate, ApplyCouponResponse


class CouponService:
    @staticmethod
    async def create(db: AsyncSession, coupon_in: CouponCreate) -> Coupon:
        stmt = select(Coupon).where(Coupon.code == coupon_in.code.upper())
        res = await db.execute(stmt)
        if res.scalar_one_or_none():
            raise ConflictException(f"Coupon code '{coupon_in.code}' already exists")

        coupon = Coupon(
            code=coupon_in.code.upper(),
            **coupon_in.model_dump(exclude={"code"})
        )
        db.add(coupon)
        await db.commit()
        await db.refresh(coupon)
        return coupon

    @staticmethod
    async def list_active(db: AsyncSession) -> List[Coupon]:
        now = datetime.now(timezone.utc)
        stmt = (
            select(Coupon)
            .where(
                Coupon.is_active == True,
                Coupon.start_date <= now,
                Coupon.end_date >= now
            )
            .order_by(Coupon.created_at.desc())
        )
        res = await db.execute(stmt)
        return list(res.scalars().all())

    @staticmethod
    async def validate_and_apply(
        db: AsyncSession,
        code: str,
        cart_amount: float,
        user_id: Optional[str] = None,
        vendor_id: Optional[str] = None,
        category_id: Optional[str] = None
    ) -> ApplyCouponResponse:
        now = datetime.now(timezone.utc)
        stmt = select(Coupon).where(Coupon.code == code.upper(), Coupon.is_active == True)
        res = await db.execute(stmt)
        coupon = res.scalar_one_or_none()

        if not coupon:
            return ApplyCouponResponse(is_valid=False, code=code, discount_amount=0.0, message="Invalid coupon code")

        if coupon.start_date > now or coupon.end_date < now:
            return ApplyCouponResponse(is_valid=False, code=code, discount_amount=0.0, message="Coupon has expired")

        if coupon.usage_limit and coupon.used_count >= coupon.usage_limit:
            return ApplyCouponResponse(is_valid=False, code=code, discount_amount=0.0, message="Coupon usage limit reached")

        if cart_amount < coupon.min_order_amount:
            return ApplyCouponResponse(
                is_valid=False,
                code=code,
                discount_amount=0.0,
                message=f"Minimum order value of ₹{coupon.min_order_amount:.0f} required for this coupon"
            )

        if coupon.vendor_id and vendor_id and coupon.vendor_id != vendor_id:
            return ApplyCouponResponse(
                is_valid=False,
                code=code,
                discount_amount=0.0,
                message="Coupon is only applicable to specific vendor items"
            )

        # Check per-user limit
        if user_id:
            usage_stmt = select(func.count(CouponUsage.id)).where(
                CouponUsage.coupon_id == coupon.id,
                CouponUsage.user_id == user_id
            )
            usage_res = await db.execute(usage_stmt)
            user_count = usage_res.scalar() or 0
            if user_count >= coupon.per_user_limit:
                return ApplyCouponResponse(
                    is_valid=False,
                    code=code,
                    discount_amount=0.0,
                    message="You have already reached the maximum usage limit for this coupon"
                )

        # Calculate discount
        if coupon.discount_type == DiscountType.PERCENTAGE:
            discount = (cart_amount * coupon.discount_value) / 100.0
            if coupon.max_discount_amount:
                discount = min(discount, coupon.max_discount_amount)
        else: # FIXED
            discount = min(coupon.discount_value, cart_amount)

        return ApplyCouponResponse(
            is_valid=True,
            code=coupon.code,
            discount_amount=round(discount, 2),
            message=f"Coupon applied! Saved ₹{discount:.2f}"
        )

    @staticmethod
    async def record_usage(
        db: AsyncSession,
        coupon_id: str,
        user_id: str,
        order_id: Optional[str],
        discount_applied: float
    ) -> None:
        usage = CouponUsage(
            coupon_id=coupon_id,
            user_id=user_id,
            order_id=order_id,
            discount_applied=discount_applied
        )
        db.add(usage)

        # Increment used count
        await db.execute(
            update(Coupon)
            .where(Coupon.id == coupon_id)
            .values(used_count=Coupon.used_count + 1)
        )
        await db.commit()
