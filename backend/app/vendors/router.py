from typing import List, Optional
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import User, UserRole
from app.authentication.dependencies import get_current_user
from app.vendors.schemas import (
    VendorProfileOut,
    VendorOnboardRequest,
    VendorUpdateProfile,
    StorefrontOut,
)
from app.vendors.service import VendorService

router = APIRouter(prefix="/vendors", tags=["Marketplace Vendors & Storefronts"])


@router.post("/onboard", response_model=VendorProfileOut, status_code=status.HTTP_201_CREATED)
async def onboard_as_vendor(
    req: VendorOnboardRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await VendorService.onboard_vendor(db, current_user, req)


@router.get("/me", response_model=VendorProfileOut)
async def get_my_vendor_profile(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await VendorService.get_by_user_id(db, current_user.id)


@router.get("/store/{slug}", response_model=StorefrontOut)
async def get_vendor_storefront(
    slug: str,
    db: AsyncSession = Depends(get_db)
):
    return await VendorService.get_by_slug(db, slug)


@router.get("", response_model=List[VendorProfileOut])
async def list_all_vendors(db: AsyncSession = Depends(get_db)):
    return await VendorService.list_vendors(db)
