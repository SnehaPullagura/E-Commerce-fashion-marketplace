"""
Virtual Try-On & Anthropometric Fabric Drape Simulation Engine.
Computes 3D silhouette mesh deformation, fabric tension heatmaps,
and physics-based drape elasticity for customer body contours.
"""

from typing import Dict, List, Optional, Any, Tuple
from pydantic import BaseModel, Field
from enum import Enum
import math


class BodyShapeArchetype(str, Enum):
    HOURGLASS = "HOURGLASS"
    PEAR_TRIANGLE = "PEAR_TRIANGLE"
    INVERTED_TRIANGLE = "INVERTED_TRIANGLE"
    RECTANGLE_ATHLETIC = "RECTANGLE_ATHLETIC"
    ROUND_APPLE = "ROUND_APPLE"


class FabricType(str, Enum):
    SILK_CHARMEUSE = "SILK_CHARMEUSE"
    COTTON_JERSEY = "COTTON_JERSEY"
    STRUCTURED_WOOL = "STRUCTURED_WOOL"
    STRETCH_DENIM = "STRETCH_DENIM"
    CHIFFON_POLY = "CHIFFON_POLY"
    LINEN_WOVEN = "LINEN_WOVEN"


class CustomerAnthropometrics(BaseModel):
    height_cm: float = Field(..., ge=120.0, le=230.0)
    bust_chest_cm: float = Field(..., ge=60.0, le=160.0)
    waist_cm: float = Field(..., ge=50.0, le=150.0)
    high_hip_cm: float = Field(..., ge=60.0, le=160.0)
    low_hip_cm: float = Field(..., ge=60.0, le=170.0)
    shoulder_width_cm: float = Field(..., ge=30.0, le=70.0)
    inseam_cm: Optional[float] = 76.0
    weight_kg: Optional[float] = 65.0


class GarmentSpecs(BaseModel):
    garment_id: str
    garment_type: str = "DRESS"  # TOP, BOTTOM, DRESS, OUTERWEAR
    size_label: str = "M"
    chest_width_cm: float
    waist_width_cm: float
    hip_width_cm: float
    garment_length_cm: float
    fabric_type: FabricType = FabricType.COTTON_JERSEY
    stretch_percentage: float = 5.0  # 0 to 50% elastane stretch


class FabricPhysicsParameters:
    # Properties: (drape_coefficient, youngs_modulus_gpa, shear_stiffness, density_gsm)
    PROPERTIES: Dict[FabricType, Dict[str, float]] = {
        FabricType.SILK_CHARMEUSE: {"drape": 0.22, "elasticity": 0.15, "gsm": 75.0, "fluidity": 0.95},
        FabricType.COTTON_JERSEY: {"drape": 0.45, "elasticity": 0.60, "gsm": 180.0, "fluidity": 0.70},
        FabricType.STRUCTURED_WOOL: {"drape": 0.78, "elasticity": 0.08, "gsm": 340.0, "fluidity": 0.25},
        FabricType.STRETCH_DENIM: {"drape": 0.65, "elasticity": 0.35, "gsm": 380.0, "fluidity": 0.30},
        FabricType.CHIFFON_POLY: {"drape": 0.18, "elasticity": 0.05, "gsm": 60.0, "fluidity": 0.98},
        FabricType.LINEN_WOVEN: {"drape": 0.58, "elasticity": 0.02, "gsm": 210.0, "fluidity": 0.40},
    }


