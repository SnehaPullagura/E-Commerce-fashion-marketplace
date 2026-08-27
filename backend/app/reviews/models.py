import enum
from typing import List, Optional
from sqlalchemy import (
    String, Boolean, Integer, Float, ForeignKey, Enum as SQLEnum, Text
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import BaseModel


class FitFeedback(str, enum.Enum):
    RUNS_SMALL = "RUNS_SMALL"
    TRUE_TO_SIZE = "TRUE_TO_SIZE"
    RUNS_LARGE = "RUNS_LARGE"


class Review(BaseModel):
    __tablename__ = "reviews"

    product_id: Mapped[str] = mapped_column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    order_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)

    rating: Mapped[int] = mapped_column(Integer, nullable=False) # 1 to 5
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    fit_feedback: Mapped[FitFeedback] = mapped_column(SQLEnum(FitFeedback), default=FitFeedback.TRUE_TO_SIZE, nullable=False)
    quality_rating: Mapped[int] = mapped_column(Integer, default=5, nullable=False) # 1 to 5

    is_verified_purchase: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_approved: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, index=True)
    helpful_votes: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    vendor_response: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Relationships
    images: Mapped[List["ReviewImage"]] = relationship("ReviewImage", back_populates="review", cascade="all, delete-orphan")
    votes: Mapped[List["ReviewVote"]] = relationship("ReviewVote", back_populates="review", cascade="all, delete-orphan")


class ReviewImage(BaseModel):
    __tablename__ = "review_images"

    review_id: Mapped[str] = mapped_column(String(36), ForeignKey("reviews.id", ondelete="CASCADE"), nullable=False, index=True)
    image_url: Mapped[str] = mapped_column(String(500), nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    review: Mapped["Review"] = relationship("Review", back_populates="images")


class ReviewVote(BaseModel):
    __tablename__ = "review_votes"

    review_id: Mapped[str] = mapped_column(String(36), ForeignKey("reviews.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    is_helpful: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    review: Mapped["Review"] = relationship("Review", back_populates="votes")
