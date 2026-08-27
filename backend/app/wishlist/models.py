from typing import List, Optional
from sqlalchemy import String, Float, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import BaseModel


class Wishlist(BaseModel):
    __tablename__ = "wishlists"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(100), default="My Wishlist", nullable=False)
    is_public: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    share_token: Mapped[Optional[str]] = mapped_column(String(100), unique=True, nullable=True)

    items: Mapped[List["WishlistItem"]] = relationship("WishlistItem", back_populates="wishlist", cascade="all, delete-orphan")


class WishlistItem(BaseModel):
    __tablename__ = "wishlist_items"

    wishlist_id: Mapped[str] = mapped_column(String(36), ForeignKey("wishlists.id", ondelete="CASCADE"), nullable=False, index=True)
    product_id: Mapped[str] = mapped_column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    desired_size: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    desired_color: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    price_when_added: Mapped[float] = mapped_column(Float, nullable=False)
    price_drop_notified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    wishlist: Mapped["Wishlist"] = relationship("Wishlist", back_populates="items")
