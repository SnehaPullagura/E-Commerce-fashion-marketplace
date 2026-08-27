"""
Comprehensive Fabric Science and Textile Engineering Module for Fashion Marketplace.
Contains deep textile taxonomy, fiber characteristics, weave structures, thermal insulation ratings,
drape coefficients, moisture regain properties, and garment care algorithms.
"""

from typing import Dict, List, Optional, Any, Tuple
from enum import Enum
from pydantic import BaseModel, Field


class FiberCategory(str, Enum):
    NATURAL_PROTEIN = "NATURAL_PROTEIN"
    NATURAL_CELLULOSIC = "NATURAL_CELLULOSIC"
    REGENERATED_CELLULOSIC = "REGENERATED_CELLULOSIC"
    SYNTHETIC_POLYMER = "SYNTHETIC_POLYMER"
    SPECIALTY_METALLIC = "SPECIALTY_METALLIC"
    BLENDED_HYBRID = "BLENDED_HYBRID"


class WeaveType(str, Enum):
    PLAIN_WEAVE = "PLAIN_WEAVE"
    TWILL_WEAVE = "TWILL_WEAVE"
    SATIN_WEAVE = "SATIN_WEAVE"
    JACQUARD_WEAVE = "JACQUARD_WEAVE"
    DOBBY_WEAVE = "DOBBY_WEAVE"
    KNIT_SINGLE_JERSEY = "KNIT_SINGLE_JERSEY"
    KNIT_DOUBLE_JERSEY = "KNIT_DOUBLE_JERSEY"
    KNIT_RIB = "KNIT_RIB"
    KNIT_FRENCH_TERRY = "KNIT_FRENCH_TERRY"
    KNIT_FLEECE = "KNIT_FLEECE"
    NON_WOVEN = "NON_WOVEN"


class FabricDrapeCoefficient(str, Enum):
    EXTRA_FLUID = "EXTRA_FLUID"
    FLUID = "FLUID"
    MODERATE_DRAPE = "MODERATE_DRAPE"
    STRUCTURED = "STRUCTURED"
    RIGID_SCULPTURAL = "RIGID_SCULPTURAL"


class SeasonalitySuitability(str, Enum):
    PEAK_SUMMER = "PEAK_SUMMER"
    SUMMER_SPRING = "SUMMER_SPRING"
    ALL_WEATHER_TRANSITIONAL = "ALL_WEATHER_TRANSITIONAL"
    AUTUMN_WINTER = "AUTUMN_WINTER"
    DEEP_WINTER = "DEEP_WINTER"


class FabricSpecification(BaseModel):
    name: str
    fiber_category: FiberCategory
    primary_fiber: str
    secondary_fiber: Optional[str] = None
    fiber_composition_pct: Dict[str, float]
    weave_type: WeaveType
    weight_gsm: float
    drape_coefficient: FabricDrapeCoefficient
    seasonality: SeasonalitySuitability
    breathability_index: float = Field(..., ge=0.0, le=100.0)
    moisture_regain_pct: float
    thermal_insulation_clo: float
    stretch_elasticity_pct: float = Field(default=0.0)
    shrinkage_potential_pct: float = Field(default=2.0)
    care_instructions: List[str]
    suitable_silhouettes: List[str]
    sustainable_rating: int = Field(..., ge=1, le=5)
    fabric_origin: str


