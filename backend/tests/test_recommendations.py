import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from main import app
from app.core.database import get_db
from app.core.base_model import Base
from app.users.models import User, UserRole, UserStylePreference
from app.core.security import get_password_hash
from app.categories.models import Category
from app.products.models import Product, ProductGender, FitType, OccasionType, SeasonType

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
        # Category
        cat = Category(name="Apparel", slug="apparel", level=0)
        session.add(cat)
        await session.flush()

        # Seed 4 products for complete outfit
        p1 = Product(
            vendor_id="v1", category_id=cat.id, title="Classic Black Linen Shirt",
            slug="classic-black-linen-shirt", description="Pure linen shirt.",
            base_mrp=2999.0, base_price=1999.0, gender=ProductGender.MEN,
            fit_type=FitType.SLIM, occasion=OccasionType.OFFICE, season=SeasonType.SUMMER,
            style_tags=["minimalist", "office", "linen"]
        )
        p2 = Product(
            vendor_id="v1", category_id=cat.id, title="Tailored Chino Trousers",
            slug="tailored-chino-trousers", description="Slim fit cotton chinos.",
            base_mrp=2499.0, base_price=1799.0, gender=ProductGender.MEN,
            fit_type=FitType.SLIM, occasion=OccasionType.OFFICE, season=SeasonType.ALL_SEASON,
            style_tags=["minimalist", "office", "chino"]
        )
        p3 = Product(
            vendor_id="v2", category_id=cat.id, title="Italian Leather Penny Loafers",
            slug="italian-leather-penny-loafers", description="Handmade genuine leather loafers.",
            base_mrp=5999.0, base_price=4499.0, gender=ProductGender.MEN,
            fit_type=FitType.REGULAR, occasion=OccasionType.OFFICE, season=SeasonType.ALL_SEASON,
            style_tags=["classic", "office", "leather"]
        )
        session.add_all([p1, p2, p3])
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
async def test_complete_the_look_outfit_engine(client: AsyncClient, db_session: AsyncSession):
    # Fetch product ID
    prod_res = await client.get("/api/v1/products/classic-black-linen-shirt")
    product_id = prod_res.json()["id"]

    # Call Complete-the-Look Engine
    ctl_res = await client.get(f"/api/v1/recommendations/complete-the-look/{product_id}")
    assert ctl_res.status_code == 200, ctl_res.text
    ctl_data = ctl_res.json()

    assert ctl_data["main_product_id"] == product_id
    assert len(ctl_data["outfit_items"]) >= 2
    assert ctl_data["bundle_discount_price"] < ctl_data["bundle_total_mrp"]
    assert ctl_data["bundle_savings"] > 0
    assert "Office" in ctl_data["outfit_style_theme"]


@pytest.mark.asyncio
async def test_personalized_fashion_feed(client: AsyncClient):
    feed_res = await client.get("/api/v1/recommendations/personalized-feed")
    assert feed_res.status_code == 200
    feed_data = feed_res.json()
    assert len(feed_data["items"]) >= 1
    assert feed_data["items"][0]["fashion_dna_match_score"] >= 70.0
