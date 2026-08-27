"""
Advanced Size & Fit Intelligence Engine.
Computes multi-dimensional body fit predictions, ease allowances,
brand vanity sizing compensation, and international sizing conversion matrix.
"""

from typing import Dict, List, Optional, Tuple, Any
from pydantic import BaseModel, Field
from enum import Enum


class FitGrade(str, Enum):
    PERFECT_FIT = "PERFECT_FIT"
    TAILORED_FITTED = "TAILORED_FITTED"
    COMFORT_RELAXED = "COMFORT_RELAXED"
    RUNS_TIGHT = "RUNS_TIGHT"
    RUNS_LOOSE = "RUNS_LOOSE"


class SizingRegion(str, Enum):
    INTERNATIONAL = "INT"
    US = "US"
    UK = "UK"
    EU = "EU"
    IT = "IT"
    FR = "FR"
    JP = "JP"
    IN = "IN"


INTERNATIONAL_SIZE_CONVERSION_TABLE: Dict[str, Dict[str, str]] = {
    "XS": {"US_WOMEN": "0-2", "UK_WOMEN": "4-6", "EU_WOMEN": "32-34", "US_MEN": "34", "EU_MEN": "44", "IN": "36"},
    "S":  {"US_WOMEN": "4-6", "UK_WOMEN": "8-10", "EU_WOMEN": "36-38", "US_MEN": "36-38", "EU_MEN": "46-48", "IN": "38"},
    "M":  {"US_WOMEN": "8-10", "UK_WOMEN": "12-14", "EU_WOMEN": "40-42", "US_MEN": "40", "EU_MEN": "50", "IN": "40"},
    "L":  {"US_WOMEN": "12-14", "UK_WOMEN": "16-18", "EU_WOMEN": "44-46", "US_MEN": "42-44", "EU_MEN": "52-54", "IN": "42"},
    "XL": {"US_WOMEN": "16-18", "UK_WOMEN": "20-22", "EU_WOMEN": "48-50", "US_MEN": "46-48", "EU_MEN": "56-58", "IN": "44"},
    "XXL":{"US_WOMEN": "20+", "UK_WOMEN": "24+", "EU_WOMEN": "52+", "US_MEN": "50-52", "EU_MEN": "60-62", "IN": "46"}
}


class AnthropometricPredictor:
    @staticmethod
    def estimate_body_dimensions(height_cm: float, weight_kg: float, gender: str) -> Dict[str, float]:
        height_m = height_cm / 100.0
        bmi = weight_kg / (height_m * height_m)

        if gender.upper() == "MEN":
            chest_in = 30.0 + (bmi * 0.45) + (height_cm * 0.05)
            waist_in = chest_in - 6.5
            hip_in = waist_in + 4.0
            shoulder_in = 14.0 + (chest_in * 0.12)
        else:
            bust_in = 28.0 + (bmi * 0.48) + (height_cm * 0.04)
            waist_in = bust_in - 8.0
            hip_in = waist_in + 9.5
            shoulder_in = 12.5 + (bust_in * 0.10)
            chest_in = bust_in

        return {
            "estimated_chest_in": round(chest_in, 1),
            "estimated_waist_in": round(waist_in, 1),
            "estimated_hips_in": round(hip_in, 1),
            "estimated_shoulder_in": round(shoulder_in, 1),
            "calculated_bmi": round(bmi, 1)
        }


class SizeIntelligenceEvaluator:
    @staticmethod
    def evaluate_fit(
        garment_measurements: Dict[str, float],
        customer_chest_in: float,
        customer_waist_in: Optional[float] = None,
        fit_preference: str = "REGULAR",
        fabric_stretch_pct: float = 0.0
    ) -> Dict[str, Any]:
        garment_chest = garment_measurements.get("chest_max", garment_measurements.get("chest_min", 40.0))
        ease_delta = garment_chest - customer_chest_in

        if fit_preference == "SLIM":
            target_min_ease = 1.0 - (fabric_stretch_pct * 0.05)
            target_max_ease = 2.5
        elif fit_preference == "OVERSIZED":
            target_min_ease = 5.0
            target_max_ease = 10.0
        else:
            target_min_ease = 2.5 - (fabric_stretch_pct * 0.03)
            target_max_ease = 4.5

        if target_min_ease <= ease_delta <= target_max_ease:
            confidence = 0.96
            grade = FitGrade.PERFECT_FIT
            rationale = f"Ideal {fit_preference.lower()} ease of {ease_delta:.1f} inches across the chest."
        elif ease_delta < target_min_ease:
            if ease_delta < 0.0 and fabric_stretch_pct < 5.0:
                confidence = 0.40
                grade = FitGrade.RUNS_TIGHT
                rationale = f"Garment chest is smaller than body measurement ({garment_chest} in vs {customer_chest_in} in) without sufficient stretch."
            else:
                confidence = 0.75
                grade = FitGrade.TAILORED_FITTED
                rationale = f"Snug tailored fit with {ease_delta:.1f} inches ease."
        else:
            confidence = 0.80
            grade = FitGrade.COMFORT_RELAXED
            rationale = f"Relaxed roomy silhouette with {ease_delta:.1f} inches ease."

        return {
            "fit_grade": grade.value,
            "confidence_score": confidence,
            "ease_delta_inches": round(ease_delta, 1),
            "fit_analysis": rationale
        }
