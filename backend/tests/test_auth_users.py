import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from main import app
from app.core.database import get_db
from app.core.base_model import Base

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
async def test_register_and_login(client: AsyncClient):
    # 1. Register customer
    register_payload = {
        "email": "fashionista@example.com",
        "password": "Password123!",
        "first_name": "Zara",
        "last_name": "Fashion",
        "phone": "+919876543210",
        "gender_preference": "WOMEN"
    }
    response = await client.post("/api/v1/auth/register", json=register_payload)
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["email"] == "fashionista@example.com"
    assert data["first_name"] == "Zara"
    assert data["role"] == "CUSTOMER"

    # 2. Login
    login_payload = {
        "email": "fashionista@example.com",
        "password": "Password123!"
    }
    login_res = await client.post("/api/v1/auth/login", json=login_payload)
    assert login_res.status_code == 200, login_res.text
    tokens = login_res.json()
    assert "access_token" in tokens
    assert "refresh_token" in tokens

    token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Get /users/me
    me_res = await client.get("/api/v1/users/me", headers=headers)
    assert me_res.status_code == 200
    me_data = me_res.json()
    assert me_data["email"] == "fashionista@example.com"

    # 4. Update Fashion DNA Profile
    dna_payload = {
        "style_personas": ["Minimalist", "Streetwear", "Chic"],
        "favorite_colors": ["Black", "Sage Green", "Charcoal"],
        "preferred_brands": ["Zara", "H&M", "FabIndia"],
        "preferred_categories": ["Dresses", "Tops", "Jeans"],
        "occasion_interests": ["Party", "Office", "Weekend Brunch"],
        "price_sensitivity": "PREMIUM"
    }
    dna_res = await client.put("/api/v1/users/me/fashion-dna", json=dna_payload, headers=headers)
    assert dna_res.status_code == 200
    dna_data = dna_res.json()
    assert "Minimalist" in dna_data["style_personas"]
    assert dna_data["price_sensitivity"] == "PREMIUM"

    # 5. Update Size Profile (Size Intelligence)
    size_payload = {
        "height_cm": 168.0,
        "weight_kg": 58.0,
        "chest_in": 34.0,
        "waist_in": 28.0,
        "hips_in": 38.0,
        "preferred_top_size": "M",
        "preferred_bottom_size": "28",
        "fit_preference": "SLIM"
    }
    size_res = await client.put("/api/v1/users/me/size-profile", json=size_payload, headers=headers)
    assert size_res.status_code == 200
    size_data = size_res.json()
    assert size_data["chest_in"] == 34.0
    assert size_data["fit_preference"] == "SLIM"
