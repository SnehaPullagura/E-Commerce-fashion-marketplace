import re
from typing import List, Dict, Any, Optional, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_, and_, func, distinct
from sqlalchemy.orm import selectinload

from app.core.exceptions import NotFoundException, ConflictException
from app.products.models import (
    Product,
    ProductVariant,
    ProductImage,
    Brand,
    ProductStatus,
    ProductGender,
    FitType,
    OccasionType,
    SeasonType,
)
from app.categories.models import Category
from app.search.models import FashionCollection, CollectionProduct, SearchEvent
from app.search.schemas import (
    ExtractedFashionTokens,
    SearchResponse,
    FacetsResponse,
    FacetBucket,
    AutocompleteResponse,
    AutocompleteItem,
    FashionCollectionCreate,
    FashionCollectionUpdate,
)

# Known Fashion Vocabulary
KNOWN_COLORS = {
    "black", "white", "blue", "red", "green", "yellow", "pink", "beige",
    "navy", "olive", "maroon", "grey", "gray", "charcoal", "rust", "brown",
    "cream", "gold", "silver", "purple", "lavender", "mustard", "teal"
}

KNOWN_OCCASIONS = {
    "party": OccasionType.PARTY,
    "wedding": OccasionType.WEDDING,
    "formal": OccasionType.FORMAL,
    "office": OccasionType.OFFICE,
    "casual": OccasionType.CASUAL,
    "festival": OccasionType.FESTIVAL,
    "streetwear": OccasionType.STREETWEAR,
    "travel": OccasionType.TRAVEL,
    "sports": OccasionType.SPORTS,
    "lounge": OccasionType.LOUNGEWEAR
}

KNOWN_FITS = {
    "slim": FitType.SLIM,
    "oversized": FitType.OVERSIZED,
    "oversize": FitType.OVERSIZED,
    "regular": FitType.REGULAR,
    "relaxed": FitType.RELAXED,
    "tailored": FitType.TAILORED,
    "skinny": FitType.SKINNY
}

KNOWN_FABRICS = {
    "linen", "cotton", "silk", "denim", "georgette", "chiffon",
    "leather", "velvet", "wool", "satin", "rayon", "polyester", "khadi"
}

KNOWN_SEASONS = {
    "summer": SeasonType.SUMMER,
    "winter": SeasonType.WINTER,
    "monsoon": SeasonType.MONSOON,
    "spring": SeasonType.SPRING,
    "autumn": SeasonType.AUTUMN
}


