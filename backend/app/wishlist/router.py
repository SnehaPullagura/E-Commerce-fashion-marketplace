from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import User
from app.authentication.dependencies import get_current_user
from app.wishlist.schemas import WishlistOut, WishlistItemAdd
from app.wishlist.service import WishlistService

router = APIRouter(prefix="/wishlist", tags=["Wishlist"])


@router.get("", response_model=WishlistOut)
async def get_my_wishlist(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await WishlistService.get_formatted_wishlist(db, current_user.id)


@router.post("/items", response_model=WishlistOut)
async def add_item_to_wishlist(
    item_in: WishlistItemAdd,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    await WishlistService.add_item(db, current_user.id, item_in)
    return await WishlistService.get_formatted_wishlist(db, current_user.id)


@router.delete("/items/{product_id}", response_model=WishlistOut)
async def remove_item_from_wishlist(
    product_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    await WishlistService.remove_item(db, current_user.id, product_id)
    return await WishlistService.get_formatted_wishlist(db, current_user.id)


@router.post("/items/{product_id}/move-to-cart")
async def move_wishlist_item_to_cart(
    product_id: str,
    variant_id: str = Body(..., embed=True),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    await WishlistService.move_to_cart(db, current_user.id, product_id, variant_id)
    return {"success": True, "message": "Moved to cart successfully"}
