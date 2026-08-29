"""
Sustainability, Circular Fashion & Digital Product Passport REST Router.
"""

from fastapi import APIRouter, HTTPException, Query, status
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

from app.sustainability.eco_passport import DPPEngine
from app.sustainability.circular_engine import (
    CircularTakebackEngine, CarbonOffsetCalculator, TradeInValuationRequest, GarmentConditionGrade
)

router = APIRouter(prefix="/sustainability", tags=["Sustainability & Circular Fashion"])


class CarbonOffsetRequest(BaseModel):
    order_weight_kg: float = 1.2
    shipping_distance_km: float = 450.0
    expedited_air: bool = False


@router.get("/digital-passport/{product_id}")
def get_digital_product_passport(
    product_id: str,
    title: Optional[str] = "Handcrafted Silk Evening Dress",
    brand: Optional[str] = "Aurelia Milano"
):
    """Fetches EU ESPR-compliant Digital Product Passport with traceability hash."""
    return DPPEngine.generate_passport(
        product_id=product_id,
        title=title or "Fashion Apparel",
        brand=brand or "Marketplace Atelier"
    )


@router.post("/trade-in/estimate")
def estimate_garment_trade_in(payload: TradeInValuationRequest):
    """Calculates trade-in buyback voucher credit and environmental footprint savings."""
    return CircularTakebackEngine.calculate_trade_in_voucher(payload)


@router.post("/carbon-offset/calculate")
def calculate_shipping_carbon_offset(payload: CarbonOffsetRequest):
    """Calculates order fulfillment emissions and carbon offset token pricing."""
    return CarbonOffsetCalculator.calculate_order_offset(
        order_weight_kg=payload.order_weight_kg,
        shipping_distance_km=payload.shipping_distance_km,
        expedited_air=payload.expedited_air
    )