class SearchService:
    @staticmethod
    def extract_fashion_tokens(query: str) -> ExtractedFashionTokens:
        words = re.findall(r"\b\w+\b", query.lower())
        detected_gender = None
        detected_color = None
        detected_fit = None
        detected_occasion = None
        detected_fabric = None
        detected_season = None
        remaining = []

        for word in words:
            if word in ("men", "mens", "male", "man"):
                detected_gender = "MEN"
            elif word in ("women", "womens", "female", "woman", "ladies"):
                detected_gender = "WOMEN"
            elif word in ("kids", "children", "boys", "girls"):
                detected_gender = "KIDS"
            elif word in KNOWN_COLORS and not detected_color:
                detected_color = word.capitalize()
            elif word in KNOWN_OCCASIONS and not detected_occasion:
                detected_occasion = KNOWN_OCCASIONS[word].value
            elif word in KNOWN_FITS and not detected_fit:
                detected_fit = KNOWN_FITS[word].value
            elif word in KNOWN_FABRICS and not detected_fabric:
                detected_fabric = word.capitalize()
            elif word in KNOWN_SEASONS and not detected_season:
                detected_season = KNOWN_SEASONS[word].value
            else:
                remaining.append(word)

        return ExtractedFashionTokens(
            query=query,
            detected_gender=detected_gender,
            detected_category=remaining[0].capitalize() if remaining else None,
            detected_color=detected_color,
            detected_fit=detected_fit,
            detected_occasion=detected_occasion,
            detected_fabric=detected_fabric,
            detected_season=detected_season,
            remaining_keywords=remaining
        )

    @staticmethod
    async def search(
        db: AsyncSession,
        query: str,
        category_id: Optional[str] = None,
        brand_id: Optional[str] = None,
        gender: Optional[str] = None,
        color: Optional[str] = None,
        size: Optional[str] = None,
        fit_type: Optional[str] = None,
        occasion: Optional[str] = None,
        fabric: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        sort_by: str = "relevance",
        page: int = 1,
        limit: int = 20,
        user_id: Optional[str] = None
    ) -> SearchResponse:
        tokens = SearchService.extract_fashion_tokens(query)

        stmt = (
            select(Product)
            .options(
                selectinload(Product.brand),
                selectinload(Product.variants),
                selectinload(Product.images)
            )
            .where(Product.is_deleted == False, Product.status == ProductStatus.PUBLISHED)
        )

        # Apply natural token filters if not explicitly provided
        active_gender = gender or tokens.detected_gender
        active_color = color or tokens.detected_color
        active_fit = fit_type or tokens.detected_fit
        active_occasion = occasion or tokens.detected_occasion
        active_fabric = fabric or tokens.detected_fabric

        # Text search against title, description, and style_tags
        if tokens.remaining_keywords:
            keyword_clauses = []
            for kw in tokens.remaining_keywords:
                keyword_clauses.append(Product.title.ilike(f"%{kw}%"))
                keyword_clauses.append(Product.description.ilike(f"%{kw}%"))
                keyword_clauses.append(Product.fabric.ilike(f"%{kw}%"))
            stmt = stmt.where(or_(*keyword_clauses))

        if active_gender:
            stmt = stmt.where(or_(Product.gender == active_gender, Product.gender == ProductGender.UNISEX))
        if active_fit:
            stmt = stmt.where(Product.fit_type == active_fit)
        if active_occasion:
            stmt = stmt.where(Product.occasion == active_occasion)
        if active_fabric:
            stmt = stmt.where(Product.fabric.ilike(f"%{active_fabric}%"))
        if category_id:
            stmt = stmt.where(Product.category_id == category_id)
        if brand_id:
            stmt = stmt.where(Product.brand_id == brand_id)
        if min_price is not None:
            stmt = stmt.where(Product.base_price >= min_price)
        if max_price is not None:
            stmt = stmt.where(Product.base_price <= max_price)

        # Variant-level filtering (Color, Size)
        if active_color or size:
            variant_subquery = select(ProductVariant.product_id).where(ProductVariant.is_active == True)
            if active_color:
                variant_subquery = variant_subquery.where(ProductVariant.color_name.ilike(f"%{active_color}%"))
            if size:
                variant_subquery = variant_subquery.where(ProductVariant.size == size)
            stmt = stmt.where(Product.id.in_(variant_subquery))

        # Count total
        count_stmt = select(func.count()).select_from(stmt.subquery())
        count_res = await db.execute(count_stmt)
        total = count_res.scalar() or 0

        # Sorting
        if sort_by == "price_asc":
            stmt = stmt.order_by(Product.base_price.asc())
        elif sort_by == "price_desc":
            stmt = stmt.order_by(Product.base_price.desc())
        elif sort_by == "rating":
            stmt = stmt.order_by(Product.average_rating.desc())
        elif sort_by == "discount":
            stmt = stmt.order_by(Product.discount_percentage.desc())
        else: # relevance / trending
            stmt = stmt.order_by(Product.is_featured.desc(), Product.is_trending.desc(), Product.average_rating.desc())

        # Pagination
        offset = (page - 1) * limit
        stmt = stmt.offset(offset).limit(limit)

        res = await db.execute(stmt)
        products = list(res.scalars().all())

        # Build items
        items = []
        for p in products:
            primary_img = next((img.image_url for img in p.images if img.is_primary), None)
            if not primary_img and p.images:
                primary_img = p.images[0].image_url

            colors = list(dict.fromkeys([v.color_name for v in p.variants if v.is_active]))
            sizes = list(dict.fromkeys([v.size for v in p.variants if v.is_active]))

            items.append({
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
                "fabric": p.fabric,
                "colors": colors,
                "sizes": sizes,
                "average_rating": p.average_rating,
                "review_count": p.review_count
            })

        # Record search event
        try:
            event = SearchEvent(
                query_text=query,
                normalized_query=" ".join(tokens.remaining_keywords),
                user_id=user_id,
                result_count=total,
                filters_applied={
                    "gender": active_gender,
                    "color": active_color,
                    "fit": active_fit,
                    "occasion": active_occasion
                }
            )
            db.add(event)
            await db.commit()
        except Exception:
            pass

        return SearchResponse(
            query=query,
            extracted_tokens=tokens,
            items=items,
            total=total,
            page=page,
            limit=limit
        )

    @staticmethod
    async def get_autocomplete(db: AsyncSession, query: str) -> AutocompleteResponse:
        suggestions: List[AutocompleteItem] = []
        term = f"%{query.strip()}%"

        # 1. Matching Products
        prod_stmt = select(Product).where(Product.title.ilike(term), Product.status == ProductStatus.PUBLISHED).limit(3)
        prod_res = await db.execute(prod_stmt)
        for p in prod_res.scalars().all():
            suggestions.append(AutocompleteItem(title=p.title, type="PRODUCT", slug=p.slug))

        # 2. Matching Brands
        brand_stmt = select(Brand).where(Brand.name.ilike(term)).limit(2)
        brand_res = await db.execute(brand_stmt)
        for b in brand_res.scalars().all():
            suggestions.append(AutocompleteItem(title=b.name, type="BRAND", slug=b.slug, image_url=b.logo_url))

        # 3. Matching Categories
        cat_stmt = select(Category).where(Category.name.ilike(term), Category.is_active == True).limit(2)
        cat_res = await db.execute(cat_stmt)
        for c in cat_res.scalars().all():
            suggestions.append(AutocompleteItem(title=c.name, type="CATEGORY", slug=c.slug))

        trending = ["Minimalist linen shirt", "Black party dress", "Oversized graphic tee", "Wedding kurta set", "Chunky sneakers"]

        return AutocompleteResponse(suggestions=suggestions, trending_searches=trending)

    # --- Curated Fashion Collections ---
    @staticmethod
    async def create_collection(db: AsyncSession, col_in: FashionCollectionCreate) -> FashionCollection:
        stmt = select(FashionCollection).where(FashionCollection.slug == col_in.slug.lower())
        res = await db.execute(stmt)
        if res.scalar_one_or_none():
            raise ConflictException(f"Collection with slug '{col_in.slug}' already exists")

        col = FashionCollection(**col_in.model_dump())
        db.add(col)
        await db.commit()
        await db.refresh(col)
        return col

    @staticmethod
    async def get_collections(db: AsyncSession, only_active: bool = True) -> List[FashionCollection]:
        stmt = select(FashionCollection).where(FashionCollection.is_deleted == False)
        if only_active:
            stmt = stmt.where(FashionCollection.is_active == True)
        stmt = stmt.order_by(FashionCollection.display_order.asc(), FashionCollection.created_at.desc())
        res = await db.execute(stmt)
        return list(res.scalars().all())

    @staticmethod
    async def get_collection_by_slug(db: AsyncSession, slug: str) -> Dict[str, Any]:
        stmt = (
            select(FashionCollection)
            .options(selectinload(FashionCollection.items))
            .where(FashionCollection.slug == slug.lower(), FashionCollection.is_deleted == False)
        )
        res = await db.execute(stmt)
        col = res.scalar_one_or_none()
        if not col:
            raise NotFoundException(f"Collection '{slug}' not found")

        # Fetch collection products
        prod_ids = [item.product_id for item in col.items]
        products = []
        if prod_ids:
            prod_stmt = (
                select(Product)
                .options(selectinload(Product.brand), selectinload(Product.variants), selectinload(Product.images))
                .where(Product.id.in_(prod_ids), Product.status == ProductStatus.PUBLISHED)
            )
            prod_res = await db.execute(prod_stmt)
            for p in prod_res.scalars().all():
                primary_img = next((img.image_url for img in p.images if img.is_primary), None)
                if not primary_img and p.images:
                    primary_img = p.images[0].image_url
                products.append({
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
                    "average_rating": p.average_rating,
                    "review_count": p.review_count
                })

        return {
            "id": col.id,
            "title": col.title,
            "slug": col.slug,
            "tagline": col.tagline,
            "description": col.description,
            "banner_image_url": col.banner_image_url,
            "season": col.season,
            "occasion": col.occasion,
            "is_active": col.is_active,
            "is_featured": col.is_featured,
            "style_tags": col.style_tags,
            "created_at": col.created_at,
            "products": products
        }

    @staticmethod
    async def add_products_to_collection(
        db: AsyncSession, collection_id: str, product_ids: List[str]
    ) -> bool:
        stmt = select(FashionCollection).where(FashionCollection.id == collection_id)
        res = await db.execute(stmt)
        if not res.scalar_one_or_none():
            raise NotFoundException("Collection not found")

        for idx, pid in enumerate(product_ids):
            item = CollectionProduct(collection_id=collection_id, product_id=pid, display_order=idx)
            db.add(item)
        await db.commit()
        return True
