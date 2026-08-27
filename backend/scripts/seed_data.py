import asyncio
import logging
from datetime import datetime, timedelta, timezone

from app.core.database import AsyncSessionLocal, init_db
from app.core.security import get_password_hash
from app.users.models import User, UserProfile, UserSizeProfile, UserStylePreference, UserAddress, UserRole, GenderPreference, FitPreference, AddressType
from app.categories.models import Category, CategoryAttribute
from app.products.models import Brand, BrandSizeChart, SizeChartMeasurement, Product, ProductVariant, ProductImage, ProductStatus, ProductGender, FitType, OccasionType, SeasonType
from app.inventory.models import InventoryItem, InventoryTransaction, InventoryTxType
from app.search.models import FashionCollection, CollectionProduct
from app.coupons.models import Coupon, DiscountType
from app.vendors.models import VendorProfile, VendorStatus

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("seed")


async def seed():
    logger.info("Initializing database schema...")
    await init_db()

    async with AsyncSessionLocal() as db:
        logger.info("Seeding Super Admin and Users...")
        # 1. Super Admin
        admin = User(
            email="admin@marketplace.com",
            hashed_password=get_password_hash("AdminPass123!"),
            first_name="Super",
            last_name="Admin",
            role=UserRole.SUPER_ADMIN,
            is_active=True,
            is_verified=True
        )
        db.add(admin)

        # 2. Vendor Owner User
        vendor_user = User(
            email="anita@anitadongre.com",
            hashed_password=get_password_hash("VendorPass123!"),
            first_name="Anita",
            last_name="Dongre",
            role=UserRole.VENDOR_OWNER,
            is_active=True,
            is_verified=True
        )
        db.add(vendor_user)

        # 3. Customer User
        customer = User(
            email="zara.customer@example.com",
            hashed_password=get_password_hash("CustomerPass123!"),
            first_name="Zara",
            last_name="Roy",
            role=UserRole.CUSTOMER,
            is_active=True,
            is_verified=True,
            gender_preference=GenderPreference.WOMEN
        )
        db.add(customer)
        await db.flush()

        # Customer Fashion DNA & Size Profile
        cust_profile = UserProfile(user_id=customer.id, bio="Fashion enthusiast and minimalist aesthetics lover.")
        cust_size = UserSizeProfile(
            user_id=customer.id,
            height_cm=168.0,
            weight_kg=56.0,
            chest_in=34.0,
            waist_in=28.0,
            hips_in=38.0,
            preferred_top_size="M",
            preferred_bottom_size="28",
            fit_preference=FitPreference.SLIM
        )
        cust_dna = UserStylePreference(
            user_id=customer.id,
            style_personas=["Minimalist", "Chic", "Contemporary"],
            favorite_colors=["Black", "Off-White", "Sage Green"],
            preferred_brands=["Noir Couture", "Anita Dongre"],
            preferred_categories=["Dresses", "Shirts", "Trousers"],
            occasion_interests=["Office", "Party", "Weekend Brunch"],
            price_sensitivity="PREMIUM"
        )
        cust_addr = UserAddress(
            user_id=customer.id,
            address_type=AddressType.HOME,
            full_name="Zara Roy",
            phone_number="+919876543210",
            street_address="Penthouse 12B, Sky High Towers, Indiranagar",
            city="Bengaluru",
            state="Karnataka",
            postal_code="560038",
            country="India",
            is_default=True
        )
        db.add_all([cust_profile, cust_size, cust_dna, cust_addr])

        # Vendor Profile
        vendor_prof = VendorProfile(
            user_id=vendor_user.id,
            business_name="Anita Dongre Couture",
            legal_name="House of Anita Dongre Ltd",
            slug="anita-dongre",
            gst_number="27AAACH7409R1ZZ",
            pan_number="AAACH7409R",
            city="Mumbai",
            state="Maharashtra",
            postal_code="400013",
            description="Sustainable luxury Indian wear and contemporary silhouettes.",
            status=VendorStatus.APPROVED,
            commission_rate=15.0,
            rating=4.9
        )
        db.add(vendor_prof)

        # 4. Brands
        logger.info("Seeding Brands...")
        b_noir = Brand(
            name="Noir Couture",
            slug="noir-couture",
            description="Minimalist luxury fashion and refined tailoring.",
            country_of_origin="India",
            is_verified=True,
            is_featured=True
        )
        b_anita = Brand(
            name="Anita Dongre",
            slug="anita-dongre",
            description="Handcrafted sustainable bridal, ethnic and festive couture.",
            country_of_origin="India",
            is_verified=True,
            is_featured=True
        )
        b_tokyo = Brand(
            name="Tokyo Raw",
            slug="tokyo-raw",
            description="Urban oversized heavyweight streetwear aesthetic.",
            country_of_origin="Japan",
            is_verified=True,
            is_featured=True
        )
        b_milano = Brand(
            name="Milano Sartorial",
            slug="milano-sartorial",
            description="Italian artisanal footwear and handcrafted leather goods.",
            country_of_origin="Italy",
            is_verified=True,
            is_featured=True
        )
        db.add_all([b_noir, b_anita, b_tokyo, b_milano])
        await db.flush()

        # 5. Categories
        logger.info("Seeding Categories...")
        cat_women = Category(name="Women's Apparel", slug="womens-apparel", level=0, display_order=1)
        cat_men = Category(name="Men's Apparel", slug="mens-apparel", level=0, display_order=2)
        cat_footwear = Category(name="Footwear & Sneakers", slug="footwear", level=0, display_order=3)
        cat_acc = Category(name="Accessories & Jewellery", slug="accessories", level=0, display_order=4)
        db.add_all([cat_women, cat_men, cat_footwear, cat_acc])
        await db.flush()

        # Subcategories
        sub_dresses = Category(name="Designer Dresses", slug="dresses", parent_id=cat_women.id, level=1)
        sub_ethnic = Category(name="Ethnic & Festive Sets", slug="ethnic-sets", parent_id=cat_women.id, level=1)
        sub_shirts = Category(name="Sartorial Shirts", slug="mens-shirts", parent_id=cat_men.id, level=1)
        sub_streetwear = Category(name="Streetwear & Tees", slug="streetwear-tees", parent_id=cat_men.id, level=1)
        db.add_all([sub_dresses, sub_ethnic, sub_shirts, sub_streetwear])
        await db.flush()

        # 6. Brand Size Charts
        logger.info("Seeding Size Charts...")
        chart_tops = BrandSizeChart(
            brand_id=b_noir.id,
            category_id=sub_shirts.id,
            title="Noir Men Tops Size Guide",
            chart_type="TOPWEAR",
            unit="INCHES"
        )
        db.add(chart_tops)
        await db.flush()

        m_s = SizeChartMeasurement(size_chart_id=chart_tops.id, size_label="S", chest_min=36.0, chest_max=38.0, waist_min=30.0, waist_max=32.0)
        m_m = SizeChartMeasurement(size_chart_id=chart_tops.id, size_label="M", chest_min=38.0, chest_max=40.0, waist_min=32.0, waist_max=34.0)
        m_l = SizeChartMeasurement(size_chart_id=chart_tops.id, size_label="L", chest_min=40.0, chest_max=42.0, waist_min=34.0, waist_max=36.0)
        m_xl = SizeChartMeasurement(size_chart_id=chart_tops.id, size_label="XL", chest_min=42.0, chest_max=44.0, waist_min=36.0, waist_max=38.0)
        db.add_all([m_s, m_m, m_l, m_xl])

        # 7. Products & Variants
        logger.info("Seeding Products...")
        p1 = Product(
            vendor_id=vendor_user.id,
            brand_id=b_noir.id,
            category_id=sub_dresses.id,
            title="Black Velvet Bodycon Party Dress",
            slug="black-velvet-bodycon-party-dress",
            description="Stunning midnight black silk velvet bodycon dress featuring an asymmetrical neckline for luxury evening events.",
            base_mrp=4999.0,
            base_price=3499.0,
            discount_percentage=30.0,
            gender=ProductGender.WOMEN,
            fabric="Silk Velvet",
            fit_type=FitType.SLIM,
            occasion=OccasionType.PARTY,
            season=SeasonType.WINTER,
            care_instructions="Dry clean only",
            style_tags=["party", "glam", "velvet", "bodycon", "lbd"],
            color_palette=["Black"],
            status=ProductStatus.PUBLISHED,
            is_featured=True,
            is_trending=True,
            average_rating=4.9,
            review_count=38
        )
        db.add(p1)
        await db.flush()

        v1_s = ProductVariant(product_id=p1.id, sku="DRS-BLK-S", size="S", color_name="Midnight Black", color_hex="#111111", mrp=4999.0, price=3499.0)
        v1_m = ProductVariant(product_id=p1.id, sku="DRS-BLK-M", size="M", color_name="Midnight Black", color_hex="#111111", mrp=4999.0, price=3499.0)
        img1 = ProductImage(product_id=p1.id, image_url="https://images.unsplash.com/photo-1566174053879-31528523f8ae?auto=format&fit=crop&w=800&q=80", is_primary=True)
        db.add_all([v1_s, v1_m, img1])

        p2 = Product(
            vendor_id=vendor_user.id,
            brand_id=b_noir.id,
            category_id=sub_shirts.id,
            size_chart_id=chart_tops.id,
            title="Minimalist Linen Mandarin Collar Shirt",
            slug="minimalist-linen-mandarin-shirt",
            description="Breathable 100% pure organic linen shirt tailored with a band collar for smart-office and casual wear.",
            base_mrp=2999.0,
            base_price=1999.0,
            discount_percentage=33.3,
            gender=ProductGender.MEN,
            fabric="100% Pure Organic Linen",
            fit_type=FitType.SLIM,
            occasion=OccasionType.OFFICE,
            season=SeasonType.SUMMER,
            care_instructions="Machine wash cold, air dry",
            style_tags=["minimalist", "summer", "linen", "mandarin-collar", "office"],
            color_palette=["Off-White", "Sage Green"],
            status=ProductStatus.PUBLISHED,
            is_featured=True,
            is_trending=True,
            average_rating=4.8,
            review_count=54
        )
        db.add(p2)
        await db.flush()

        v2_m = ProductVariant(product_id=p2.id, sku="NOIR-LIN-WHT-M", size="M", color_name="Off-White", color_hex="#FAF9F6", mrp=2999.0, price=1999.0)
        v2_l = ProductVariant(product_id=p2.id, sku="NOIR-LIN-WHT-L", size="L", color_name="Off-White", color_hex="#FAF9F6", mrp=2999.0, price=1999.0)
        img2 = ProductImage(product_id=p2.id, image_url="https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80", is_primary=True)
        db.add_all([v2_m, v2_l, img2])

        p3 = Product(
            vendor_id=vendor_user.id,
            brand_id=b_anita.id,
            category_id=sub_ethnic.id,
            title="Handcrafted Zari Embroidered Silk Kurta Set",
            slug="silk-kurta-set",
            description="Luxurious mulberry silk kurta paired with tailored pants and a georgette dupatta.",
            base_mrp=11999.0,
            base_price=7999.0,
            discount_percentage=33.3,
            gender=ProductGender.WOMEN,
            fabric="Mulberry Silk",
            fit_type=FitType.REGULAR,
            occasion=OccasionType.WEDDING,
            season=SeasonType.ALL_SEASON,
            style_tags=["ethnic", "wedding", "festive", "zari", "designer"],
            color_palette=["Ruby Red", "Gold"],
            status=ProductStatus.PUBLISHED,
            is_featured=True,
            is_trending=True,
            average_rating=5.0,
            review_count=24
        )
        db.add(p3)
        await db.flush()

        v3_m = ProductVariant(product_id=p3.id, sku="ANITA-KURTA-M", size="M", color_name="Ruby Red", color_hex="#9B111E", mrp=11999.0, price=7999.0)
        img3 = ProductImage(product_id=p3.id, image_url="https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=800&q=80", is_primary=True)
        db.add_all([v3_m, img3])

        p4 = Product(
            vendor_id=vendor_user.id,
            brand_id=b_tokyo.id,
            category_id=sub_streetwear.id,
            title="Oversized Heavyweight Graphic Streetwear Tee",
            slug="oversized-graphic-tee",
            description="280 GSM heavyweight french terry cotton drop-shoulder streetwear graphic t-shirt.",
            base_mrp=1999.0,
            base_price=1299.0,
            discount_percentage=35.0,
            gender=ProductGender.UNISEX,
            fabric="280 GSM Cotton",
            fit_type=FitType.OVERSIZED,
            occasion=OccasionType.STREETWEAR,
            season=SeasonType.ALL_SEASON,
            style_tags=["streetwear", "oversized", "graphic-tee", "vintage"],
            color_palette=["Charcoal", "Sage Green"],
            status=ProductStatus.PUBLISHED,
            is_featured=True,
            is_trending=True,
            average_rating=4.7,
            review_count=82
        )
        db.add(p4)
        await db.flush()

        v4_l = ProductVariant(product_id=p4.id, sku="TOKYO-TEE-CHAR-L", size="L", color_name="Charcoal", color_hex="#36454F", mrp=1999.0, price=1299.0)
        img4 = ProductImage(product_id=p4.id, image_url="https://images.unsplash.com/photo-1552374196-1ab2a1c593e8?auto=format&fit=crop&w=800&q=80", is_primary=True)
        db.add_all([v4_l, img4])
        await db.flush()

        # 8. Initial Inventory
        logger.info("Initializing Inventory...")
        for v in [v1_s, v1_m, v2_m, v2_l, v3_m, v4_l]:
            inv = InventoryItem(
                variant_id=v.id,
                sku=v.sku,
                vendor_id=vendor_user.id,
                physical_stock=50,
                reserved_stock=0,
                warehouse_location="Mumbai Hub"
            )
            db.add(inv)

        # 9. Curated Collections
        logger.info("Seeding Curated Collections...")
        col_monsoon = FashionCollection(
            title="Monsoon Edit: Breathable Linens & Cottons",
            slug="monsoon-edit",
            tagline="Stay effortlessly fresh in lightweight organic weaves",
            description="Curated selection of pure linens, quick-dry silks, and breezy relaxed silhouettes.",
            banner_image_url="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?auto=format&fit=crop&w=1200&q=80",
            season="MONSOON",
            is_active=True,
            is_featured=True,
            display_order=1,
            style_tags=["monsoon", "linen", "breathable", "lightweight"]
        )
        col_wedding = FashionCollection(
            title="The Grand Wedding Edit",
            slug="wedding-edit",
            tagline="Royal silks, intricate zari embroidery and regal ensembles",
            description="Handcrafted couture designed for weddings, sangeet and festive receptions.",
            banner_image_url="https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=1200&q=80",
            season="ALL_SEASON",
            occasion="WEDDING",
            is_active=True,
            is_featured=True,
            display_order=2,
            style_tags=["wedding", "couture", "zari", "silk"]
        )
        db.add_all([col_monsoon, col_wedding])
        await db.flush()

        db.add_all([
            CollectionProduct(collection_id=col_monsoon.id, product_id=p2.id, display_order=1),
            CollectionProduct(collection_id=col_monsoon.id, product_id=p4.id, display_order=2),
            CollectionProduct(collection_id=col_wedding.id, product_id=p3.id, display_order=1),
            CollectionProduct(collection_id=col_wedding.id, product_id=p1.id, display_order=2)
        ])

        # 10. Promotional Coupons
        logger.info("Seeding Coupons...")
        c1 = Coupon(
            code="FASHION15",
            description="15% off on orders above Rs.999",
            discount_type=DiscountType.PERCENTAGE,
            discount_value=15.0,
            min_order_amount=999.0,
            max_discount_amount=750.0,
            start_date=datetime.now(timezone.utc) - timedelta(days=1),
            end_date=datetime.now(timezone.utc) + timedelta(days=90),
            is_active=True
        )
        c2 = Coupon(
            code="FESTIVE500",
            description="Flat Rs.500 off on Wedding & Festive Collection",
            discount_type=DiscountType.FIXED,
            discount_value=500.0,
            min_order_amount=2999.0,
            start_date=datetime.now(timezone.utc) - timedelta(days=1),
            end_date=datetime.now(timezone.utc) + timedelta(days=90),
            is_active=True
        )
        db.add_all([c1, c2])

        await db.commit()
        logger.info("Seed data loaded successfully!")


if __name__ == "__main__":
    asyncio.run(seed())
