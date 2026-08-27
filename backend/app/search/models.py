from typing import List, Optional
from sqlalchemy import String, Boolean, Integer, JSON, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import BaseModel


class FashionCollection(BaseModel):
    """Curated Fashion Collections (e.g., Monsoon Edit, Wedding Edit, Office Essentials, Minimalist Streetwear)"""
    __tablename__ = "fashion_collections"

    title: Mapped[str] = mapped_column(String(150), unique=True, index=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(160), unique=True, index=True, nullable=False)
    tagline: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    banner_image_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    season: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    occasion: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, index=True)
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    style_tags: Mapped[List[str]] = mapped_column(JSON, default=list, nullable=False)

    # Relationships
    items: Mapped[List["CollectionProduct"]] = relationship("CollectionProduct", back_populates="collection", cascade="all, delete-orphan")


class CollectionProduct(BaseModel):
    __tablename__ = "collection_products"

    collection_id: Mapped[str] = mapped_column(String(36), ForeignKey("fashion_collections.id", ondelete="CASCADE"), nullable=False, index=True)
    product_id: Mapped[str] = mapped_column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    collection: Mapped["FashionCollection"] = relationship("FashionCollection", back_populates="items")


class SearchEvent(BaseModel):
    """Tracks search behavior and trending searches"""
    __tablename__ = "search_events"

    query_text: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    normalized_query: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    user_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    result_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    filters_applied: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
