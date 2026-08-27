from typing import List, Optional, Tuple, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload

from app.core.exceptions import NotFoundException, ConflictException, ForbiddenException
from app.users.models import User, UserRole
from app.products.models import Product, ProductStatus
from app.vendors.models import VendorProfile, VendorDocument, VendorPayout, VendorStatus
from app.vendors.schemas import VendorOnboardRequest, VendorUpdateProfile


class VendorService:
    @staticmethod
    async def onboard_vendor(db: AsyncSession, user: User, req: VendorOnboardRequest) -> VendorProfile:
        # Check if slug exists
        stmt = select(VendorProfile).where(VendorProfile.slug == req.slug.lower())
        res = await db.execute(stmt)
        if res.scalar_one_or_none():
            raise ConflictException(f"Vendor store slug '{req.slug}' is already taken")

        # Check if user already has a vendor profile
        user_stmt = select(VendorProfile).where(VendorProfile.user_id == user.id)
        user_res = await db.execute(user_stmt)
        if user_res.scalar_one_or_none():
            raise ConflictException("You already have an existing vendor profile")

        # Update user role to VENDOR_OWNER
        user.role = UserRole.VENDOR_OWNER

        vendor = VendorProfile(
            user_id=user.id,
            business_name=req.business_name,
            legal_name=req.legal_name,
            slug=req.slug.lower(),
            gst_number=req.gst_number,
            pan_number=req.pan_number,
            bank_account_name=req.bank_account_name,
            bank_account_number=req.bank_account_number,
            bank_ifsc=req.bank_ifsc,
            bank_name=req.bank_name,
            city=req.city,
            state=req.state,
            postal_code=req.postal_code,
            description=req.description,
            support_email=req.support_email or user.email,
            support_phone=req.support_phone or user.phone,
            status=VendorStatus.APPROVED # Auto-approve in dev or set to PENDING
        )
        db.add(vendor)
        await db.commit()
        await db.refresh(vendor)
        return vendor

    @staticmethod
    async def get_by_user_id(db: AsyncSession, user_id: str) -> VendorProfile:
        stmt = select(VendorProfile).where(VendorProfile.user_id == user_id, VendorProfile.is_deleted == False)
        res = await db.execute(stmt)
        vendor = res.scalar_one_or_none()
        if not vendor:
            raise NotFoundException("Vendor profile not found")
        return vendor

    @staticmethod
    async def get_by_slug(db: AsyncSession, slug: str) -> Dict[str, Any]:
        stmt = select(VendorProfile).where(VendorProfile.slug == slug.lower(), VendorProfile.is_deleted == False)
        res = await db.execute(stmt)
        vendor = res.scalar_one_or_none()
        if not vendor:
            raise NotFoundException("Vendor not found")

        # Fetch active products for this vendor
        prod_stmt = (
            select(Product)
            .options(selectinload(Product.brand), selectinload(Product.images), selectinload(Product.variants))
            .where(Product.vendor_id == vendor.user_id, Product.status == ProductStatus.PUBLISHED)
        )
        prod_res = await db.execute(prod_stmt)
        products = list(prod_res.scalars().all())

        product_list = []
        for p in products:
            primary_img = next((img.image_url for img in p.images if img.is_primary), None)
            if not primary_img and p.images:
                primary_img = p.images[0].image_url

            product_list.append({
                "id": p.id,
                "title": p.title,
                "slug": p.slug,
                "base_mrp": p.base_mrp,
                "base_price": p.base_price,
                "discount_percentage": p.discount_percentage,
                "primary_image": primary_img,
                "fit_type": p.fit_type.value,
                "occasion": p.occasion.value,
                "average_rating": p.average_rating,
                "review_count": p.review_count
            })

        return {
            "id": vendor.id,
            "business_name": vendor.business_name,
            "slug": vendor.slug,
            "logo_url": vendor.logo_url,
            "banner_url": vendor.banner_url,
            "description": vendor.description,
            "rating": vendor.rating,
            "city": vendor.city,
            "state": vendor.state,
            "products_count": len(product_list),
            "products": product_list
        }

    @staticmethod
    async def list_vendors(db: AsyncSession) -> List[VendorProfile]:
        stmt = select(VendorProfile).where(VendorProfile.is_deleted == False).order_by(VendorProfile.created_at.desc())
        res = await db.execute(stmt)
        return list(res.scalars().all())
