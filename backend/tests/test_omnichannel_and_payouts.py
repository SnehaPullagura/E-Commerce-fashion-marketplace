import pytest
from datetime import datetime, timezone
from httpx import AsyncClient, ASGITransport
from main import app
from app.shipping.omnichannel import OmniChannelLogisticsEngine, RoutingOptimizationRequest, ShipmentItem
from app.vendors.automated_payouts import escrow_engine, VendorPayoutAccount, OrderSettlementItem


@pytest.mark.asyncio
async def test_dark_store_haversine_and_routing():
    # Customer located near Mumbai BKC
    req = RoutingOptimizationRequest(
        customer_lat=19.075,
        customer_lon=72.877,
        customer_city="Mumbai",
        items=[
            ShipmentItem(product_id="p1", vendor_id="v_gucci", title="Silk Scarf", weight_kg=0.2, price=250.0),
            ShipmentItem(product_id="p2", vendor_id="v_prada", title="Leather Belt", weight_kg=0.4, price=380.0)
        ]
    )
    result = OmniChannelLogisticsEngine.optimize_order_routing(req)
    assert result["destination_city"] == "Mumbai"
    assert result["hyperlocal_eligible"] is True
    assert result["total_packages"] == 2
    assert result["total_shipping_fee_usd"] > 0


@pytest.mark.asyncio
async def test_vendor_escrow_settlement():
    account = VendorPayoutAccount(
        vendor_id="vend_atelier_roma",
        vendor_name="Atelier Roma",
        platform_commission_rate=0.10,
        rolling_reserve_pct=0.05
    )
    orders = [
        OrderSettlementItem(order_id="ord_1", vendor_id="vend_atelier_roma", gross_order_amount=1000.0, delivered_at=datetime.now(timezone.utc)),
        OrderSettlementItem(order_id="ord_2", vendor_id="vend_atelier_roma", gross_order_amount=500.0, delivered_at=datetime.now(timezone.utc))
    ]
    settlement = escrow_engine.process_order_settlement(account, orders)
    assert settlement["gross_revenue"] == 1500.0
    assert settlement["commission_amount"] == 150.0  # 10%
    assert settlement["reserve_held_amount"] == 75.0   # 5%
    assert settlement["net_payable"] == 1275.0        # 1500 - 150 - 75
    assert settlement["ledger_current_balance"] >= 1275.0

    # Test reserve release
    rel_res = escrow_engine.release_rolling_reserve("vend_atelier_roma", amount=25.0)
    assert rel_res["released_amount"] == 25.0
    assert rel_res["remaining_reserve_held"] == 50.0

    # Test payout disbursement
    disburse_res = escrow_engine.request_payout_disbursement("vend_atelier_roma", amount=500.0)
    assert disburse_res["disbursed_amount"] == 500.0
    assert disburse_res["lifetime_payouts_total"] >= 500.0


@pytest.mark.asyncio
async def test_logistics_and_payout_api_endpoints():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # Dark stores list
        ds_resp = await client.get("/api/v1/logistics/dark-stores/all")
        assert ds_resp.status_code == 200
        assert len(ds_resp.json()["dark_stores"]) >= 5

        # Route optimization API
        route_payload = {
            "customer_lat": 51.507,
            "customer_lon": -0.127,
            "customer_city": "London",
            "items": [
                {
                    "product_id": "p_coat",
                    "vendor_id": "vend_burberry",
                    "title": "Cashmere Coat",
                    "weight_kg": 1.5,
                    "price": 1800.0
                }
            ],
            "prefer_eco": True
        }
        route_resp = await client.post("/api/v1/logistics/route-optimize", json=route_payload)
        assert route_resp.status_code == 200
        assert "nearest_fulfillment_hub" in route_resp.json()

        # Batch settlement API
        batch_payload = {
            "account": {
                "vendor_id": "vend_milan_hub",
                "vendor_name": "Milan Hub",
                "platform_commission_rate": 0.15,
                "rolling_reserve_pct": 0.05
            },
            "orders": [
                {
                    "order_id": "ord_99",
                    "vendor_id": "vend_milan_hub",
                    "gross_order_amount": 2000.0,
                    "delivered_at": "2026-08-29T10:00:00Z",
                    "return_window_expired": True
                }
            ]
        }
        batch_resp = await client.post("/api/v1/logistics/payouts/batch-settle", json=batch_payload)
        assert batch_resp.status_code == 200
        assert batch_resp.json()["net_payable"] == 1600.0  # 2000 - 300 - 100
