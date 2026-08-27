"""
Garment Ease Matrix and 3D Anthropometric Geometry Engine.
Calculates minimum functional movement ease, design volume ease,
and elastane stretch compression offsets across 20+ silhouette archetypes.
"""

from typing import Dict, List, Optional, Any, Tuple
from pydantic import BaseModel, Field
from enum import Enum


class EaseCategory(str, Enum):
    NEGATIVE_EASE = "NEGATIVE_EASE"        # -2.0 to -0.5 inches (Swimwear, shapewear, compression knits)
    ZERO_EASE = "ZERO_EASE"                # 0.0 to 0.5 inches (Corsetry, tailored bustiers)
    SLIM_TAILORED = "SLIM_TAILORED"        # 1.0 to 2.5 inches (Fitted dress shirts, tailored blazers)
    REGULAR_CLASSIC = "REGULAR_CLASSIC"    # 2.5 to 4.5 inches (Standard business shirts, chinos)
    RELAXED_CASUAL = "RELAXED_CASUAL"      # 4.5 to 6.5 inches (Camp collar shirts, relaxed trousers)
    OVERSIZED_BOXY = "OVERSIZED_BOXY"      # 6.5 to 10.0 inches (Drop-shoulder hoodies, boxy tees)
    VOLUMINOUS_DRAMATIC = "VOLUMINOUS"     # 10.0+ inches (Cape coats, cocoon trenches, voluminous gowns)


class EaseMeasurementProfile(BaseModel):
    silhouette_id: str
    ease_category: EaseCategory
    chest_ease_in: float
    waist_ease_in: float
    hip_ease_in: float
    bicep_ease_in: float
    thigh_ease_in: float
    wrist_ease_in: float
    shoulder_drop_in: float


EASE_PROFILES: Dict[str, EaseMeasurementProfile] = {
    "tailored_oxford_shirt": EaseMeasurementProfile(
        silhouette_id="tailored_oxford_shirt",
        ease_category=EaseCategory.SLIM_TAILORED,
        chest_ease_in=2.5,
        waist_ease_in=2.0,
        hip_ease_in=2.5,
        bicep_ease_in=1.5,
        thigh_ease_in=0.0,
        wrist_ease_in=1.0,
        shoulder_drop_in=0.0
    ),
    "oversized_hoodie": EaseMeasurementProfile(
        silhouette_id="oversized_hoodie",
        ease_category=EaseCategory.OVERSIZED_BOXY,
        chest_ease_in=8.0,
        waist_ease_in=9.0,
        hip_ease_in=8.0,
        bicep_ease_in=4.0,
        thigh_ease_in=0.0,
        wrist_ease_in=2.0,
        shoulder_drop_in=3.5
    ),
    "pleated_wide_leg_trouser": EaseMeasurementProfile(
        silhouette_id="pleated_wide_leg_trouser",
        ease_category=EaseCategory.RELAXED_CASUAL,
        chest_ease_in=0.0,
        waist_ease_in=0.75,
        hip_ease_in=5.5,
        bicep_ease_in=0.0,
        thigh_ease_in=6.0,
        wrist_ease_in=0.0,
        shoulder_drop_in=0.0
    )
}