FABRIC_DATABASE: Dict[str, FabricSpecification] = {
    "mulberry_silk_charmeuse": FabricSpecification(
        name="Mulberry Silk Charmeuse",
        fiber_category=FiberCategory.NATURAL_PROTEIN,
        primary_fiber="Mulberry Silk",
        fiber_composition_pct={"Mulberry Silk": 100.0},
        weave_type=WeaveType.SATIN_WEAVE,
        weight_gsm=82.0,
        drape_coefficient=FabricDrapeCoefficient.EXTRA_FLUID,
        seasonality=SeasonalitySuitability.ALL_WEATHER_TRANSITIONAL,
        breathability_index=85.0,
        moisture_regain_pct=11.0,
        thermal_insulation_clo=0.35,
        stretch_elasticity_pct=2.0,
        shrinkage_potential_pct=3.0,
        care_instructions=[
            "Dry clean professionally or hand wash in cold water with pH-neutral silk detergent",
            "Do not wring or twist; press out water between clean cotton towels",
            "Dry flat in shade away from direct sunlight",
            "Iron on reverse using lowest silk setting with steam cloth"
        ],
        suitable_silhouettes=["Bias-cut slip dress", "Draped cowl neck blouse", "Luxury evening gown", "Fluid pajama set"],
        sustainable_rating=4,
        fabric_origin="Varanasi & Karnataka, India"
    ),
    "pure_belgian_linen": FabricSpecification(
        name="Pure Belgian Flax Linen",
        fiber_category=FiberCategory.NATURAL_CELLULOSIC,
        primary_fiber="Flax Linen",
        fiber_composition_pct={"Flax Linen": 100.0},
        weave_type=WeaveType.PLAIN_WEAVE,
        weight_gsm=165.0,
        drape_coefficient=FabricDrapeCoefficient.MODERATE_DRAPE,
        seasonality=SeasonalitySuitability.PEAK_SUMMER,
        breathability_index=98.0,
        moisture_regain_pct=12.0,
        thermal_insulation_clo=0.20,
        stretch_elasticity_pct=0.5,
        shrinkage_potential_pct=4.5,
        care_instructions=[
            "Machine wash warm on gentle cycle using mild detergent without optical brighteners",
            "Tumble dry low or line dry in gentle breeze",
            "Iron while damp on high linen setting for crisp finish, or leave un-ironed for relaxed natural aesthetic"
        ],
        suitable_silhouettes=["Mandarin collar shirt", "Tailored relaxed trousers", "Summer blazer", "Resort tunic", "A-line midi dress"],
        sustainable_rating=5,
        fabric_origin="Flanders, Belgium"
    ),
    "egyptian_giza_cotton_poplin": FabricSpecification(
        name="Giza 88 Egyptian Cotton Poplin",
        fiber_category=FiberCategory.NATURAL_CELLULOSIC,
        primary_fiber="Extra-Long Staple Cotton",
        fiber_composition_pct={"ELS Cotton": 100.0},
        weave_type=WeaveType.PLAIN_WEAVE,
        weight_gsm=125.0,
        drape_coefficient=FabricDrapeCoefficient.MODERATE_DRAPE,
        seasonality=SeasonalitySuitability.ALL_WEATHER_TRANSITIONAL,
        breathability_index=92.0,
        moisture_regain_pct=8.5,
        thermal_insulation_clo=0.25,
        stretch_elasticity_pct=1.0,
        shrinkage_potential_pct=2.0,
        care_instructions=[
            "Machine wash at 40°C with similar colors",
            "Tumble dry medium",
            "Warm iron with steam for pristine crisp collar and cuffs"
        ],
        suitable_silhouettes=["Crisp Oxford shirt", "Tailored business shirt", "Structured shirt dress", "Tiered summer sundress"],
        sustainable_rating=4,
        fabric_origin="Nile River Delta, Egypt"
    ),
    "japanese_selvedge_raw_denim": FabricSpecification(
        name="Kuroki Japanese Selvedge Raw Denim (14.5oz)",
        fiber_category=FiberCategory.NATURAL_CELLULOSIC,
        primary_fiber="Zimbambwe Long Staple Cotton",
        fiber_composition_pct={"Cotton": 100.0},
        weave_type=WeaveType.TWILL_WEAVE,
        weight_gsm=490.0,
        drape_coefficient=FabricDrapeCoefficient.RIGID_SCULPTURAL,
        seasonality=SeasonalitySuitability.ALL_WEATHER_TRANSITIONAL,
        breathability_index=45.0,
        moisture_regain_pct=7.5,
        thermal_insulation_clo=0.65,
        stretch_elasticity_pct=0.0,
        shrinkage_potential_pct=5.0,
        care_instructions=[
            "Wear continuously for 6 months prior to first wash to develop personalized honeycomb fades",
            "Hand wash inside out in cold tub with woolite dark or specialized denim wash",
            "Hang dry by hem in well-ventilated shade; never machine tumble dry"
        ],
        suitable_silhouettes=["Straight leg raw denim jeans", "Type III trucker jacket", "Heavyweight workshirt"],
        sustainable_rating=4,
        fabric_origin="Okayama, Japan"
    ),
    "tencel_lyocell_twill": FabricSpecification(
        name="Lenzing TENCEL™ Lyocell Twill",
        fiber_category=FiberCategory.REGENERATED_CELLULOSIC,
        primary_fiber="Lyocell",
        fiber_composition_pct={"TENCEL Lyocell": 100.0},
        weave_type=WeaveType.TWILL_WEAVE,
        weight_gsm=190.0,
        drape_coefficient=FabricDrapeCoefficient.FLUID,
        seasonality=SeasonalitySuitability.ALL_WEATHER_TRANSITIONAL,
        breathability_index=90.0,
        moisture_regain_pct=11.5,
        thermal_insulation_clo=0.30,
        stretch_elasticity_pct=2.5,
        shrinkage_potential_pct=2.0,
        care_instructions=[
            "Gentle machine wash cold with eco-friendly liquid detergent",
            "Line dry in shade to prevent fiber fibrillation",
            "Medium iron on reverse side"
        ],
        suitable_silhouettes=["Fluid wide-leg palazzo trousers", "Trench coat", "Wrap dress", "Camp collar shirt"],
        sustainable_rating=5,
        fabric_origin="Lenzing, Austria"
    ),
    "banarasi_kathan_silk_brocade": FabricSpecification(
        name="Banarasi Katan Silk Royal Zari Brocade",
        fiber_category=FiberCategory.SPECIALTY_METALLIC,
        primary_fiber="Pure Katan Silk",
        secondary_fiber="Electroplated Silver Zari",
        fiber_composition_pct={"Katan Silk": 82.0, "Metallic Zari": 18.0},
        weave_type=WeaveType.JACQUARD_WEAVE,
        weight_gsm=240.0,
        drape_coefficient=FabricDrapeCoefficient.STRUCTURED,
        seasonality=SeasonalitySuitability.ALL_WEATHER_TRANSITIONAL,
        breathability_index=60.0,
        moisture_regain_pct=9.0,
        thermal_insulation_clo=0.45,
        stretch_elasticity_pct=0.0,
        shrinkage_potential_pct=1.0,
        care_instructions=[
            "Strictly dry clean only by heritage luxury textile specialist",
            "Store wrapped in breathable muslin cotton fabric; do not use plastic bags",
            "Refold periodically along different lines to avoid permanent creasing of zari filaments"
        ],
        suitable_silhouettes=["Royal bridal lehenga", "Sherwani", "Heritage saree", "Structured festive jacket", "Kurta set"],
        sustainable_rating=4,
        fabric_origin="Varanasi, Uttar Pradesh, India"
    ),
    "mongolian_pure_cashmere": FabricSpecification(
        name="Grade-A Mongolian Cashmere Knit (2-Ply 12-Gauge)",
        fiber_category=FiberCategory.NATURAL_PROTEIN,
        primary_fiber="Cashmere Wool",
        fiber_composition_pct={"Cashmere": 100.0},
        weave_type=WeaveType.KNIT_SINGLE_JERSEY,
        weight_gsm=220.0,
        drape_coefficient=FabricDrapeCoefficient.FLUID,
        seasonality=SeasonalitySuitability.AUTUMN_WINTER,
        breathability_index=75.0,
        moisture_regain_pct=16.0,
        thermal_insulation_clo=1.20,
        stretch_elasticity_pct=25.0,
        shrinkage_potential_pct=3.0,
        care_instructions=[
            "Hand wash gently in lukewarm water with cashmere shampoo",
            "Do not wring; roll in towel to absorb excess water",
            "Dry flat horizontally on mesh drying rack away from heat sources",
            "De-pill occasionally with a natural cedar cashmere comb"
        ],
        suitable_silhouettes=["Crewneck sweater", "Turtleneck pullover", "Cashmere cardigan", "Travel wrap scarf"],
        sustainable_rating=4,
        fabric_origin="Inner Mongolia, Ulaanbaatar"
    ),
    "heavyweight_french_terry": FabricSpecification(
        name="Organic Heavyweight French Terry (450 GSM)",
        fiber_category=FiberCategory.NATURAL_CELLULOSIC,
        primary_fiber="Combed Organic Cotton",
        fiber_composition_pct={"Organic Cotton": 100.0},
        weave_type=WeaveType.KNIT_FRENCH_TERRY,
        weight_gsm=450.0,
        drape_coefficient=FabricDrapeCoefficient.STRUCTURED,
        seasonality=SeasonalitySuitability.AUTUMN_WINTER,
        breathability_index=65.0,
        moisture_regain_pct=8.0,
        thermal_insulation_clo=0.85,
        stretch_elasticity_pct=15.0,
        shrinkage_potential_pct=3.0,
        care_instructions=[
            "Machine wash cold inside out with like colors",
            "Do not bleach",
            "Hang dry or tumble dry low",
            "Warm iron if desired"
        ],
        suitable_silhouettes=["Oversized streetwear hoodie", "Drop-shoulder sweatshirt", "Heavyweight sweatpants"],
        sustainable_rating=5,
        fabric_origin="Coimbatore & Tirupur, India"
    )
}


