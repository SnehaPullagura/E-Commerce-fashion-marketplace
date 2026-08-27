import pytest
import pytest_asyncio
from datetime import datetime, timedelta, timezone
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from main import app
from app.core.database import get_db
from app.core.base_model import Base
from app.users.models import User, UserRole
from app.core.security import get_password_hash, create_access_token
from app.categories.models import Category
from app.products.models import Product, ProductVariant, ProductGender, FitType, OccasionType, SeasonType
from app.coupons.models import Coupon, DiscountType

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestSessionLocal = async_sessionmaker(
    bind=test_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


@pytest_asyncio.fixture(scope="function")
async def db_session():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with TestSessionLocal() as session:
        # Seed test user
        user = User(
            email="shopper@example.com",
            hashed_password=get_password_hash("Password123!"),
            first_name="Fashion",
            last_name="Lover",
            role=UserRole.CUSTOMER,
            is_active=True,
            is_verified=True
        )
        session.add(user)
        await session.flush()

        # Seed category & product
        cat = Category(name="Outerwear", slug="outerwear", level=0)
        session.add(cat)
        await session.flush()

        prod = Product(
            vendor_id="vendor-fashion-hub",
            category_id=cat.id,
            title="Oversized Denim Jacket",
            slug="oversized-denim-jacket",
            description="Classic vintage wash oversized denim jacket.",
            base_mrp=3999.0,
            base_price=2499.0,
            discount_percentage=37.5,
            gender=ProductGender.UNISEX,
            fabric="100% Cotton Denim",
            fit_type=FitType.OVERSIZED,
            occasion=OccasionType.STREETWEAR,
            season=SeasonType.ALL_SEASON
        )
        session.add(prod)
        await session.flush()

        var = ProductVariant(
            product_id=prod.id,
            sku="JKT-DNM-L",
            size="L",
            color_name="Vintage Blue",
            mrp=3999.0,
            price=2499.0
        )
        session.add(var)

        # Seed Coupon
        coupon = Coupon(
            code="FASHION15",
            description="15% off on orders above Rs.1000",
            discount_type=DiscountType.PERCENTAGE,
            discount_value=15.0,
            min_order_amount=1000.0,
            max_discount_amount=500.0,
            start_date=datetime.now(timezone.utc) - timedelta(days=1),
            end_date=datetime.now(timezone.utc) + timedelta(days=30),
            is_active=True
        )
        session.add(coupon)

        await session.commit()
        yield session

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope="function")
async def client(db_session):
    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()


@pytest.mark.asyncio
async def test_cart_and_coupon_flow(client: AsyncClient, db_session: AsyncSession):
    # 1. Login user
    login_res = await client.post("/api/v1/auth/login", json={"email": "shopper@example.com", "password": "Password123!"})
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Get product & variant
    prod_res = await client.get("/api/v1/products/oversized-denim-jacket")
    prod_data = prod_res.json()
    product_id = prod_data["id"]
    variant_id = prod_data["variants"][0]["id"]

    # 3. Add to Cart
    add_payload = {
        "product_id": product_id,
        "variant_id": variant_id,
        "quantity": 1
    }
    cart_res = await client.post("/api/v1/cart/items", json=add_payload, headers=headers)
    assert cart_res.status_code == 200, cart_res.text
    cart_data = cart_res.json()
    assert cart_data["items_count"] == 1
    assert cart_data["subtotal"] == 2499.0
    assert len(cart_data["vendor_groups"]) == 1
    assert cart_data["vendor_groups"][0]["vendor_id"] == "vendor-fashion-hub"

    # 4. Apply Coupon
    coupon_payload = {
        "code": "FASHION15",
        "cart_amount": 2499.0
    }
    coupon_res = await client.post("/api/v1/coupons/apply", json=coupon_payload, headers=headers)
    assert coupon_res.status_code == 200
    c_data = coupon_res.json()
    assert c_data["is_valid"] is True
    # 15% of 2499 = 374.85
    assert c_data["discount_amount"] == 374.85

    # 5. Add to Wishlist
    wish_res = await client.post("/api/v1/wishlist/items", json={"product_id": product_id}, headers=headers)
    assert wish_res.status_code == 200
    wish_data = wish_res.json()
    assert wish_data["items_count"] == 1