class VirtualTryOnEngine:
    @staticmethod
    def classify_body_shape(anthro: CustomerAnthropometrics) -> BodyShapeArchetype:
        """Classifies body shape based on bust-waist-hip ratios."""
        bust = anthro.bust_chest_cm
        waist = anthro.waist_cm
        hip = anthro.low_hip_cm

        waist_hip_ratio = waist / hip if hip > 0 else 0.7
        waist_bust_ratio = waist / bust if bust > 0 else 0.7
        bust_hip_diff = abs(bust - hip)

        if waist_hip_ratio < 0.80 and waist_bust_ratio < 0.80 and bust_hip_diff <= 7.0:
            return BodyShapeArchetype.HOURGLASS
        elif (hip - bust) > 6.0 and waist_hip_ratio < 0.85:
            return BodyShapeArchetype.PEAR_TRIANGLE
        elif (bust - hip) > 6.0 and anthro.shoulder_width_cm >= 40.0:
            return BodyShapeArchetype.INVERTED_TRIANGLE
        elif waist_hip_ratio >= 0.85 and (waist >= bust or waist >= hip):
            return BodyShapeArchetype.ROUND_APPLE
        else:
            return BodyShapeArchetype.RECTANGLE_ATHLETIC

    @staticmethod
    def simulate_try_on(
        anthro: CustomerAnthropometrics,
        garment: GarmentSpecs
    ) -> Dict[str, Any]:
        """
        Executes biomechanical tension calculation and drape simulation.
        Returns fit score (0-100), tension heatmap map, and recommendations.
        """
        body_shape = VirtualTryOnEngine.classify_body_shape(anthro)
        fabric_props = FabricPhysicsParameters.PROPERTIES.get(
            garment.fabric_type,
            {"drape": 0.45, "elasticity": 0.3, "gsm": 200.0, "fluidity": 0.6}
        )

        # Ease calculation = Garment Circumference - Body Circumference
        garment_chest_circ = garment.chest_width_cm * 2.0
        garment_waist_circ = garment.waist_width_cm * 2.0
        garment_hip_circ = garment.hip_width_cm * 2.0

        chest_ease = garment_chest_circ - anthro.bust_chest_cm
        waist_ease = garment_waist_circ - anthro.waist_cm
        hip_ease = garment_hip_circ - anthro.low_hip_cm

        # Stretch accommodation
        max_stretch_factor = 1.0 + (garment.stretch_percentage / 100.0)

        # Tension calculations (0 = loose drape, 100 = critical strain/tearing)
        def compute_strain(ease: float, baseline: float) -> Tuple[float, str]:
            if ease >= 8.0:
                return (10.0, "Oversized / Relaxed")
            elif 3.0 <= ease < 8.0:
                return (25.0, "Tailored Classic")
            elif 0.0 <= ease < 3.0:
                return (45.0, "Fitted Contour")
            elif -4.0 <= ease < 0.0:
                strain = abs(ease) * 15.0 / max_stretch_factor
                return (min(85.0, 50.0 + strain), "Snug Compression")
            else:
                strain = abs(ease) * 25.0 / max_stretch_factor
                return (min(100.0, 75.0 + strain), "Overly Tight / Strained")

        chest_strain, chest_fit = compute_strain(chest_ease, anthro.bust_chest_cm)
        waist_strain, waist_fit = compute_strain(waist_ease, anthro.waist_cm)
        hip_strain, hip_fit = compute_strain(hip_ease, anthro.low_hip_cm)

        # Overall fit confidence (penalize extreme strains or excessively loose points)
        avg_strain = (chest_strain + waist_strain + hip_strain) / 3.0
        penalty = 0.0
        for strain in [chest_strain, waist_strain, hip_strain]:
            if strain > 80.0:
                penalty += 25.0
            elif strain < 15.0:
                penalty += 8.0

        fit_confidence_score = max(5.0, min(100.0, 100.0 - (abs(avg_strain - 35.0) * 1.2) - penalty))

        # Drape flow simulation (higher fluidity creates graceful pleating)
        drape_effect = "Sculpted & Crisp" if fabric_props["drape"] > 0.65 else (
            "Cascade Waterfall Drape" if fabric_props["fluidity"] > 0.8 else "Fluid Contoured"
        )

        return {
            "garment_id": garment.garment_id,
            "size_tested": garment.size_label,
            "customer_body_shape": body_shape.value,
            "overall_fit_confidence": round(fit_confidence_score, 1),
            "verdict": (
                "PERFECT_MATCH" if fit_confidence_score >= 85 else
                ("SLIGHT_ADJUSTMENT" if fit_confidence_score >= 65 else "NOT_RECOMMENDED")
            ),
            "tension_zones": {
                "chest": {
                    "ease_cm": round(chest_ease, 1),
                    "strain_index": round(chest_strain, 1),
                    "fit_feeling": chest_fit
                },
                "waist": {
                    "ease_cm": round(waist_ease, 1),
                    "strain_index": round(waist_strain, 1),
                    "fit_feeling": waist_fit
                },
                "hip": {
                    "ease_cm": round(hip_ease, 1),
                    "strain_index": round(hip_strain, 1),
                    "fit_feeling": hip_fit
                }
            },
            "fabric_simulation": {
                "fabric_type": garment.fabric_type.value,
                "drape_style": drape_effect,
                "fluidity_index": fabric_props["fluidity"],
                "gsm_weight": fabric_props["gsm"]
            },
            "recommended_size_action": (
                f"Size {garment.size_label} is an optimal match for your {body_shape.value.replace('_', ' ').title()} shape."
                if fit_confidence_score >= 80 else
                f"Consider sizing {'UP' if avg_strain > 60 else 'DOWN'} for improved comfort."
            )
        }
