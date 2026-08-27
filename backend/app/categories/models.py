from typing import List, Optional
from sqlalchemy import String, Boolean, Float, Integer, JSON, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(120), unique=True, index=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    parent_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("categories.id", ondelete="SET NULL"), nullable=True, index=True)
    level: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    image_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    banner_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    icon_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, index=True)
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    commission_rate: Mapped[float] = mapped_column(Float, default=15.0, nullable=False)

    # Relationships
    parent: Mapped[Optional["Category"]] = relationship("Category", remote_side="Category.id", back_populates="subcategories")
    subcategories: Mapped[List["Category"]] = relationship("Category", back_populates="parent", cascade="all")
    attributes: Mapped[List["CategoryAttribute"]] = relationship("CategoryAttribute", back_populates="category", cascade="all, delete-orphan")


class CategoryAttribute(BaseModel):
    __tablename__ = "category_attributes"

    category_id: Mapped[str] = mapped_column(String(36), ForeignKey("categories.id", ondelete="CASCADE"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False) # e.g., "Fabric", "Fit", "Neckline", "Sleeve Length"
    attribute_type: Mapped[str] = mapped_column(String(50), default="MULTI_SELECT", nullable=False) # MULTI_SELECT, SINGLE_SELECT, TEXT, RANGE
    is_required: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_filterable: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    allowed_values: Mapped[List[str]] = mapped_column(JSON, default=list, nullable=False) # e.g. ["Cotton", "Linen", "Silk", "Denim"]

    category: Mapped["Category"] = relationship("Category", back_populates="attributes")
