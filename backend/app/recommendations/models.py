import enum
from typing import Optional
from sqlalchemy import String, Float, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base_model import BaseModel


class RecommendationEventType(str, enum.Enum):
    VIEW = "VIEW"
    CLICK = "CLICK"
    ADD_TO_CART = "ADD_TO_CART"
    PURCHASE = "PURCHASE"


class ProductRecommendationLog(BaseModel):
    __tablename__ = "recommendation_logs"

    user_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    product_id: Mapped[str] = mapped_column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    recommended_product_id: Mapped[str] = mapped_column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    engine_type: Mapped[str] = mapped_column(String(50), default="COMPLETE_THE_LOOK", nullable=False) # COMPLETE_THE_LOOK, SIMILAR_LOOK, FASHION_DNA
    event_type: Mapped[RecommendationEventType] = mapped_column(SQLEnum(RecommendationEventType), default=RecommendationEventType.VIEW, nullable=False)
