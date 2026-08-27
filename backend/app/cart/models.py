from typing import List, Optional
from sqlalchemy import String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import BaseModel


class Cart(BaseModel):
    __tablename__ = "carts"

    user_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=True, index=True)
    session_id: Mapped[Optional[str]] = mapped_column(String(100), unique=True, nullable=True, index=True) # Guest cart

    # Relationships
    items: Mapped[List["CartItem"]] = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")


class CartItem(BaseModel):
    __tablename__ = "cart_items"

    cart_id: Mapped[str] = mapped_column(String(36), ForeignKey("carts.id", ondelete="CASCADE"), nullable=False, index=True)
    product_id: Mapped[str] = mapped_column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    variant_id: Mapped[str] = mapped_column(String(36), ForeignKey("product_variants.id", ondelete="CASCADE"), nullable=False, index=True)
    quantity: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    selected_size: Mapped[str] = mapped_column(String(30), nullable=False)
    selected_color: Mapped[str] = mapped_column(String(50), nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)

    cart: Mapped["Cart"] = relationship("Cart", back_populates="items")
