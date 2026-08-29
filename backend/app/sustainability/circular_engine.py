"""
Circular Fashion Takeback, Trade-In Valuation & Carbon Offset Engine.
Computes instant buyback vouchers, diverted landfill weights, and shipping carbon offsets.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from enum import Enum


class GarmentConditionGrade(str, Enum):
    PRISTINE_WITH_TAGS = "PRISTINE_WITH_TAGS"
    EXCELLENT_BARELY_WORN = "EXCELLENT_BARELY_WORN"
    GOOD_GENTLY_USED = "GOOD_GENTLY_USED"
    FAIR_MINOR_SIGNS_OF_WEAR = "FAIR_MINOR_SIGNS_OF_WEAR"
    UPCYCLE_REPAIR_NEEDED = "UPCYCLE_REPAIR_NEEDED"


class TradeInValuationRequest(BaseModel):
    brand_name: str
    original_mrp: float
    age_months: int
    condition: GarmentConditionGrade
    material_type: str = "ORGANIC_SILK"
    weight_grams: float = 450.0


class CircularTakebackEngine:
    CONDITION_MULTIPLIERS = {
        GarmentConditionGrade.PRISTINE_WITH_TAGS: 0.55,
        GarmentConditionGrade.EXCELLENT_BARELY_WORN: 0.40,
        GarmentConditionGrade.GOOD_GENTLY_USED: 0.28,
        GarmentConditionGrade.FAIR_MINOR_SIGNS_OF_WEAR: 0.16,
        GarmentConditionGrade.UPCYCLE_REPAIR_NEEDED: 0.08,
    }

    @staticmethod
    def calculate_trade_in_voucher(request: TradeInValuationRequest) -> Dict[str, Any]:
        """Calculates store credit voucher valuation and circular impact."""
        # Age depreciation curve (depreciates ~2.5% per month, capped at 60% decay)
        age_factor = max(0.40, 1.0 - (request.age_months * 0.025))
        base_rate = CircularTakebackEngine.CONDITION_MULTIPLIERS.get(request.condition, 0.20)

        # Luxury tier bonus
        luxury_brands = {"chanel", "gucci", "prada", "hermes", "saint laurent", "dior", "bottega veneta"}
        brand_multiplier = 1.25 if request.brand_name.strip().lower() in luxury_brands else 1.0

        voucher_value = round(request.original_mrp * base_rate * age_factor * brand_multiplier, 2)
        voucher_value = max(10.0, voucher_value)  # Minimum guarantee

        # Environmental metrics
        landfill_diverted_kg = round(request.weight_grams / 1000.0, 2)
        co2_saved_kg = round(landfill_diverted_kg * 8.5, 2)  # Avg 8.5 kg CO2e saved per kg diverted garment

        return {
            "brand": request.brand_name,
            "original_mrp": request.original_mrp,
            "condition": request.condition.value,
            "estimated_store_credit": voucher_value,
            "bonus_points_earned": int(voucher_value * 10),
            "circular_impact": {
                "landfill_diverted_kg": landfill_diverted_kg,
                "co2_emissions_saved_kg": co2_saved_kg,
                "trees_equivalent": round(co2_saved_kg / 21.0, 2)
            },
            "next_lifecycle_path": (
                "Direct Authenticated Resale" if request.condition in [
                    GarmentConditionGrade.PRISTINE_WITH_TAGS,
                    GarmentConditionGrade.EXCELLENT_BARELY_WORN
                ] else ("Renewed / Cleaned Vintage Market" if request.condition == GarmentConditionGrade.GOOD_GENTLY_USED else "Artisanal Upcycling & Fiber Reclamation")
            )
        }


class CarbonOffsetCalculator:
    @staticmethod
    def calculate_order_offset(
        order_weight_kg: float,
        shipping_distance_km: float,
        expedited_air: bool = False
    ) -> Dict[str, Any]:
        """Calculates carbon footprint for fulfillment and tree-planting offset cost."""
        # Emission factors: Air = 0.50 kg CO2/t-km, Road Ground = 0.12 kg CO2/t-km
        emission_factor = 0.00050 if expedited_air else 0.00012
        transport_co2_kg = round(order_weight_kg * shipping_distance_km * emission_factor, 2)
        packaging_co2_kg = 0.35  # Recycled craft box + compostable polybag
        total_co2_kg = round(transport_co2_kg + packaging_co2_kg, 2)

        # Carbon offset pricing: $15 per ton ($0.015 per kg)
        offset_cost_usd = max(0.49, round(total_co2_kg * 0.015, 2))

        return {
            "order_weight_kg": order_weight_kg,
            "distance_km": shipping_distance_km,
            "transport_method": "Expedited Air" if expedited_air else "Eco Ground Route",
            "carbon_emissions_kg_co2e": total_co2_kg,
            "recommended_offset_usd": offset_cost_usd,
            "certified_project": "Global Reforestation & Mangrove Restoration Verified by Gold Standard"
        }
