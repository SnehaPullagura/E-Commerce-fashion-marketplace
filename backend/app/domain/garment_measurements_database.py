"""
Comprehensive Garment Anthropometric Measurement & Grading Specification Database.
Defines grade increments, tolerance thresholds, and dimensional specifications
for standard fashion silhouettes across international sizes (XXS to 3XL).
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field


class GarmentSizeSpec(BaseModel):
    size_label: str
    chest_circumference_in: float
    waist_circumference_in: float
    hip_circumference_in: float
    garment_length_in: float
    shoulder_width_in: float
    sleeve_length_in: float
    bicep_circumference_in: float
    neck_circumference_in: float
    tolerance_margin_in: float = 0.5


class SilhouetteGradingChart(BaseModel):
    silhouette_code: str
    silhouette_name: str
    gender: str
    category: str
    fit_type: str
    sizes: Dict[str, GarmentSizeSpec]


def _build_graded_sizes(
    base_chest: float,
    base_waist: float,
    base_hip: float,
    base_len: float,
    chest_step: float = 2.0
) -> Dict[str, GarmentSizeSpec]:
    labels = ["XXS", "XS", "S", "M", "L", "XL", "2XL", "3XL"]
    sizes = {}
    for idx, lbl in enumerate(labels):
        offset = (idx - 3) * chest_step  # M is index 3
        sizes[lbl] = GarmentSizeSpec(
            size_label=lbl,
            chest_circumference_in=round(base_chest + offset, 1),
            waist_circumference_in=round(base_waist + offset, 1),
            hip_circumference_in=round(base_hip + offset, 1),
            garment_length_in=round(base_len + (idx * 0.5), 1),
            shoulder_width_in=round(16.0 + (idx * 0.4), 1),
            sleeve_length_in=round(24.0 + (idx * 0.3), 1),
            bicep_circumference_in=round(13.5 + (idx * 0.4), 1),
            neck_circumference_in=round(14.5 + (idx * 0.3), 1),
            tolerance_margin_in=0.5
        )
    return sizes


SILHOUETTE_DEFINITIONS = [
    ("SIL_SLIM_SHIRT", "Tailored European Dress Shirt", "MEN", "TOPS", "SLIM", 38.0, 32.0, 38.0, 30.0, 2.0),
    ("SIL_OVERSIZE_HOODIE", "Heavyweight Drop-Shoulder Hoodie", "UNISEX", "OUTERWEAR", "OVERSIZED", 44.0, 42.0, 44.0, 28.0, 2.5),
    ("SIL_TAILORED_BLAZER", "Single-Breasted Italian Structured Blazer", "MEN", "OUTERWEAR", "REGULAR", 40.0, 34.0, 40.0, 30.5, 2.0),
    ("SIL_ANARKALI_GOWN", "Flared Floor-Length Festive Anarkali", "WOMEN", "ETHNIC", "FLARED", 36.0, 30.0, 42.0, 54.0, 2.0),
    ("SIL_CIGARETTE_TROUSER", "High-Waist Tapered Ankle Trouser", "WOMEN", "BOTTOMS", "SLIM", 34.0, 28.0, 38.0, 37.0, 2.0),
    ("SIL_KURTA_BANDGALA", "Structured Royal Bandgala Jodhpur Kurta", "MEN", "ETHNIC", "TAILORED", 39.0, 33.0, 40.0, 42.0, 2.0),
]

GARMENT_MEASUREMENT_DATABASE: Dict[str, SilhouetteGradingChart] = {
    code: SilhouetteGradingChart(
        silhouette_code=code,
        silhouette_name=name,
        gender=gender,
        category=cat,
        fit_type=fit,
        sizes=_build_graded_sizes(chest, waist, hip, length, step)
    )
    for code, name, gender, cat, fit, chest, waist, hip, length, step in SILHOUETTE_DEFINITIONS
}
