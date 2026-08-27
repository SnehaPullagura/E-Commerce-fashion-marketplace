from typing import Optional, List, Dict, Any
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import User
from app.authentication.dependencies import get_current_user_optional
from app.recommendations.schemas import (
    CompleteTheLookResponse,
    PersonalizedFeedResponse,
)
from app.recommendations.service import RecommendationService

router = APIRouter(prefix="/recommendations", tags=["Fashion Intelligence & Recommendations"])


@router.get("/complete-the-look/{product_id}", response_model=CompleteTheLookResponse)
async def get_complete_the_look(
    product_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Complete-the-Look Outfit Engine API"""
    return await RecommendationService.get_complete_the_look(db, product_id)


@router.get("/personalized-feed", response_model=PersonalizedFeedResponse)
async def get_personalized_fashion_feed(
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """Fashion DNA Tailored Feed API"""
    user_id = current_user.id if current_user else None
    return await RecommendationService.get_personalized_feed(db, user_id=user_id)


@router.get("/similar/{product_id}")
async def get_similar_looks(
    product_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Similar Style Discovery API"""
    return await RecommendationService.get_similar_products(db, product_id)
