from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import User, UserRole
from app.authentication.dependencies import get_current_user, require_roles
from app.analytics.schemas import (
    MarketplaceOverviewAnalytics,
    VendorAnalyticsSummary,
    FashionTrendRadar,
    ConversionFunnelResponse,
)
from app.analytics.service import AnalyticsService

router = APIRouter(prefix="/analytics", tags=["Business Intelligence & Analytics"])


@router.get(
    "/overview",
    response_model=MarketplaceOverviewAnalytics,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN]))]
)
async def get_marketplace_analytics(
    days: int = Query(30, ge=1, le=365),
    db: AsyncSession = Depends(get_db)
):
    return await AnalyticsService.get_overview(db, days=days)


@router.get("/vendor/me", response_model=VendorAnalyticsSummary)
async def get_my_vendor_analytics(
    days: int = Query(30, ge=1, le=365),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await AnalyticsService.get_vendor_analytics(db, vendor_id=current_user.id, days=days)


@router.get("/trends", response_model=FashionTrendRadar)
async def get_fashion_trend_radar(db: AsyncSession = Depends(get_db)):
    return await AnalyticsService.get_trend_radar(db)


@router.get(
    "/funnel",
    response_model=ConversionFunnelResponse,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN]))]
)
async def get_conversion_funnel(db: AsyncSession = Depends(get_db)):
    return await AnalyticsService.get_conversion_funnel(db)
