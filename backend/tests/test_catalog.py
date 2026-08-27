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


@pytest_asyncio.fixture(scope="function")
async def admin_auth_headers(db_session: AsyncSession):
    admin = User(
        email="superadmin@marketplace.com",
        hashed_password=get_password_hash("AdminPass123!"),
        first_name="Super",
        last_name="Admin",
        role=UserRole.SUPER_ADMIN,
        is_active=True,
        is_verified=True
    )
    db_session.add(admin)
    await db_session.commit()

    token = create_access_token(subject=admin.id, role=admin.role.value)
    return {"Authorization": f"Bearer {token}"}


@pytest.mark.asyncio
async def test_fashion_catalog_flow(client: AsyncClient, admin_auth_headers: dict):
    # 1. Create Category
    cat_payload = {
        "name": "Men's Shirts",
        "slug": "mens-shirts",
        "description": "Premium casual and formal shirts for men",
        "commission_rate": 12.5,
        "attributes": [
            {"name": "Fabric", "attribute_type": "MULTI_SELECT", "allowed_values": ["Cotton", "Linen", "Silk"]},
            {"name": "Fit", "attribute_type": "SINGLE_SELECT", "allowed_values": ["Slim", "Regular", "Relaxed"]}
        ]
    }
    cat_res = await client.post("/api/v1/categories", json=cat_payload, headers=admin_auth_headers)
    assert cat_res.status_code == 201, cat_res.text
    category_id = cat_res.json()["id"]

    # 2. Create Brand
    brand_payload = {
        "name": "Noir Couture",
        "slug": "noir-couture",
        "description": "Minimalist luxury streetwear brand",
        "country_of_origin": "India",
        "is_verified": True
    }
    brand_res = await client.post("/api/v1/brands", json=brand_payload, headers=admin_auth_headers)
    assert brand_res.status_code == 201
    brand_id = brand_res.json()["id"]

    # 3. Create Brand Size Chart
    size_chart_payload = {
        "title": "Noir Couture Men Tops Size Guide",
        "brand_id": brand_id,
        "category_id": category_id,
        "chart_type": "TOPWEAR",
        "unit": "INCHES",
        "measurements": [
            {"size_label": "S", "chest_min": 36.0, "chest_max": 38.0, "waist_min": 30.0, "waist_max": 32.0},
            {"size_label": "M", "chest_min": 38.0, "chest_max": 40.0, "waist_min": 32.0, "waist_max": 34.0},
            {"size_label": "L", "chest_min": 40.0, "chest_max": 42.0, "waist_min": 34.0, "waist_max": 36.0},
            {"size_label": "XL", "chest_min": 42.0, "chest_max": 44.0, "waist_min": 36.0, "waist_max": 38.0}
        ]
    }
    chart_res = await client.post("/api/v1/size-charts", json=size_chart_payload, headers=admin_auth_headers)
    assert chart_res.status_code == 201
    size_chart_id = chart_res.json()["id"]

    # 4. Create Fashion Product with Variants & Images
    product_payload = {
        "title": "Minimalist Linen Mandarin Collar Shirt",
        "slug": "minimalist-linen-mandarin-shirt",
        "description": "Breathable 100% pure organic linen shirt tailored for casual and smart-office wear.",
        "brand_id": brand_id,
        "category_id": category_id,
        "size_chart_id": size_chart_id,
        "base_mrp": 2999.0,
        "base_price": 1999.0,
        "gender": "MEN",
        "fabric": "100% Pure Organic Linen",
        "fit_type": "SLIM",
        "pattern": "Solid",
        "occasion": "OFFICE",
        "season": "SUMMER",
        "care_instructions": "Hand wash cold, air dry in shade",
        "style_tags": ["minimalist", "summer", "linen", "mandarin-collar"],
        "color_palette": ["Off-White", "Sage Green", "Charcoal"],
        "variants": [
            {"sku": "NOIR-LIN-WHT-S", "size": "S", "color_name": "Off-White", "color_hex": "#FAF9F6", "mrp": 2999.0, "price": 1999.0},
            {"sku": "NOIR-LIN-WHT-M", "size": "M", "color_name": "Off-White", "color_hex": "#FAF9F6", "mrp": 2999.0, "price": 1999.0},
            {"sku": "NOIR-LIN-WHT-L", "size": "L", "color_name": "Off-White", "color_hex": "#FAF9F6", "mrp": 2999.0, "price": 1999.0}
        ],
        "images": [
            {"image_url": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c", "alt_text": "Front view", "is_primary": True}
        ]
    }
    prod_res = await client.post("/api/v1/products", json=product_payload, headers=admin_auth_headers)
    assert prod_res.status_code == 201, prod_res.text
    prod_data = prod_res.json()
    product_id = prod_data["id"]
    assert prod_data["discount_percentage"] > 0
    assert len(prod_data["variants"]) == 3

    # 5. Test Smart Size Advisor Recommendation
    size_advisor_payload = {
        "chest_in": 39.2,
        "waist_in": 33.0,
        "fit_preference": "SLIM"
    }
    advisor_res = await client.post(f"/api/v1/products/{product_id}/size-advisor", json=size_advisor_payload)
    assert advisor_res.status_code == 200
    advisor_data = advisor_res.json()
    assert advisor_data["recommended_size"] == "M"
    assert advisor_data["confidence_score"] >= 0.8
