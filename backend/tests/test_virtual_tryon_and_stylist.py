import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from app.styling.virtual_tryon import (
    CustomerAnthropometrics, GarmentSpecs, FabricType, VirtualTryOnEngine, BodyShapeArchetype
)
from app.styling.ai_stylist import ColorTheoryEngine, UndertoneType


@pytest.mark.asyncio
async def test_virtual_tryon_engine_direct():
    anthro = CustomerAnthropometrics(
        height_cm=170.0,
        bust_chest_cm=88.0,
        waist_cm=68.0,
        high_hip_cm=90.0,
        low_hip_cm=94.0,
        shoulder_width_cm=39.0
    )
    garment = GarmentSpecs(
        garment_id="prod_silk_dress_001",
        garment_type="DRESS",
        size_label="M",
        chest_width_cm=46.0,  # 92cm circumference
        waist_width_cm=36.0,  # 72cm circumference
        hip_width_cm=50.0,    # 100cm circumference
        garment_length_cm=115.0,
        fabric_type=FabricType.SILK_CHARMEUSE,
        stretch_percentage=2.0
    )

    result = VirtualTryOnEngine.simulate_try_on(anthro, garment)
    assert result["garment_id"] == "prod_silk_dress_001"
    assert result["customer_body_shape"] == BodyShapeArchetype.HOURGLASS.value
    assert result["overall_fit_confidence"] >= 80.0
    assert result["verdict"] == "PERFECT_MATCH"
    assert "chest" in result["tension_zones"]
    assert "fabric_simulation" in result


@pytest.mark.asyncio
async def test_color_theory_and_stylist_engine():
    # Complementary test
    match = ColorTheoryEngine.calculate_color_harmony_score("#0000FF", "#FF8000")
    assert match["harmony_score"] >= 80.0

    # Undertone test
    warm_palette = ColorTheoryEngine.get_palette_for_undertone(UndertoneType.WARM)
    assert len(warm_palette["signature_accents"]) > 0


@pytest.mark.asyncio
async def test_styling_api_endpoints():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # Body shapes endpoint
        resp = await client.get("/api/v1/styling/try-on/body-shapes")
        assert resp.status_code == 200
        data = resp.json()
        assert "archetypes" in data
        assert len(data["archetypes"]) >= 5

        # Try-on simulation API
        sim_payload = {
            "anthropometrics": {
                "height_cm": 175.0,
                "bust_chest_cm": 92.0,
                "waist_cm": 74.0,
                "high_hip_cm": 94.0,
                "low_hip_cm": 98.0,
                "shoulder_width_cm": 41.0
            },
            "garment": {
                "garment_id": "dress_001",
                "garment_type": "DRESS",
                "size_label": "L",
                "chest_width_cm": 48.0,
                "waist_width_cm": 39.0,
                "hip_width_cm": 52.0,
                "garment_length_cm": 120.0,
                "fabric_type": "COTTON_JERSEY",
                "stretch_percentage": 5.0
            }
        }
        sim_resp = await client.post("/api/v1/styling/try-on/simulate", json=sim_payload)
        assert sim_resp.status_code == 200
        sim_data = sim_resp.json()
        assert "overall_fit_confidence" in sim_data
        assert sim_data["overall_fit_confidence"] > 0

        # AI Advisor Chat
        chat_payload = {
            "prompt": "What should I wear to a black tie gala in autumn?",
            "user_gender": "FEMALE",
            "occasion": "BLACK_TIE"
        }
        chat_resp = await client.post("/api/v1/styling/advisor/chat", json=chat_payload)
        assert chat_resp.status_code == 200
        chat_data = chat_resp.json()
        assert "stylist_curation" in chat_data
