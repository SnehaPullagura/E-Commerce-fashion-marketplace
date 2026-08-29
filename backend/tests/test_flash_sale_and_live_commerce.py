import pytest
from datetime import datetime, timezone, timedelta
from httpx import AsyncClient, ASGITransport
from main import app
from app.commerce.flash_sales import flash_engine, FlashSaleDrop
from app.commerce.live_streaming import live_manager


@pytest.mark.asyncio
async def test_flash_sale_atomic_reservation():
    now = datetime.now(timezone.utc)
    drop = FlashSaleDrop(
        drop_id="drop_paris_fashion_001",
        product_id="prod_trench_coat",
        title="Limited Runway Trench",
        original_price=1200.0,
        flash_price=600.0,
        total_inventory=3,
        start_time=now - timedelta(minutes=1),
        end_time=now + timedelta(minutes=30)
    )
    flash_engine.register_drop(drop)

    # First user claims 2 items
    claim1 = flash_engine.claim_atomic_reservation("drop_paris_fashion_001", "usr_101", quantity=2)
    assert claim1["success"] is True
    assert claim1["quantity_reserved"] == 2

    # Second user claims 1 item (reaches cap of 3)
    claim2 = flash_engine.claim_atomic_reservation("drop_paris_fashion_001", "usr_102", quantity=1)
    assert claim2["success"] is True

    # Third user tries to claim 1 item (stock exhausted)
    claim3 = flash_engine.claim_atomic_reservation("drop_paris_fashion_001", "usr_103", quantity=1)
    assert claim3["success"] is False
    assert "Sold Out" in claim3["error"]


@pytest.mark.asyncio
async def test_live_streaming_and_auction_mechanics():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # Create stream
        stream_payload = {
            "vendor_id": "vend_gucci_milan",
            "channel_title": "Milan Fashion Week Runway Exclusive",
            "host_name": "Alessandra V.",
            "pinned_product_id": "prod_couture_gown_09"
        }
        create_resp = await client.post("/api/v1/commerce/live/streams/create", json=stream_payload)
        assert create_resp.status_code == 200
        stream_data = create_resp.json()
        stream_id = stream_data["stream_id"]

        # Start auction
        auction_payload = {
            "product_id": "prod_couture_gown_09",
            "starting_price": 500.0,
            "duration_minutes": 10,
            "min_increment": 50.0
        }
        start_auc_resp = await client.post(f"/api/v1/commerce/live/streams/{stream_id}/auction/start", json=auction_payload)
        assert start_auc_resp.status_code == 200

        # Place initial valid bid
        bid1_resp = await client.post(f"/api/v1/commerce/live/streams/{stream_id}/bids", json={
            "user_id": "usr_collector_1",
            "user_name": "Eleanor Vance",
            "bid_amount": 550.0
        })
        assert bid1_resp.status_code == 200
        assert bid1_resp.json()["highest_bid"] == 550.0

        # Place invalid under-bid
        bid2_resp = await client.post(f"/api/v1/commerce/live/streams/{stream_id}/bids", json={
            "user_id": "usr_collector_2",
            "user_name": "Julian Moreau",
            "bid_amount": 570.0  # Needs at least 550 + 50 = 600
        })
        assert bid2_resp.status_code == 400

        # Send stream reaction
        react_resp = await client.post(f"/api/v1/commerce/live/streams/{stream_id}/reaction")
        assert react_resp.status_code == 200
        assert react_resp.json()["likes_count"] > 0
