import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from main import app
from app.core.database import get_db
from app.core.base_model import Base
from app.users.models import User, UserRole
from app.core.security import get_password_hash, create_access_token

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
        admin = User(
            email="analytics_admin@marketplace.com",
            hashed_password=get_password_hash("AdminPass123!"),
            first_name="Admin",
            role=UserRole.SUPER_ADMIN,
            is_active=True,
            is_verified=True
        )
        session.add(admin)
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
async def test_analytics_endpoints(client: AsyncClient, db_session: AsyncSession):
    # Login admin
    login_res = await client.post("/api/v1/auth/login", json={"email": "analytics_admin@marketplace.com", "password": "AdminPass123!"})
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 1. Overview analytics
    overview_res = await client.get("/api/v1/analytics/overview?days=30", headers=headers)
    assert overview_res.status_code == 200, overview_res.text
    data = overview_res.json()
    assert "total_gmv" in data
    assert "gmv_trend" in data
    assert "top_categories" in data

    # 2. Fashion Trend Radar
    trend_res = await client.get("/api/v1/analytics/trends")
    assert trend_res.status_code == 200
    t_data = trend_res.json()
    assert "top_fabrics" in t_data
    assert "top_color_palettes" in t_data

    # 3. Conversion Funnel
    funnel_res = await client.get("/api/v1/analytics/funnel", headers=headers)
    assert funnel_res.status_code == 200
    f_data = funnel_res.json()
    assert len(f_data["steps"]) == 4
    assert f_data["overall_conversion_rate"] > 0
