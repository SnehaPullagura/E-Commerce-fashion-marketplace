import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from main import app
from app.core.database import get_db
from app.core.base_model import Base
from app.users.models import User, UserRole
from app.core.security import get_password_hash, create_access_token
from app.vendors.models import VendorProfile, VendorStatus

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
        # Seed Admin user
        admin = User(
            email="superadmin@marketplace.com",
            hashed_password=get_password_hash("AdminPass123!"),
            first_name="Super",
            last_name="Admin",
            role=UserRole.SUPER_ADMIN,
            is_active=True,
            is_verified=True
        )
        # Seed prospective Vendor user
        vendor_user = User(
            email="designer@studio.com",
            hashed_password=get_password_hash("DesignerPass123!"),
            first_name="Anita",
            last_name="Dongre",
            role=UserRole.CUSTOMER,
            is_active=True,
            is_verified=True
        )
        session.add_all([admin, vendor_user])
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
async def test_vendor_onboarding_and_admin_governance(client: AsyncClient, db_session: AsyncSession):
    # 1. Login prospective vendor
    v_login = await client.post("/api/v1/auth/login", json={"email": "designer@studio.com", "password": "DesignerPass123!"})
    vendor_token = v_login.json()["access_token"]
    vendor_headers = {"Authorization": f"Bearer {vendor_token}"}

    # 2. Submit Vendor Onboarding KYC
    onboard_payload = {
        "business_name": "Anita Dongre Haute Couture",
        "legal_name": "House of Anita Dongre Ltd",
        "slug": "anita-dongre",
        "gst_number": "27AAACH7409R1ZZ",
        "pan_number": "AAACH7409R",
        "bank_account_name": "House of Anita Dongre Ltd",
        "bank_account_number": "98765432101234",
        "bank_ifsc": "HDFC0000123",
        "bank_name": "HDFC Bank",
        "city": "Mumbai",
        "state": "Maharashtra",
        "postal_code": "400013",
        "description": "Sustainable luxury Indian wear and contemporary silhouettes.",
        "support_email": "care@anitadongre.com",
        "support_phone": "+912248900000"
    }
    onboard_res = await client.post("/api/v1/vendors/onboard", json=onboard_payload, headers=vendor_headers)
    assert onboard_res.status_code == 201, onboard_res.text
    vendor_data = onboard_res.json()
    vendor_id = vendor_data["id"]
    assert vendor_data["business_name"] == "Anita Dongre Haute Couture"

    # 3. View Public Storefront
    store_res = await client.get("/api/v1/vendors/store/anita-dongre")
    assert store_res.status_code == 200
    store_data = store_res.json()
    assert store_data["business_name"] == "Anita Dongre Haute Couture"

    # 4. Admin Login & View Stats
    a_login = await client.post("/api/v1/auth/login", json={"email": "superadmin@marketplace.com", "password": "AdminPass123!"})
    admin_token = a_login.json()["access_token"]
    admin_headers = {"Authorization": f"Bearer {admin_token}"}

    stats_res = await client.get("/api/v1/admin/stats", headers=admin_headers)
    assert stats_res.status_code == 200
    stats_data = stats_res.json()
    assert stats_data["total_vendors"] >= 1

    # 5. Admin Moderates Vendor Commission Rate
    mod_res = await client.put(
        f"/api/v1/admin/vendors/{vendor_id}/moderate",
        json={"status": "APPROVED", "commission_rate": 10.0, "reason": "Verified premier designer brand"},
        headers=admin_headers
    )
    assert mod_res.status_code == 200
    assert mod_res.json()["commission_rate"] == 10.0
