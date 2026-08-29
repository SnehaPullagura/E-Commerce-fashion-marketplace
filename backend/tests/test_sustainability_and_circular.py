import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from app.sustainability.eco_passport import DPPEngine
from app.sustainability.circular_engine import (
    CircularTakebackEngine, CarbonOffsetCalculator, TradeInValuationRequest, GarmentConditionGrade
)


@pytest.mark.asyncio
async def test_dpp_passport_generation():
    passport = DPPEngine.generate_passport(
        product_id="prod_silk_blouse_99",
        title="Artisanal Silk Shirt",
        brand="Maison Aurelia"
    )
    assert passport.product_id == "prod_silk_blouse_99"
    assert passport.carbon_footprint_kg_co2e > 0
    assert passport.repairability_score >= 8.0
    assert passport.sustainability_grade in ["A+", "A", "B", "C", "D"]
    assert "GOTS Organic" in passport.certification_badges
    assert len(passport.provenance_hash) == 64
    assert "https://" in passport.verification_qr_uri


@pytest.mark.asyncio
async def test_circular_tradein_valuation():
    request = TradeInValuationRequest(
        brand_name="Gucci",
        original_mrp=800.0,
        age_months=6,
        condition=GarmentConditionGrade.PRISTINE_WITH_TAGS,
        weight_grams=500.0
    )
    res = CircularTakebackEngine.calculate_trade_in_voucher(request)
    assert res["brand"] == "Gucci"
    assert res["estimated_store_credit"] >= 200.0
    assert res["circular_impact"]["landfill_diverted_kg"] == 0.5
    assert res["circular_impact"]["co2_emissions_saved_kg"] > 0


@pytest.mark.asyncio
async def test_sustainability_api_routes():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # Get DPP endpoint
        dpp_resp = await client.get("/api/v1/sustainability/digital-passport/prod_101?title=Cashmere+Knit&brand=Loro+Piana")
        assert dpp_resp.status_code == 200
        dpp_data = dpp_resp.json()
        assert dpp_data["product_id"] == "prod_101"
        assert "provenance_hash" in dpp_data

        # Trade in estimate API
        trade_payload = {
            "brand_name": "Prada",
            "original_mrp": 1200.0,
            "age_months": 12,
            "condition": "EXCELLENT_BARELY_WORN",
            "material_type": "VIRGIN_WOOL",
            "weight_grams": 600.0
        }
        trade_resp = await client.post("/api/v1/sustainability/trade-in/estimate", json=trade_payload)
        assert trade_resp.status_code == 200
        assert trade_resp.json()["estimated_store_credit"] > 0

        # Carbon offset calculation
        offset_payload = {
            "order_weight_kg": 2.5,
            "shipping_distance_km": 800.0,
            "expedited_air": False
        }
        offset_resp = await client.post("/api/v1/sustainability/carbon-offset/calculate", json=offset_payload)
        assert offset_resp.status_code == 200
        assert offset_resp.json()["recommended_offset_usd"] > 0
