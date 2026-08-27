from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import User, UserRole
from app.authentication.dependencies import get_current_user_optional, require_roles
from app.search.schemas import (
    SearchResponse,
    AutocompleteResponse,
    FashionCollectionOut,
    FashionCollectionCreate,
    FashionCollectionUpdate,
    AddProductsToCollection,
)
from app.search.service import SearchService

router = APIRouter(tags=["Fashion Search & Collections"])


@router.get("/search", response_model=SearchResponse)
async def search_fashion_catalog(
    q: str = Query(..., min_length=1, description="Fashion search query, e.g. 'black party dress' or 'linen shirt'"),
    category_id: Optional[str] = None,
    brand_id: Optional[str] = None,
    gender: Optional[str] = None,
    color: Optional[str] = None,
    size: Optional[str] = None,
    fit_type: Optional[str] = None,
    occasion: Optional[str] = None,
    fabric: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    sort_by: str = Query("relevance", description="relevance, price_asc, price_desc, rating, discount"),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    user_id = current_user.id if current_user else None
    return await SearchService.search(
        db=db,
        query=q,
        category_id=category_id,
        brand_id=brand_id,
        gender=gender,
        color=color,
        size=size,
        fit_type=fit_type,
        occasion=occasion,
        fabric=fabric,
        min_price=min_price,
        max_price=max_price,
        sort_by=sort_by,
        page=page,
        limit=limit,
        user_id=user_id
    )


@router.get("/search/autocomplete", response_model=AutocompleteResponse)
async def autocomplete(
    q: str = Query(..., min_length=1),
    db: AsyncSession = Depends(get_db)
):
    return await SearchService.get_autocomplete(db, q)


@router.get("/collections")
async def list_fashion_collections(db: AsyncSession = Depends(get_db)):
    cols = await SearchService.get_collections(db, only_active=True)
    return [
        {
            "id": c.id,
            "title": c.title,
            "slug": c.slug,
            "tagline": c.tagline,
            "description": c.description,
            "banner_image_url": c.banner_image_url,
            "season": c.season,
            "occasion": c.occasion,
            "is_featured": c.is_featured,
            "style_tags": c.style_tags,
            "created_at": c.created_at
        }
        for c in cols
    ]


@router.get("/collections/{slug}")
async def get_fashion_collection_details(slug: str, db: AsyncSession = Depends(get_db)):
    return await SearchService.get_collection_by_slug(db, slug)


@router.post(
    "/collections",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN]))]
)
async def create_fashion_collection(col_in: FashionCollectionCreate, db: AsyncSession = Depends(get_db)):
    return await SearchService.create_collection(db, col_in)


@router.post(
    "/collections/{collection_id}/products",
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN]))]
)
async def add_products_to_collection(
    collection_id: str,
    payload: AddProductsToCollection,
    db: AsyncSession = Depends(get_db)
):
    await SearchService.add_products_to_collection(db, collection_id, payload.product_ids)
    return {"success": True, "message": "Products added to collection successfully"}
