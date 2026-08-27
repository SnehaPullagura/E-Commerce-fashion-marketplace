"""
Haute Couture and Contemporary Silhouette Structural Taxonomy.
Defines precise geometric silhouettes, drape profiles, waistline placements,
hemline specifications, and garment volume metrics.
"""

from typing import Dict, List, Optional, Any
from enum import Enum
from pydantic import BaseModel, Field


class SilhouetteCategory(str, Enum):
    TOPWEAR = "TOPWEAR"
    BOTTOMWEAR = "BOTTOMWEAR"
    DRESSES_GOWNS = "DRESSES_GOWNS"
    OUTERWEAR_TAILORING = "OUTERWEAR_TAILORING"
    ETHNIC_HERITAGE = "ETHNIC_HERITAGE"
    FOOTWEAR = "FOOTWEAR"


class VolumeProfile(str, Enum):
    SECOND_SKIN = "SECOND_SKIN"
    FITTED = "FITTED"
    SEMI_FITTED = "SEMI_FITTED"
    STRAIGHT_BOX = "STRAIGHT_BOX"
    A_LINE_TRAPEZE = "A_LINE_TRAPEZE"
    HOURGLASS_PEPLUM = "HOURGLASS"
    OVERSIZED_COCOON = "OVERSIZED"
    BALLGOWN_VOLUMINOUS = "VOLUMINOUS"


class WaistPlacement(str, Enum):
    EMPIRE = "EMPIRE"
    HIGH_WAISTED = "HIGH_WAISTED"
    MID_RISE = "MID_RISE"
    LOW_RISE = "LOW_RISE"
    DROPPED_WAIST = "DROPPED_WAIST"


class HemlineLength(str, Enum):
    MICRO_MINI = "MICRO_MINI"
    ABOVE_KNEE = "ABOVE_KNEE"
    KNEE_LENGTH = "KNEE_LENGTH"
    MIDI_TEA_LENGTH = "MIDI_TEA"
    MAXI_ANKLE = "MAXI_ANKLE"
    FLOOR_LENGTH_TRAIN = "FLOOR_TRAIN"


class SilhouetteDefinition(BaseModel):
    id: str
    name: str
    category: SilhouetteCategory
    volume_profile: VolumeProfile
    waist_placement: Optional[WaistPlacement] = None
    hemline_length: Optional[HemlineLength] = None
    ease_allowance_inches: float
    ideal_body_types: List[str]
    style_personas: List[str]
    layering_role: str


SILHOUETTE_CATALOG: Dict[str, SilhouetteDefinition] = {
    "bias_cut_slip_dress": SilhouetteDefinition(
        id="bias_cut_slip_dress",
        name="Bias-Cut 90s Slip Dress",
        category=SilhouetteCategory.DRESSES_GOWNS,
        volume_profile=VolumeProfile.SEMI_FITTED,
        waist_placement=WaistPlacement.HIGH_WAISTED,
        hemline_length=HemlineLength.MIDI_TEA_LENGTH,
        ease_allowance_inches=1.5,
        ideal_body_types=["Hourglass", "Rectangle", "Petite", "Athletic"],
        style_personas=["Minimalist", "Chic", "Quiet Luxury", "90s Retro"],
        layering_role="STANDALONE"
    ),
    "mandarin_collar_shirt": SilhouetteDefinition(
        id="mandarin_collar_shirt",
        name="Slim-Tailored Mandarin Collar Shirt",
        category=SilhouetteCategory.TOPWEAR,
        volume_profile=VolumeProfile.FITTED,
        waist_placement=WaistPlacement.MID_RISE,
        hemline_length=HemlineLength.ABOVE_KNEE,
        ease_allowance_inches=2.5,
        ideal_body_types=["Athletic", "Lean", "Inverted Triangle", "Rectangle"],
        style_personas=["Sartorial", "Minimalist", "Smart Casual", "Resort"],
        layering_role="BASE_LAYER"
    ),
    "wide_leg_pleated_trousers": SilhouetteDefinition(
        id="wide_leg_pleated_trousers",
        name="High-Rise Double-Pleated Wide-Leg Trousers",
        category=SilhouetteCategory.BOTTOMWEAR,
        volume_profile=VolumeProfile.A_LINE_TRAPEZE,
        waist_placement=WaistPlacement.HIGH_WAISTED,
        hemline_length=HemlineLength.FLOOR_LENGTH_TRAIN,
        ease_allowance_inches=6.0,
        ideal_body_types=["Pear", "Hourglass", "Tall", "Rectangle"],
        style_personas=["Old Money", "Quiet Luxury", "Power Dressing", "Parisian Chic"],
        layering_role="STANDALONE"
    ),
    "oversized_heavyweight_hoodie": SilhouetteDefinition(
        id="oversized_heavyweight_hoodie",
        name="Boxy Drop-Shoulder Heavyweight Hoodie",
        category=SilhouetteCategory.OUTERWEAR_TAILORING,
        volume_profile=VolumeProfile.OVERSIZED_COCOON,
        waist_placement=WaistPlacement.DROPPED_WAIST,
        hemline_length=HemlineLength.MID_RISE,
        ease_allowance_inches=8.5,
        ideal_body_types=["All Body Types"],
        style_personas=["Streetwear", "Urban", "Cyberpunk", "Athleisure"],
        layering_role="OUTERWEAR"
    ),
    "royal_kalidar_anarkali": SilhouetteDefinition(
        id="royal_kalidar_anarkali",
        name="Heritage 32-Kali Royal Anarkali Set",
        category=SilhouetteCategory.ETHNIC_HERITAGE,
        volume_profile=VolumeProfile.BALLGOWN_VOLUMINOUS,
        waist_placement=WaistPlacement.EMPIRE,
        hemline_length=HemlineLength.FLOOR_LENGTH_TRAIN,
        ease_allowance_inches=4.0,
        ideal_body_types=["Hourglass", "Pear", "Round", "Inverted Triangle"],
        style_personas=["Royal Festive", "Bridal", "Heritage Ethnic"],
        layering_role="STANDALONE"
    )
}
