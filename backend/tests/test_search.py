import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from main import app
from app.core.database import get_db
from app.core.base_model import Base
from app.users.models import User, UserRole
from app.core.security import get_password_hash, create_access_token
from app.categories.models import Category
from app.products.models import Product, ProductVariant, ProductImage, ProductGender, FitType, OccasionType, SeasonType

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
        # Seed test category and products
        cat = Category(name="Dresses", slug="dresses", level=0)
        session.add(cat)
        await session.flush()

        prod1 = Product(
            vendor_id="v1",
            category_id=cat.id,
            title="Black Velvet Bodycon Party Dress",
            slug="black-velvet-bodycon-party-dress",
            description="Stunning black velvet party dress for evening soirees.",
            base_mrp=4999.0,
            base_price=3499.0,
            gender=ProductGender.WOMEN,
            fabric="Velvet",
            fit_type=FitType.SLIM,
            occasion=OccasionType.PARTY,
            season=SeasonType.WINTER,
            style_tags=["glam", "party", "velvet", "bodycon"]
        )
        session.add(prod1)
        await session.flush()

        v1 = ProductVariant(
            product_id=prod1.id,
            sku="DRS-BLK-M",
            size="M",
            color_name="Black",
            color_hex="#000000",
            mrp=4999.0,
            price=3499.0
        )
        session.add(v1)
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
async def test_fashion_search_nlp_extraction(client: AsyncClient):
    # Test natural query: "black velvet party dress"
    res = await client.get("/api/v1/search?q=black+velvet+party+dress")
    assert res.status_code == 200, res.text
    data = res.json()

    assert data["extracted_tokens"]["detected_color"] == "Black"
    assert data["extracted_tokens"]["detected_fabric"] == "Velvet"
    assert data["extracted_tokens"]["detected_occasion"] == "PARTY"
    assert len(data["items"]) == 1
    assert data["items"][0]["title"] == "Black Velvet Bodycon Party Dress"


@pytest.mark.asyncio
async def test_search_autocomplete(client: AsyncClient):
    res = await client.get("/api/v1/search/autocomplete?q=velvet")
    assert res.status_code == 200
    data = res.json()
    assert len(data["suggestions"]) >= 1
    assert data["suggestions"][0]["type"] == "PRODUCT"
    assert len(data["trending_searches"]) > 0
