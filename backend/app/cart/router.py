from typing import Optional
from fastapi import APIRouter, Depends, Header, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import User
from app.authentication.dependencies import get_current_user_optional, get_current_user
from app.cart.schemas import CartOut, CartItemAdd, CartItemUpdate
from app.cart.service import CartService

router = APIRouter(prefix="/cart", tags=["Shopping Cart"])


async def resolve_cart(
    current_user: Optional[User] = Depends(get_current_user_optional),
    x_session_id: Optional[str] = Header(None, alias="X-Session-ID"),
    db: AsyncSession = Depends(get_db)
):
    user_id = current_user.id if current_user else None
    session_id = x_session_id if not user_id else None
    if not user_id and not session_id:
        session_id = "guest_default_session"
    return await CartService.get_or_create_cart(db, user_id=user_id, session_id=session_id)


@router.get("", response_model=CartOut)
async def get_cart(
    cart = Depends(resolve_cart),
    db: AsyncSession = Depends(get_db)
):
    return await CartService.get_formatted_cart(db, cart)


@router.post("/items", response_model=CartOut)
async def add_item_to_cart(
    item_in: CartItemAdd,
    cart = Depends(resolve_cart),
    db: AsyncSession = Depends(get_db)
):
    updated_cart = await CartService.add_item(db, cart, item_in)
    return await CartService.get_formatted_cart(db, updated_cart)


@router.put("/items/{item_id}", response_model=CartOut)
async def update_item_quantity(
    item_id: str,
    item_in: CartItemUpdate,
    cart = Depends(resolve_cart),
    db: AsyncSession = Depends(get_db)
):
    updated_cart = await CartService.update_quantity(db, cart, item_id, item_in.quantity)
    return await CartService.get_formatted_cart(db, updated_cart)


@router.delete("/items/{item_id}", response_model=CartOut)
async def remove_item_from_cart(
    item_id: str,
    cart = Depends(resolve_cart),
    db: AsyncSession = Depends(get_db)
):
    updated_cart = await CartService.remove_item(db, cart, item_id)
    return await CartService.get_formatted_cart(db, updated_cart)


@router.delete("")
async def clear_cart(
    cart = Depends(resolve_cart),
    db: AsyncSession = Depends(get_db)
):
    await CartService.clear_cart(db, cart)
    return {"success": True, "message": "Cart cleared successfully"}


@router.post("/merge", response_model=CartOut)
async def merge_guest_cart(
    x_session_id: str = Header(..., alias="X-Session-ID"),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    merged_cart = await CartService.merge_guest_cart(db, x_session_id, current_user.id)
    return await CartService.get_formatted_cart(db, merged_cart)
