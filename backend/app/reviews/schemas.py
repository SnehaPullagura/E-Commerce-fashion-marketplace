from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from app.reviews.models import FitFeedback


class ReviewImageOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    image_url: str
    display_order: int


class ReviewCreate(BaseModel):
    product_id: str
    order_id: Optional[str] = None
    rating: int = Field(..., ge=1, le=5)
    title: str
    comment: str
    fit_feedback: FitFeedback = FitFeedback.TRUE_TO_SIZE
    quality_rating: int = Field(5, ge=1, le=5)
    images: List[str] = [] # list of image URLs


class ReviewOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    product_id: str
    user_id: str
    rating: int
    title: str
    comment: str
    fit_feedback: FitFeedback
    quality_rating: int
    is_verified_purchase: bool
    is_approved: bool
    helpful_votes: int
    vendor_response: Optional[str] = None
    created_at: datetime
    images: List[ReviewImageOut] = []


class ReviewSummaryOut(BaseModel):
    average_rating: float
    total_reviews: int
    rating_breakdown: dict # {"5": 40, "4": 10, ...}
    fit_feedback_breakdown: dict # {"RUNS_SMALL": 5, "TRUE_TO_SIZE": 40, "RUNS_LARGE": 2}
