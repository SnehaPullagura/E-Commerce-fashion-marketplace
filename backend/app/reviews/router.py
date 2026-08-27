from fastapi import APIRouter, Depends, Query, Body, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import User
from app.authentication.dependencies import get_current_user
from app.reviews.schemas import ReviewOut, ReviewCreate, ReviewSummaryOut
from app.reviews.service import ReviewService

router = APIRouter(prefix="/reviews", tags=["Customer Reviews & Fit Ratings"])


@router.post("", response_model=ReviewOut, status_code=status.HTTP_201_CREATED)
async def create_review(
    review_in: ReviewCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await ReviewService.create_review(db, current_user, review_in)


@router.get("/product/{product_id}")
async def list_product_reviews(
    product_id: str,
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=50),
    db: AsyncSession = Depends(get_db)
):
    reviews, total = await ReviewService.list_product_reviews(db, product_id, page, limit)
    return {
        "items": [ReviewOut.model_validate(r) for r in reviews],
        "total": total,
        "page": page,
        "limit": limit
    }


@router.get("/product/{product_id}/summary", response_model=ReviewSummaryOut)
async def get_product_review_summary(
    product_id: str,
    db: AsyncSession = Depends(get_db)
):
    return await ReviewService.get_summary(db, product_id)


@router.post("/reviews/{review_id}/vote")
async def vote_review(
    review_id: str,
    is_helpful: bool = Body(True, embed=True),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    await ReviewService.vote_helpful(db, review_id, current_user.id, is_helpful)
    return {"success": True, "message": "Vote recorded"}
