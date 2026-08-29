from typing import Optional, Dict, Any, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.orm import selectinload

from app.core.config import settings
from app.core.exceptions import NotFoundException, BadRequestException
from app.products.models import Product, ProductVariant, ProductImage, Brand
from app.cart.models import Cart, CartItem
from app.cart.schemas import CartItemAdd, CartOut, CartItemOut, VendorCartGroup


class CartService:
    @staticmethod
    async def get_or_create_cart(
        db: AsyncSession, user_id: Optional[str] = None, session_id: Optional[str] = None
    ) -> Cart:
        if not user_id and not session_id:
            raise BadRequestException("Either user_id or session_id must be provided")

        stmt = select(Cart).options(selectinload(Cart.items))
        if user_id:
            stmt = stmt.where(Cart.user_id == user_id)
        else:
            stmt = stmt.where(Cart.session_id == session_id)

        res = await db.execute(stmt)
        cart = res.scalar_one_or_none()

        if cart:
            await db.refresh(cart, ["items"])
        else:
            cart = Cart(user_id=user_id, session_id=session_id)
            db.add(cart)
            await db.commit()
            stmt_reload = select(Cart).options(selectinload(Cart.items)).where(Cart.id == cart.id)
            res_reload = await db.execute(stmt_reload)
            cart = res_reload.scalar_one()

        return cart

    @staticmethod
    async def merge_guest_cart(db: AsyncSession, session_id: str, user_id: str) -> Cart:
        guest_cart_stmt = select(Cart).options(selectinload(Cart.items)).where(Cart.session_id == session_id)
        res_guest = await db.execute(guest_cart_stmt)
        guest_cart = res_guest.scalar_one_or_none()

        user_cart = await CartService.get_or_create_cart(db, user_id=user_id)

        if guest_cart and guest_cart.items:
            for g_item in guest_cart.items:
                # Check if item variant already in user cart
                existing = next((item for item in user_cart.items if item.variant_id == g_item.variant_id), None)
                if existing:
                    existing.quantity += g_item.quantity
                else:
                    new_item = CartItem(
                        cart_id=user_cart.id,
                        product_id=g_item.product_id,
                        variant_id=g_item.variant_id,
                        quantity=g_item.quantity,
                        selected_size=g_item.selected_size,
                        selected_color=g_item.selected_color,
                        unit_price=g_item.unit_price
                    )
                    db.add(new_item)

            # Delete guest cart
            await db.delete(guest_cart)
            await db.commit()

        return await CartService.get_or_create_cart(db, user_id=user_id)

    @staticmethod
    async def add_item(db: AsyncSession, cart: Cart, item_in: CartItemAdd) -> Cart:
        # Validate variant and product
        var_stmt = (
            select(ProductVariant)
            .options(selectinload(ProductVariant.product))
            .where(ProductVariant.id == item_in.variant_id, ProductVariant.is_active == True)
        )
        res = await db.execute(var_stmt)
        variant = res.scalar_one_or_none()
        if not variant:
            raise NotFoundException("Product variant not found or inactive")

        MAX_ITEM_LIMIT = 20

        if item_in.quantity <= 0:
            raise BadRequestException("Item quantity must be greater than zero")
        if item_in.quantity > MAX_ITEM_LIMIT:
            raise BadRequestException(f"Maximum quantity allowed per item is {MAX_ITEM_LIMIT} units")

        # Check existing item in cart
        existing_item = next((item for item in cart.items if item.variant_id == item_in.variant_id), None)
        if existing_item:
            if existing_item.quantity + item_in.quantity > MAX_ITEM_LIMIT:
                raise BadRequestException(f"Total quantity for this item in cart cannot exceed {MAX_ITEM_LIMIT} units")
            existing_item.quantity += item_in.quantity
            existing_item.unit_price = variant.price
        else:
            new_item = CartItem(
                cart_id=cart.id,
                product_id=variant.product_id,
                variant_id=variant.id,
                quantity=item_in.quantity,
                selected_size=variant.size,
                selected_color=variant.color_name,
                unit_price=variant.price
            )
            db.add(new_item)

        await db.commit()
        return await CartService.get_or_create_cart(db, user_id=cart.user_id, session_id=cart.session_id)

    @staticmethod
    async def update_quantity(db: AsyncSession, cart: Cart, item_id: str, quantity: int) -> Cart:
        item = next((i for i in cart.items if i.id == item_id), None)
        if not item:
            raise NotFoundException("Cart item not found")

        if quantity <= 0:
            await db.delete(item)
        elif quantity > 20:
            raise BadRequestException("Maximum quantity allowed per item is 20 units")
        else:
            item.quantity = quantity

        await db.commit()
        return await CartService.get_or_create_cart(db, user_id=cart.user_id, session_id=cart.session_id)

    @staticmethod
    async def remove_item(db: AsyncSession, cart: Cart, item_id: str) -> Cart:
        item = next((i for i in cart.items if i.id == item_id), None)
        if not item:
            raise NotFoundException("Cart item not found")

        await db.delete(item)
        await db.commit()
        return await CartService.get_or_create_cart(db, user_id=cart.user_id, session_id=cart.session_id)

    @staticmethod
    async def clear_cart(db: AsyncSession, cart: Cart) -> None:
        for item in cart.items:
            await db.delete(item)
        await db.commit()

    @staticmethod
    async def get_formatted_cart(db: AsyncSession, cart: Cart) -> CartOut:
        items_out: List[CartItemOut] = []
        vendor_items_map: Dict[str, List[CartItemOut]] = {}

        subtotal = 0.0
        total_mrp = 0.0

        items_stmt = select(CartItem).where(CartItem.cart_id == cart.id)
        items_res = await db.execute(items_stmt)
        cart_items = list(items_res.scalars().all())

        for item in cart_items:
            # Fetch fresh product & variant details
            prod_stmt = (
                select(Product)
                .options(selectinload(Product.brand), selectinload(Product.images), selectinload(Product.variants))
                .where(Product.id == item.product_id)
            )
            res = await db.execute(prod_stmt)
            product = res.scalar_one_or_none()
            if not product:
                continue

            variant = next((v for v in product.variants if v.id == item.variant_id), None)
            mrp = variant.mrp if variant else product.base_mrp
            selling_price = variant.price if variant else product.base_price

            primary_img = next((img.image_url for img in product.images if img.is_primary), None)
            if not primary_img and product.images:
                primary_img = product.images[0].image_url

            item_sub = selling_price * item.quantity
            subtotal += item_sub
            total_mrp += (mrp * item.quantity)

            item_obj = CartItemOut(
                id=item.id,
                product_id=product.id,
                variant_id=item.variant_id,
                product_title=product.title,
                product_slug=product.slug,
                brand_name=product.brand.name if product.brand else None,
                vendor_id=product.vendor_id,
                image_url=primary_img,
                size=item.selected_size,
                color_name=item.selected_color,
                unit_price=selling_price,
                mrp=mrp,
                quantity=item.quantity,
                item_subtotal=item_sub,
                is_in_stock=variant.is_active if variant else False
            )
            items_out.append(item_obj)

            if product.vendor_id not in vendor_items_map:
                vendor_items_map[product.vendor_id] = []
            vendor_items_map[product.vendor_id].append(item_obj)

        # Build Vendor Groups
        vendor_groups: List[VendorCartGroup] = []
        for v_id, v_items in vendor_items_map.items():
            v_sub = sum(i.item_subtotal for i in v_items)
            v_ship = 0.0 if v_sub >= settings.FREE_SHIPPING_THRESHOLD or not v_items else settings.DEFAULT_SHIPPING_FEE
            vendor_groups.append(
                VendorCartGroup(
                    vendor_id=v_id,
                    vendor_name=f"Vendor #{v_id[:8]}",
                    items=v_items,
                    vendor_subtotal=v_sub,
                    shipping_fee=v_ship
                )
            )

        total_shipping = sum(vg.shipping_fee for vg in vendor_groups)
        discount = max(0.0, total_mrp - subtotal)

        return CartOut(
            id=cart.id,
            user_id=cart.user_id,
            session_id=cart.session_id,
            items_count=sum(i.quantity for i in items_out),
            items=items_out,
            vendor_groups=vendor_groups,
            subtotal=round(subtotal, 2),
            total_mrp=round(total_mrp, 2),
            discount_amount=round(discount, 2),
            shipping_fee=round(total_shipping, 2),
            estimated_total=round(subtotal + total_shipping, 2),
            coupon_applied=None,
            coupon_discount=0.0
        )
