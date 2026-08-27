from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import User, UserRole
from app.authentication.dependencies import get_current_user, require_roles
from app.products.models import (
    ProductStatus,
    ProductGender,
    FitType,
    OccasionType,
    SeasonType,
)
from app.products.schemas import (
    ProductOut,
    ProductListOut,
    ProductCreate,
    ProductUpdate,
    ProductVariantCreate,
    ProductVariantOut,
    ProductImageCreate,
    ProductImageOut,
    BrandOut,
    BrandCreate,
    BrandSizeChartCreate,
    BrandSizeChartOut,
    SizeAdvisorRequest,
    SizeAdvisorResponse,
)
from app.products.service import ProductService

router = APIRouter(tags=["Fashion Products & Brands"])


# --- Brand Endpoints ---
@router.get("/brands", response_model=List[BrandOut])
async def list_brands(db: AsyncSession = Depends(get_db)):
    return await ProductService.get_all_brands(db)


@router.post(
    "/brands",
    response_model=BrandOut,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN]))]
)
async def create_brand(brand_in: BrandCreate, db: AsyncSession = Depends(get_db)):
    return await ProductService.create_brand(db, brand_in)


# --- Size Chart Endpoints ---
@router.post(
    "/size-charts",
    response_model=BrandSizeChartOut,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.VENDOR_OWNER]))]
)
async def create_size_chart(chart_in: BrandSizeChartCreate, db: AsyncSession = Depends(get_db)):
    return await ProductService.create_size_chart(db, chart_in)


# --- Product Endpoints ---
@router.get("/products")
async def list_products(
    category_id: Optional[str] = None,
    brand_id: Optional[str] = None,
    gender: Optional[ProductGender] = None,
    occasion: Optional[OccasionType] = None,
    fit_type: Optional[FitType] = None,
    season: Optional[SeasonType] = None,
    fabric: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    is_featured: Optional[bool] = None,
    is_trending: Optional[bool] = None,
    vendor_id: Optional[str] = None,
    sort_by: str = Query("newest", description="newest, price_asc, price_desc, rating, discount"),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    products, total = await ProductService.list_products(
        db,
        category_id=category_id,
        brand_id=brand_id,
        gender=gender,
        occasion=occasion,
        fit_type=fit_type,
        season=season,
        fabric=fabric,
        min_price=min_price,
        max_price=max_price,
        is_featured=is_featured,
        is_trending=is_trending,
        vendor_id=vendor_id,
        status=ProductStatus.PUBLISHED,
        sort_by=sort_by,
        page=page,
        limit=limit
    )

    items = []
    for p in products:
        primary_img = next((img.image_url for img in p.images if img.is_primary), None)
        if not primary_img and p.images:
            primary_img = p.images[0].image_url

        colors = list(dict.fromkeys([v.color_name for v in p.variants if v.is_active]))
        sizes = list(dict.fromkeys([v.size for v in p.variants if v.is_active]))

        items.append({
            "id": p.id,
            "vendor_id": p.vendor_id,
            "brand_id": p.brand_id,
            "category_id": p.category_id,
            "title": p.title,
            "slug": p.slug,
            "base_mrp": p.base_mrp,
            "base_price": p.base_price,
            "discount_percentage": p.discount_percentage,
            "gender": p.gender,
            "fabric": p.fabric,
            "fit_type": p.fit_type,
            "pattern": p.pattern,
            "occasion": p.occasion,
            "season": p.season,
            "status": p.status,
            "is_featured": p.is_featured,
            "is_trending": p.is_trending,
            "average_rating": p.average_rating,
            "review_count": p.review_count,
            "primary_image": primary_img,
            "colors": colors,
            "sizes": sizes,
            "created_at": p.created_at
        })

    return {
        "items": items,
        "total": total,
        "page": page,
        "limit": limit,
        "pages": (total + limit - 1) // limit
    }


@router.get("/products/{identifier}", response_model=ProductOut)
async def get_product(identifier: str, db: AsyncSession = Depends(get_db)):
    if len(identifier) == 36 and "-" in identifier:
        return await ProductService.get_by_id(db, identifier)
    return await ProductService.get_by_slug(db, identifier)


@router.post(
    "/products",
    response_model=ProductOut,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.VENDOR_OWNER]))]
)
async def create_product(
    prod_in: ProductCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    vendor_id = prod_in.vendor_id or current_user.id
    return await ProductService.create_product(db, vendor_id, prod_in)


@router.put(
    "/products/{product_id}",
    response_model=ProductOut,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.VENDOR_OWNER]))]
)
async def update_product(
    product_id: str,
    prod_in: ProductUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    vendor_id = None if current_user.role in (UserRole.SUPER_ADMIN, UserRole.ADMIN) else current_user.id
    return await ProductService.update_product(db, product_id, prod_in, vendor_id=vendor_id)


@router.post(
    "/products/{product_id}/variants",
    response_model=ProductVariantOut,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.VENDOR_OWNER]))]
)
async def add_product_variant(
    product_id: str,
    var_in: ProductVariantCreate,
    db: AsyncSession = Depends(get_db)
):
    return await ProductService.add_variant(db, product_id, var_in)


@router.post(
    "/products/{product_id}/images",
    response_model=ProductImageOut,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.VENDOR_OWNER]))]
)
async def add_product_image(
    product_id: str,
    img_in: ProductImageCreate,
    db: AsyncSession = Depends(get_db)
):
    return await ProductService.add_image(db, product_id, img_in)


@router.post("/products/{product_id}/size-advisor", response_model=SizeAdvisorResponse)
async def get_size_recommendation(
    product_id: str,
    req: SizeAdvisorRequest,
    db: AsyncSession = Depends(get_db)
):
    """Fashion Size & Fit Intelligence API"""
    return await ProductService.recommend_size(db, product_id, req)
