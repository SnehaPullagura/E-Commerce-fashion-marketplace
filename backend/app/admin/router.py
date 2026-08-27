from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.users.models import UserRole
from app.authentication.dependencies import require_roles
from app.vendors.schemas import VendorProfileOut
from app.products.schemas import ProductOut
from app.admin.models import PlatformSetting
from app.admin.schemas import (
    AdminOverviewStats,
    ModerateVendorRequest,
    ModerateProductRequest,
    PlatformSettingCreate,
    PlatformSettingOut,
)
from app.admin.service import AdminService

router = APIRouter(
    prefix="/admin",
    tags=["Admin & Platform Governance"],
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN]))]
)


@router.get("/stats", response_model=AdminOverviewStats)
async def get_overview_metrics(db: AsyncSession = Depends(get_db)):
    return await AdminService.get_overview_stats(db)


@router.put("/vendors/{vendor_id}/moderate", response_model=VendorProfileOut)
async def moderate_vendor(
    vendor_id: str,
    req: ModerateVendorRequest,
    db: AsyncSession = Depends(get_db)
):
    return await AdminService.moderate_vendor(db, vendor_id, req)


@router.put("/products/{product_id}/moderate", response_model=ProductOut)
async def moderate_product(
    product_id: str,
    req: ModerateProductRequest,
    db: AsyncSession = Depends(get_db)
):
    return await AdminService.moderate_product(db, product_id, req)


@router.post("/settings", response_model=PlatformSettingOut)
async def update_platform_setting(
    req: PlatformSettingCreate,
    db: AsyncSession = Depends(get_db)
):
    return await AdminService.set_setting(db, req)


@router.get("/settings", response_model=List[PlatformSettingOut])
async def list_platform_settings(db: AsyncSession = Depends(get_db)):
    stmt = select(PlatformSetting)
    res = await db.execute(stmt)
    return list(res.scalars().all())
