from typing import List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_, and_, func
from sqlalchemy.orm import selectinload

from app.core.exceptions import NotFoundException
from app.users.models import User, UserStylePreference, UserSizeProfile
from app.products.models import (
    Product,
    ProductVariant,
    ProductImage,
    Brand,
    ProductStatus,
    ProductGender,
    FitType,
    OccasionType,
)
from app.categories.models import Category
from app.recommendations.models import ProductRecommendationLog, RecommendationEventType
from app.recommendations.schemas import (
    CompleteTheLookResponse,
    OutfitItem,
    PersonalizedFeedResponse,
    PersonalizedFeedItem,
)


class RecommendationService:
    @staticmethod
    async def get_complete_the_look(db: AsyncSession, product_id: str) -> CompleteTheLookResponse:
        stmt = (
            select(Product)
            .options(
                selectinload(Product.brand),
                selectinload(Product.variants),
                selectinload(Product.images)
            )
            .where(Product.id == product_id, Product.is_deleted == False)
        )
        res = await db.execute(stmt)
        main_prod = res.scalar_one_or_none()
        if not main_prod:
            raise NotFoundException("Product not found")

        # Determine main product role
        cat_stmt = select(Category).where(Category.id == main_prod.category_id)
        cat_res = await db.execute(cat_stmt)
        category = cat_res.scalar_one_or_none()
        cat_name = category.name.lower() if category else ""

        # Fetch candidate complementary products with matching gender & occasion
        comp_stmt = (
            select(Product)
            .options(
                selectinload(Product.brand),
                selectinload(Product.variants),
                selectinload(Product.images)
            )
            .where(
                Product.id != main_prod.id,
                Product.status == ProductStatus.PUBLISHED,
                or_(Product.gender == main_prod.gender, Product.gender == ProductGender.UNISEX),
                Product.is_deleted == False
            )
            .order_by(Product.average_rating.desc(), Product.created_at.desc())
            .limit(10)
        )
        comp_res = await db.execute(comp_stmt)
        candidates = list(comp_res.scalars().all())

        outfit_items: List[OutfitItem] = []

        # 1. Main Piece
        primary_img = next((img.image_url for img in main_prod.images if img.is_primary), None)
        if not primary_img and main_prod.images:
            primary_img = main_prod.images[0].image_url

        outfit_items.append(
            OutfitItem(
                id=main_prod.id,
                title=main_prod.title,
                slug=main_prod.slug,
                category_role="MAIN_PIECE",
                brand_name=main_prod.brand.name if main_prod.brand else None,
                price=main_prod.base_price,
                mrp=main_prod.base_mrp,
                discount_percentage=main_prod.discount_percentage,
                image_url=primary_img,
                fit_type=main_prod.fit_type.value,
                match_reason="Selected Core Piece"
            )
        )

        # 2. Complementary Pieces
        roles = ["BOTTOMWEAR", "FOOTWEAR", "ACCESSORY"]
        for idx, cand in enumerate(candidates[:3]):
            role = roles[idx % len(roles)]
            cand_img = next((img.image_url for img in cand.images if img.is_primary), None)
            if not cand_img and cand.images:
                cand_img = cand.images[0].image_url

            outfit_items.append(
                OutfitItem(
                    id=cand.id,
                    title=cand.title,
                    slug=cand.slug,
                    category_role=role,
                    brand_name=cand.brand.name if cand.brand else None,
                    price=cand.base_price,
                    mrp=cand.base_mrp,
                    discount_percentage=cand.discount_percentage,
                    image_url=cand_img,
                    fit_type=cand.fit_type.value,
                    match_reason=f"Pairs seamlessly with {main_prod.title[:25]} for a cohesive {main_prod.occasion.value.lower()} look."
                )
            )

        # Calculate bundle pricing
        bundle_mrp = sum(i.mrp for i in outfit_items)
        bundle_subtotal = sum(i.price for i in outfit_items)
        # Extra 10% bundle discount
        bundle_final_price = round(bundle_subtotal * 0.90, 2)
        bundle_savings = round(bundle_mrp - bundle_final_price, 2)

        return CompleteTheLookResponse(
            main_product_id=main_prod.id,
            main_product_title=main_prod.title,
            outfit_style_theme=f"{main_prod.fit_type.value.capitalize()} {main_prod.occasion.value.capitalize()} Aesthetic",
            occasion=main_prod.occasion.value,
            outfit_items=outfit_items,
            bundle_total_mrp=round(bundle_mrp, 2),
            bundle_discount_price=bundle_final_price,
            bundle_savings=bundle_savings,
            bundle_discount_percentage=10.0
        )

    @staticmethod
    async def get_personalized_feed(
        db: AsyncSession, user_id: Optional[str] = None
    ) -> PersonalizedFeedResponse:
        user_styles = []
        user_colors = []
        user_occasions = []
        preferred_size = None

        if user_id:
            stmt_user = (
                select(User)
                .options(selectinload(User.style_preference), selectinload(User.size_profile))
                .where(User.id == user_id)
            )
            res = await db.execute(stmt_user)
            user = res.scalar_one_or_none()
            if user and user.style_preference:
                user_styles = [s.lower() for s in user.style_preference.style_personas]
                user_colors = [c.lower() for c in user.style_preference.favorite_colors]
                user_occasions = [o.lower() for o in user.style_preference.occasion_interests]
            if user and user.size_profile:
                preferred_size = user.size_profile.preferred_top_size

        # Fetch published products
        prod_stmt = (
            select(Product)
            .options(
                selectinload(Product.brand),
                selectinload(Product.images),
                selectinload(Product.variants)
            )
            .where(Product.status == ProductStatus.PUBLISHED, Product.is_deleted == False)
            .limit(30)
        )
        prod_res = await db.execute(prod_stmt)
        products = list(prod_res.scalars().all())

        feed_items: List[PersonalizedFeedItem] = []

        for p in products:
            score = 70.0 # Base match
            match_tags = []

            # Match style tags
            p_tags = [t.lower() for t in p.style_tags]
            matched_styles = [s for s in user_styles if s in p_tags or s in p.title.lower()]
            if matched_styles:
                score += 15.0
                match_tags.append(f"Matches your '{matched_styles[0].capitalize()}' style")

            # Match color
            p_colors = [c.lower() for c in p.color_palette]
            for v in p.variants:
                p_colors.append(v.color_name.lower())
            matched_colors = [c for c in user_colors if any(c in pc for pc in p_colors)]
            if matched_colors:
                score += 10.0
                match_tags.append(f"Available in your favorite color: {matched_colors[0].capitalize()}")

            # Match occasion
            if p.occasion.value.lower() in user_occasions:
                score += 10.0
                match_tags.append(f"Perfect for {p.occasion.value.capitalize()} events")

            # Match size in stock
            if preferred_size:
                has_size = any(v.size == preferred_size and v.is_active for v in p.variants)
                if has_size:
                    score += 5.0
                    match_tags.append(f"Size {preferred_size} in stock")

            primary_img = next((img.image_url for img in p.images if img.is_primary), None)
            if not primary_img and p.images:
                primary_img = p.images[0].image_url

            final_score = min(98.5, score)

            feed_items.append(
                PersonalizedFeedItem(
                    product_id=p.id,
                    title=p.title,
                    slug=p.slug,
                    brand_name=p.brand.name if p.brand else None,
                    base_price=p.base_price,
                    base_mrp=p.base_mrp,
                    discount_percentage=p.discount_percentage,
                    primary_image=primary_img,
                    fit_type=p.fit_type.value,
                    occasion=p.occasion.value,
                    fabric=p.fabric,
                    fashion_dna_match_score=round(final_score, 1),
                    match_tags=match_tags or ["Curated trending fashion pick"]
                )
            )

        feed_items.sort(key=lambda x: x.fashion_dna_match_score, reverse=True)

        return PersonalizedFeedResponse(
            fashion_persona=user_styles or ["Contemporary", "Chic"],
            preferred_occasions=user_occasions or ["Casual", "Party", "Office"],
            items=feed_items,
            total=len(feed_items)
        )

    @staticmethod
    async def get_similar_products(db: AsyncSession, product_id: str) -> List[Dict[str, Any]]:
        target_prod = await db.get(Product, product_id)
        if not target_prod:
            raise NotFoundException("Product not found")

        stmt = (
            select(Product)
            .options(selectinload(Product.brand), selectinload(Product.images), selectinload(Product.variants))
            .where(
                Product.id != product_id,
                Product.category_id == target_prod.category_id,
                Product.status == ProductStatus.PUBLISHED,
                Product.is_deleted == False
            )
            .limit(6)
        )
        res = await db.execute(stmt)
        products = list(res.scalars().all())

        results = []
        for p in products:
            primary_img = next((img.image_url for img in p.images if img.is_primary), None)
            if not primary_img and p.images:
                primary_img = p.images[0].image_url

            results.append({
                "id": p.id,
                "title": p.title,
                "slug": p.slug,
                "brand_name": p.brand.name if p.brand else None,
                "base_mrp": p.base_mrp,
                "base_price": p.base_price,
                "discount_percentage": p.discount_percentage,
                "primary_image": primary_img,
                "fit_type": p.fit_type.value,
                "occasion": p.occasion.value,
                "fabric": p.fabric
            })
        return results
