from typing import List, Optional, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, func, or_, and_
from sqlalchemy.orm import selectinload

from app.core.exceptions import NotFoundException, ConflictException, ForbiddenException
from app.core.events import event_bus, EventType
from app.products.models import (
    Product,
    ProductVariant,
    ProductImage,
    Brand,
    BrandSizeChart,
    SizeChartMeasurement,
    ProductStatus,
    ProductGender,
    FitType,
    OccasionType,
    SeasonType,
)
from app.products.schemas import (
    ProductCreate,
    ProductUpdate,
    ProductVariantCreate,
    ProductImageCreate,
    BrandCreate,
    BrandUpdate,
    BrandSizeChartCreate,
    SizeAdvisorRequest,
    SizeAdvisorResponse,
    SizeMeasurementOut,
)


class ProductService:
    # --- Brand Operations ---
    @staticmethod
    async def create_brand(db: AsyncSession, brand_in: BrandCreate) -> Brand:
        stmt = select(Brand).where(Brand.slug == brand_in.slug.lower())
        res = await db.execute(stmt)
        if res.scalar_one_or_none():
            raise ConflictException(f"Brand with slug '{brand_in.slug}' already exists")

        brand = Brand(**brand_in.model_dump())
        db.add(brand)
        await db.commit()
        await db.refresh(brand)
        return brand

    @staticmethod
    async def get_all_brands(db: AsyncSession) -> List[Brand]:
        stmt = select(Brand).where(Brand.is_deleted == False).order_by(Brand.name.asc())
        res = await db.execute(stmt)
        return list(res.scalars().all())

    @staticmethod
    async def get_brand_by_id(db: AsyncSession, brand_id: str) -> Brand:
        stmt = select(Brand).where(Brand.id == brand_id, Brand.is_deleted == False)
        res = await db.execute(stmt)
        brand = res.scalar_one_or_none()
        if not brand:
            raise NotFoundException("Brand not found")
        return brand

    # --- Size Chart & Intelligence ---
    @staticmethod
    async def create_size_chart(db: AsyncSession, chart_in: BrandSizeChartCreate) -> BrandSizeChart:
        chart_dict = chart_in.model_dump(exclude={"measurements"})
        chart = BrandSizeChart(**chart_dict)
        db.add(chart)
        await db.flush()

        for m in chart_in.measurements:
            meas = SizeChartMeasurement(size_chart_id=chart.id, **m.model_dump())
            db.add(meas)

        await db.commit()
        stmt = (
            select(BrandSizeChart)
            .options(selectinload(BrandSizeChart.measurements))
            .where(BrandSizeChart.id == chart.id)
        )
        res = await db.execute(stmt)
        return res.scalar_one()

    @staticmethod
    async def recommend_size(
        db: AsyncSession, product_id: str, req: SizeAdvisorRequest
    ) -> SizeAdvisorResponse:
        product = await ProductService.get_by_id(db, product_id)
        size_chart = None

        if product.size_chart_id:
            stmt = (
                select(BrandSizeChart)
                .options(selectinload(BrandSizeChart.measurements))
                .where(BrandSizeChart.id == product.size_chart_id)
            )
            res = await db.execute(stmt)
            size_chart = res.scalar_one_or_none()

        if not size_chart or not size_chart.measurements:
            # Fallback heuristic using available variant sizes
            variants = product.variants
            sizes = [v.size for v in variants if v.is_active]
            recommended = "M" if "M" in sizes else (sizes[0] if sizes else "Standard")
            return SizeAdvisorResponse(
                recommended_size=recommended,
                confidence_score=0.75,
                fit_analysis=f"Estimated size {recommended} based on standard sizing proportions."
            )

        # Smart Size Matching Algorithm
        best_match_size = None
        best_score = 9999.0
        best_meas = None

        target_chest = req.chest_in
        target_waist = req.waist_in
        target_hips = req.hips_in

        for m in size_chart.measurements:
            score = 0.0
            points = 0

            if target_chest and m.chest_min and m.chest_max:
                mid_chest = (m.chest_min + m.chest_max) / 2.0
                score += abs(target_chest - mid_chest) * 1.5
                points += 1
            elif target_chest and m.chest_min:
                score += abs(target_chest - m.chest_min) * 1.5
                points += 1

            if target_waist and m.waist_min and m.waist_max:
                mid_waist = (m.waist_min + m.waist_max) / 2.0
                score += abs(target_waist - mid_waist) * 1.2
                points += 1

            if target_hips and m.hips_min and m.hips_max:
                mid_hips = (m.hips_min + m.hips_max) / 2.0
                score += abs(target_hips - mid_hips)
                points += 1

            if points > 0 and score < best_score:
                best_score = score
                best_match_size = m.size_label
                best_meas = m

        if not best_match_size:
            best_match_size = size_chart.measurements[0].size_label
            best_meas = size_chart.measurements[0]

        confidence = max(0.65, min(0.98, 1.0 - (best_score / 50.0)))
        fit_note = f"Size {best_match_size} matches your body measurements for a {product.fit_type.value.lower()} look."

        meas_out = SizeMeasurementOut.model_validate(best_meas) if best_meas else None

        return SizeAdvisorResponse(
            recommended_size=best_match_size,
            confidence_score=round(confidence, 2),
            fit_analysis=fit_note,
            size_measurements=meas_out
        )

    # --- Product Management ---
    @staticmethod
    async def create_product(db: AsyncSession, vendor_id: str, prod_in: ProductCreate) -> Product:
        stmt = select(Product).where(Product.slug == prod_in.slug.lower())
        res = await db.execute(stmt)
        if res.scalar_one_or_none():
            raise ConflictException(f"Product with slug '{prod_in.slug}' already exists")

        # Calculate discount percentage if not provided
        discount_pct = prod_in.discount_percentage
        if prod_in.base_mrp > prod_in.base_price and discount_pct == 0:
            discount_pct = round(((prod_in.base_mrp - prod_in.base_price) / prod_in.base_mrp) * 100, 1)

        prod_dict = prod_in.model_dump(exclude={"variants", "images", "vendor_id", "discount_percentage"})
        product = Product(
            vendor_id=vendor_id,
            discount_percentage=discount_pct,
            **prod_dict
        )
        db.add(product)
        await db.flush()

        # Add Variants
        for v in prod_in.variants:
            variant = ProductVariant(product_id=product.id, **v.model_dump())
            db.add(variant)

        # Add Images
        for img in prod_in.images:
            image = ProductImage(product_id=product.id, **img.model_dump())
            db.add(image)

        await db.commit()

        await event_bus.publish(
            EventType.PRODUCT_CREATED,
            {"product_id": product.id, "title": product.title, "vendor_id": vendor_id}
        )

        return await ProductService.get_by_id(db, product.id)

    @staticmethod
    async def get_by_id(db: AsyncSession, product_id: str) -> Product:
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
        product = res.scalar_one_or_none()
        if not product:
            raise NotFoundException("Product not found")
        return product

    @staticmethod
    async def get_by_slug(db: AsyncSession, slug: str) -> Product:
        stmt = (
            select(Product)
            .options(
                selectinload(Product.brand),
                selectinload(Product.variants),
                selectinload(Product.images)
            )
            .where(Product.slug == slug.lower(), Product.is_deleted == False)
        )
        res = await db.execute(stmt)
        product = res.scalar_one_or_none()
        if not product:
            raise NotFoundException(f"Product with slug '{slug}' not found")
        return product

    @staticmethod
    async def list_products(
        db: AsyncSession,
        category_id: Optional[str] = None,
        brand_id: Optional[str] = None,
        gender: Optional[ProductGender] = None,
        occasion: Optional[OccasionType] = None,
        fit_type: Optional[FitType] = None,
        season: Optional[SeasonType] = None,
        fabric: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        is_featured: Optional[bool] = None,
        is_trending: Optional[bool] = None,
        vendor_id: Optional[str] = None,
        status: Optional[ProductStatus] = ProductStatus.PUBLISHED,
        sort_by: str = "newest",
        page: int = 1,
        limit: int = 20
    ) -> Tuple[List[Product], int]:
        stmt = (
            select(Product)
            .options(
                selectinload(Product.brand),
                selectinload(Product.variants),
                selectinload(Product.images)
            )
            .where(Product.is_deleted == False)
        )

        if status:
            stmt = stmt.where(Product.status == status)
        if vendor_id:
            stmt = stmt.where(Product.vendor_id == vendor_id)
        if category_id:
            stmt = stmt.where(Product.category_id == category_id)
        if brand_id:
            stmt = stmt.where(Product.brand_id == brand_id)
        if gender:
            stmt = stmt.where(Product.gender == gender)
        if occasion:
            stmt = stmt.where(Product.occasion == occasion)
        if fit_type:
            stmt = stmt.where(Product.fit_type == fit_type)
        if season:
            stmt = stmt.where(Product.season == season)
        if fabric:
            stmt = stmt.where(Product.fabric.ilike(f"%{fabric}%"))
        if min_price is not None:
            stmt = stmt.where(Product.base_price >= min_price)
        if max_price is not None:
            stmt = stmt.where(Product.base_price <= max_price)
        if is_featured is not None:
            stmt = stmt.where(Product.is_featured == is_featured)
        if is_trending is not None:
            stmt = stmt.where(Product.is_trending == is_trending)

        # Count total
        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_res = await db.execute(count_stmt)
        total = total_res.scalar() or 0

        # Sorting
        if sort_by == "price_asc":
            stmt = stmt.order_by(Product.base_price.asc())
        elif sort_by == "price_desc":
            stmt = stmt.order_by(Product.base_price.desc())
        elif sort_by == "rating":
            stmt = stmt.order_by(Product.average_rating.desc())
        elif sort_by == "discount":
            stmt = stmt.order_by(Product.discount_percentage.desc())
        else: # newest
            stmt = stmt.order_by(Product.created_at.desc())

        # Pagination
        offset = (page - 1) * limit
        stmt = stmt.offset(offset).limit(limit)

        res = await db.execute(stmt)
        return list(res.scalars().all()), total

    @staticmethod
    async def update_product(
        db: AsyncSession, product_id: str, prod_in: ProductUpdate, vendor_id: Optional[str] = None
    ) -> Product:
        product = await ProductService.get_by_id(db, product_id)
        if vendor_id and product.vendor_id != vendor_id:
            raise ForbiddenException("You cannot edit another vendor's product")

        update_data = prod_in.model_dump(exclude_unset=True)
        for key, val in update_data.items():
            setattr(product, key, val)

        await db.commit()
        return await ProductService.get_by_id(db, product.id)

    @staticmethod
    async def add_variant(db: AsyncSession, product_id: str, var_in: ProductVariantCreate) -> ProductVariant:
        await ProductService.get_by_id(db, product_id)
        variant = ProductVariant(product_id=product_id, **var_in.model_dump())
        db.add(variant)
        await db.commit()
        await db.refresh(variant)
        return variant

    @staticmethod
    async def add_image(db: AsyncSession, product_id: str, img_in: ProductImageCreate) -> ProductImage:
        await ProductService.get_by_id(db, product_id)
        image = ProductImage(product_id=product_id, **img_in.model_dump())
        db.add(image)
        await db.commit()
        await db.refresh(image)
        return image