class FabricScienceEngine:
    @staticmethod
    def get_fabric_by_id(fabric_id: str) -> Optional[FabricSpecification]:
        return FABRIC_DATABASE.get(fabric_id.lower().replace(" ", "_").replace("-", "_"))

    @staticmethod
    def analyze_weather_compatibility(fabric_id: str, temperature_c: float, humidity_pct: float) -> Dict[str, Any]:
        spec = FabricScienceEngine.get_fabric_by_id(fabric_id)
        if not spec:
            return {"compatibility_score": 75.0, "reason": "Standard fabric"}

        score = 100.0
        reasons = []

        if temperature_c > 30.0:
            if spec.breathability_index < 70.0:
                score -= 30.0
                reasons.append("Low breathability may cause overheating in high temperatures.")
            if spec.weight_gsm > 200.0:
                score -= 25.0
                reasons.append("Heavyweight fabric is unsuited for warm climates.")
            if spec.moisture_regain_pct > 10.0:
                score += 10.0
                reasons.append("High natural moisture absorption keeps body cool.")
        elif temperature_c < 15.0:
            if spec.thermal_insulation_clo < 0.5:
                score -= 30.0
                reasons.append("Low thermal insulation requires heavy external layering in cold weather.")
            if spec.thermal_insulation_clo >= 0.8:
                score += 15.0
                reasons.append("Superior natural thermal insulation provides excellent warmth.")

        if humidity_pct > 70.0:
            if spec.fiber_category == FiberCategory.SYNTHETIC_POLYMER:
                score -= 20.0
                reasons.append("Synthetics trap moisture and heat in humid climates.")
            if spec.fiber_category in [FiberCategory.NATURAL_CELLULOSIC, FiberCategory.REGENERATED_CELLULOSIC]:
                score += 10.0
                reasons.append("Cellulosic fibers allow rapid evaporative cooling in humid environments.")

        final_score = max(10.0, min(100.0, score))
        return {
            "fabric_name": spec.name,
            "temperature_c": temperature_c,
            "humidity_pct": humidity_pct,
            "compatibility_score": round(final_score, 1),
            "is_recommended": final_score >= 70.0,
            "analysis_notes": reasons
        }

    @staticmethod
    def get_layering_compatibility(base_fabric_id: str, outer_fabric_id: str) -> Dict[str, Any]:
        base = FabricScienceEngine.get_fabric_by_id(base_fabric_id)
        outer = FabricScienceEngine.get_fabric_by_id(outer_fabric_id)

        if not base or not outer:
            return {"compatible": True, "score": 80.0, "note": "Standard layering pair"}

        score = 85.0
        notes = []

        if base.weight_gsm > outer.weight_gsm * 1.2:
            score -= 25.0
            notes.append(f"Base layer ({base.name} @ {base.weight_gsm} GSM) is heavier than outer layer ({outer.name} @ {outer.weight_gsm} GSM), creating bunching.")
        else:
            score += 10.0
            notes.append("Ideal weight progression from lighter base to structured outer.")

        if base.drape_coefficient == FabricDrapeCoefficient.RIGID_SCULPTURAL and outer.drape_coefficient == FabricDrapeCoefficient.EXTRA_FLUID:
            score -= 20.0
            notes.append("Rigid inner fabric overpowers delicate fluid outer drape.")

        return {
            "base_layer": base.name,
            "outer_layer": outer.name,
            "layering_score": max(20.0, min(100.0, score)),
            "is_harmonious": score >= 70.0,
            "reasons": notes
        }
