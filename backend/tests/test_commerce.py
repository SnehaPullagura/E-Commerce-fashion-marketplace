import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from main import app
from app.core.database import get_db
from app.core.base_model import Base
from app.users.models import User, UserRole, UserAddress, AddressType
from app.core.security import get_password_hash, create_access_token
from app.categories.models import Category
from app.products.models import Product, ProductVariant, ProductGender, FitType, OccasionType, SeasonType
from app.inventory.service import InventoryService
from app.cart.service import CartService
from app.cart.schemas import CartItemAdd

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
        # 1. Customer User
        user = User(
            email="buyer@example.com",
            hashed_password=get_password_hash("Password123!"),
            first_name="Priya",
            last_name="Sharma",
            role=UserRole.CUSTOMER,
            is_active=True,
            is_verified=True
        )
        session.add(user)
        await session.flush()

        # 2. Address
        addr = UserAddress(
            user_id=user.id,
            address_type=AddressType.HOME,
            full_name="Priya Sharma",
            phone_number="+919876543210",
            street_address="Flat 402, Highline Residency, Indiranagar",
            city="Bengaluru",
            state="Karnataka",
            postal_code="560038",
            country="India",
            is_default=True
        )
        session.add(addr)
        await session.flush()

        # 3. Category & 2 Vendor Products
        cat = Category(name="Ethnic Wear", slug="ethnic-wear", level=0)
        session.add(cat)
        await session.flush()

        # Product from Vendor A
        p1 = Product(
            vendor_id="vendor-a",
            category_id=cat.id,
            title="Handcrafted Silk Kurta Set",
            slug="silk-kurta-set",
            description="Pure raw silk kurta set with embroidery.",
            base_mrp=5999.0,
            base_price=3999.0,
            gender=ProductGender.WOMEN,
            fit_type=FitType.REGULAR,
            occasion=OccasionType.FESTIVAL,
            season=SeasonType.ALL_SEASON
        )
        session.add(p1)
        await session.flush()
        v1 = ProductVariant(product_id=p1.id, sku="KURTA-A-M", size="M", color_name="Ruby Red", mrp=5999.0, price=3999.0)
        session.add(v1)
        await session.flush()

        # Product from Vendor B
        p2 = Product(
            vendor_id="vendor-b",
            category_id=cat.id,
            title="Embroidered Dupatta",
            slug="embroidered-dupatta",
            description="Georgette dupatta with zari work.",
            base_mrp=1999.0,
            base_price=999.0,
            gender=ProductGender.WOMEN,
            fit_type=FitType.REGULAR,
            occasion=OccasionType.FESTIVAL,
            season=SeasonType.ALL_SEASON
        )
        session.add(p2)
        await session.flush()
        v2 = ProductVariant(product_id=p2.id, sku="DUPATTA-B-FREE", size="Free Size", color_name="Golden", mrp=1999.0, price=999.0)
        session.add(v2)
        await session.flush()

        # Initialize inventory
        await InventoryService.get_or_create_item(session, variant_id=v1.id, sku=v1.sku, vendor_id="vendor-a", initial_stock=10)
        await InventoryService.get_or_create_item(session, variant_id=v2.id, sku=v2.sku, vendor_id="vendor-b", initial_stock=10)

        # Add both to user's cart
        cart = await CartService.get_or_create_cart(session, user_id=user.id)
        await CartService.add_item(session, cart, CartItemAdd(product_id=p1.id, variant_id=v1.id, quantity=1))
        await CartService.add_item(session, cart, CartItemAdd(product_id=p2.id, variant_id=v2.id, quantity=1))

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
async def test_multi_vendor_order_and_payment_flow(client: AsyncClient, db_session: AsyncSession):
    # 1. Login user
    login_res = await client.post("/api/v1/auth/login", json={"email": "buyer@example.com", "password": "Password123!"})
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Get address ID
    addr_res = await client.get("/api/v1/users/me/addresses", headers=headers)
    address_id = addr_res.json()[0]["id"]

    # 2. Checkout (Multi-Vendor Split + 2-Phase Stock Reservation)
    checkout_payload = {
        "shipping_address_id": address_id,
        "payment_method": "UPI"
    }
    order_res = await client.post("/api/v1/orders/checkout", json=checkout_payload, headers=headers)
    assert order_res.status_code == 201, order_res.text
    order_data = order_res.json()
    order_id = order_data["id"]

    # Verify Multi-Vendor order splitting
    assert order_data["status"] == "PENDING"
    assert order_data["payment_status"] == "PENDING"
    assert len(order_data["sub_orders"]) == 2
    assert len(order_data["items"]) == 2

    # 3. Initiate Payment
    pay_init_res = await client.post(
        "/api/v1/payments/initiate",
        json={"order_id": order_id, "gateway": "MOCK", "payment_method": "UPI"},
        headers=headers
    )
    assert pay_init_res.status_code == 200
    txn_ref = pay_init_res.json()["transaction_reference"]

    # 4. Payment Gateway Webhook Callback (Confirms Order & Finalizes Stock Reservation)
    webhook_payload = {
        "transaction_reference": txn_ref,
        "status": "SUCCESS",
        "gateway_payment_id": "pay_mock_12345678"
    }
    webhook_res = await client.post("/api/v1/payments/webhook", json=webhook_payload)
    assert webhook_res.status_code == 200
    assert webhook_res.json()["status"] == "PAID"

    # 5. Verify Order Status Updated to CONFIRMED
    order_check = await client.get(f"/api/v1/orders/{order_id}", headers=headers)
    assert order_check.status_code == 200
    assert order_check.json()["status"] == "CONFIRMED"
    assert order_check.json()["payment_status"] == "PAID"

    # 6. Admin / Vendor Creates Shipment
    sub_order_id = order_check.json()["sub_orders"][0]["id"]
    admin_user = User(
        email="vendor_admin@marketplace.com",
        hashed_password=get_password_hash("AdminPass123!"),
        first_name="Admin",
        role=UserRole.ADMIN,
        is_active=True,
        is_verified=True
    )
    db_session.add(admin_user)
    await db_session.commit()
    admin_token = create_access_token(subject=admin_user.id, role=admin_user.role.value)
    admin_headers = {"Authorization": f"Bearer {admin_token}"}

    ship_res = await client.post(
        "/api/v1/shipping/shipments",
        json={"sub_order_id": sub_order_id, "courier": "MOCK_EXPRESS"},
        headers=admin_headers
    )
    assert ship_res.status_code == 201
    ship_data = ship_res.json()
    assert "waybill_number" in ship_data
    assert len(ship_data["tracking_events"]) >= 1

    # 7. Customer creates Review
    prod_id = order_check.json()["items"][0]["product_id"]
    review_payload = {
        "product_id": prod_id,
        "order_id": order_id,
        "rating": 5,
        "title": "Stunning quality silk!",
        "comment": "The fabric is authentic pure silk and the fit is perfect.",
        "fit_feedback": "TRUE_TO_SIZE",
        "quality_rating": 5
    }
    review_res = await client.post("/api/v1/reviews", json=review_payload, headers=headers)
    assert review_res.status_code == 201
    assert review_res.json()["rating"] == 5
