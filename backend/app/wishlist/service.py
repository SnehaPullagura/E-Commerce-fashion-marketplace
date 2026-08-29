from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload

from app.core.exceptions import NotFoundException, ConflictException, BadRequestException
from app.products.models import Product, ProductVariant
from app.cart.models import Cart, CartItem
from app.cart.service import CartService
from app.wishlist.models import Wishlist, WishlistItem
from app.wishlist.schemas import WishlistItemAdd, WishlistOut, WishlistItemOut


class WishlistService:
    @staticmethod
    async def get_or_create_wishlist(db: AsyncSession, user_id: str) -> Wishlist:
        stmt = select(Wishlist).options(selectinload(Wishlist.items)).where(Wishlist.user_id == user_id)
        res = await db.execute(stmt)
        wishlist = res.scalar_one_or_none()

        if not wishlist:
            wishlist = Wishlist(user_id=user_id, name="My Wishlist")
            db.add(wishlist)
            await db.commit()
            stmt_reload = select(Wishlist).options(selectinload(Wishlist.items)).where(Wishlist.id == wishlist.id)
            res_reload = await db.execute(stmt_reload)
            wishlist = res_reload.scalar_one()

        return wishlist

    @staticmethod
    async def add_item(db: AsyncSession, user_id: str, item_in: WishlistItemAdd) -> Wishlist:
        wishlist = await WishlistService.get_or_create_wishlist(db, user_id)

        # Check product
        prod_stmt = select(Product).where(Product.id == item_in.product_id)
        prod_res = await db.execute(prod_stmt)
        product = prod_res.scalar_one_or_none()
        if not product:
            raise NotFoundException("Product not found")

        # Check if already in wishlist
        existing = next((i for i in wishlist.items if i.product_id == item_in.product_id), None)
        if not existing:
            item = WishlistItem(
                wishlist_id=wishlist.id,
                product_id=product.id,
                desired_size=item_in.desired_size,
                desired_color=item_in.desired_color,
                price_when_added=product.base_price
            )
            db.add(item)
            await db.commit()

        return await WishlistService.get_or_create_wishlist(db, user_id)

    @staticmethod
    async def remove_item(db: AsyncSession, user_id: str, product_id: str) -> Wishlist:
        wishlist = await WishlistService.get_or_create_wishlist(db, user_id)
        item = next((i for i in wishlist.items if i.product_id == product_id), None)
        if item:
            await db.delete(item)
            await db.commit()
        return await WishlistService.get_or_create_wishlist(db, user_id)

    @staticmethod
    async def move_to_cart(db: AsyncSession, user_id: str, product_id: str, variant_id: str) -> None:
        cart = await CartService.get_or_create_cart(db, user_id=user_id)
        
        # Validate variant
        var_stmt = select(ProductVariant).where(ProductVariant.id == variant_id)
        var_res = await db.execute(var_stmt)
        variant = var_res.scalar_one_or_none()
        if not variant:
            raise NotFoundException("Variant not found")
        if not variant.is_active:
            raise BadRequestException("Selected variant is currently inactive or out of stock")

        # Check if item variant already in cart
        existing_item = next((item for item in cart.items if item.variant_id == variant_id), None)
        if existing_item:
            existing_item.quantity += 1
            existing_item.unit_price = variant.price
        else:
            cart_item = CartItem(
                cart_id=cart.id,
                product_id=variant.product_id,
                variant_id=variant.id,
                quantity=1,
                selected_size=variant.size,
                selected_color=variant.color_name,
                unit_price=variant.price
            )
            db.add(cart_item)

        # Remove from wishlist
        wishlist = await WishlistService.get_or_create_wishlist(db, user_id)
        w_item = next((i for i in wishlist.items if i.product_id == product_id), None)
        if w_item:
            await db.delete(w_item)

        await db.commit()

    @staticmethod
    async def get_formatted_wishlist(db: AsyncSession, user_id: str) -> WishlistOut:
        wishlist = await WishlistService.get_or_create_wishlist(db, user_id)
        items_out: List[WishlistItemOut] = []

        items_stmt = select(WishlistItem).where(WishlistItem.wishlist_id == wishlist.id)
        items_res = await db.execute(items_stmt)
        wishlist_items = list(items_res.scalars().all())

        for item in wishlist_items:
            prod_stmt = (
                select(Product)
                .options(selectinload(Product.brand), selectinload(Product.images))
                .where(Product.id == item.product_id)
            )
            res = await db.execute(prod_stmt)
            product = res.scalar_one_or_none()
            if not product:
                continue

            primary_img = next((img.image_url for img in product.images if img.is_primary), None)
            if not primary_img and product.images:
                primary_img = product.images[0].image_url

            has_dropped = product.base_price < item.price_when_added
            diff = round(item.price_when_added - product.base_price, 2) if has_dropped else 0.0

            items_out.append(
                WishlistItemOut(
                    id=item.id,
                    product_id=product.id,
                    product_title=product.title,
                    product_slug=product.slug,
                    brand_name=product.brand.name if product.brand else None,
                    image_url=primary_img,
                    current_price=product.base_price,
                    original_price_added=item.price_when_added,
                    has_price_dropped=has_dropped,
                    price_difference=diff,
                    desired_size=item.desired_size,
                    desired_color=item.desired_color,
                    created_at=item.created_at
                )
            )

        return WishlistOut(
            id=wishlist.id,
            user_id=wishlist.user_id,
            name=wishlist.name,
            is_public=wishlist.is_public,
            share_token=wishlist.share_token,
            items_count=len(items_out),
            items=items_out
        )
