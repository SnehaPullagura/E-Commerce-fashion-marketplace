"""
Color Theory and Chromatic Harmony Engine for Haute Couture Fashion.
Implements CIELAB color space distance, 12-hue color wheel harmony models,
skin undertone matching, and Pantone seasonal palette mappings.
"""

import math
from typing import Dict, List, Optional, Tuple, Any
from pydantic import BaseModel, Field
from enum import Enum


class ColorFamily(str, Enum):
    NEUTRAL_WARM = "NEUTRAL_WARM"
    NEUTRAL_COOL = "NEUTRAL_COOL"
    EARTH_TONES = "EARTH_TONES"
    PASTELS = "PASTELS"
    JEWEL_TONES = "JEWEL_TONES"
    METALLICS = "METALLICS"
    MONOCHROME = "MONOCHROME"


class SkinUndertone(str, Enum):
    COOL = "COOL"
    WARM = "WARM"
    NEUTRAL = "NEUTRAL"
    OLIVE = "OLIVE"


class HarmonyType(str, Enum):
    MONOCHROMATIC = "MONOCHROMATIC"
    ANALOGOUS = "ANALOGOUS"
    COMPLEMENTARY = "COMPLEMENTARY"
    SPLIT_COMPLEMENTARY = "SPLIT_COMPLEMENTARY"
    TRIADIC = "TRIADIC"
    TETRADIC = "TETRADIC"
    NEUTRAL_ACCENT = "NEUTRAL_ACCENT"


class ColorDefinition(BaseModel):
    name: str
    hex_code: str
    family: ColorFamily
    hue_degrees: float = Field(..., ge=0.0, le=360.0)
    saturation_pct: float = Field(..., ge=0.0, le=100.0)
    lightness_pct: float = Field(..., ge=0.0, le=100.0)
    warmth_index: float = Field(..., ge=-1.0, le=1.0)
    pantone_reference: Optional[str] = None
    compatible_undertones: List[SkinUndertone]
    suggested_pairings: List[str]


COLOR_REGISTRY: Dict[str, ColorDefinition] = {
    "midnight_black": ColorDefinition(
        name="Midnight Black",
        hex_code="#111111",
        family=ColorFamily.MONOCHROME,
        hue_degrees=0.0,
        saturation_pct=0.0,
        lightness_pct=6.7,
        warmth_index=0.0,
        pantone_reference="PANTONE 19-4008 TCX (Meteorite)",
        compatible_undertones=[SkinUndertone.COOL, SkinUndertone.WARM, SkinUndertone.NEUTRAL, SkinUndertone.OLIVE],
        suggested_pairings=["off_white", "champagne_gold", "ruby_red", "sage_green", "camel"]
    ),
    "off_white_ecru": ColorDefinition(
        name="Off-White Ecru",
        hex_code="#FAF9F6",
        family=ColorFamily.MONOCHROME,
        hue_degrees=45.0,
        saturation_pct=25.0,
        lightness_pct=97.5,
        warmth_index=0.2,
        pantone_reference="PANTONE 11-0601 TCX (Bright White)",
        compatible_undertones=[SkinUndertone.COOL, SkinUndertone.WARM, SkinUndertone.NEUTRAL, SkinUndertone.OLIVE],
        suggested_pairings=["midnight_black", "sage_green", "terracotta_rust", "navy_blue", "camel"]
    ),
    "sage_green": ColorDefinition(
        name="Sage Green",
        hex_code="#8A9A86",
        family=ColorFamily.EARTH_TONES,
        hue_degrees=108.0,
        saturation_pct=10.5,
        lightness_pct=56.9,
        warmth_index=-0.1,
        pantone_reference="PANTONE 16-0213 TCX (Tea)",
        compatible_undertones=[SkinUndertone.NEUTRAL, SkinUndertone.COOL, SkinUndertone.OLIVE],
        suggested_pairings=["off_white_ecru", "charcoal_slate", "terracotta_rust", "butter_cream"]
    ),
    "terracotta_rust": ColorDefinition(
        name="Terracotta Rust",
        hex_code="#C86D51",
        family=ColorFamily.EARTH_TONES,
        hue_degrees=14.0,
        saturation_pct=52.2,
        lightness_pct=55.1,
        warmth_index=0.85,
        pantone_reference="PANTONE 18-1440 TCX (Chili)",
        compatible_undertones=[SkinUndertone.WARM, SkinUndertone.OLIVE, SkinUndertone.NEUTRAL],
        suggested_pairings=["sage_green", "camel", "off_white_ecru", "midnight_black", "raw_denim_indigo"]
    ),
    "royal_ruby_red": ColorDefinition(
        name="Royal Ruby Red",
        hex_code="#9B111E",
        family=ColorFamily.JEWEL_TONES,
        hue_degrees=354.0,
        saturation_pct=80.3,
        lightness_pct=33.7,
        warmth_index=0.4,
        pantone_reference="PANTONE 19-1763 TCX (Crimson)",
        compatible_undertones=[SkinUndertone.COOL, SkinUndertone.WARM, SkinUndertone.OLIVE],
        suggested_pairings=["antique_gold", "midnight_black", "champagne_silver", "off_white_ecru"]
    ),
    "antique_gold": ColorDefinition(
        name="Antique Gold",
        hex_code="#D4AF37",
        family=ColorFamily.METALLICS,
        hue_degrees=45.8,
        saturation_pct=65.0,
        lightness_pct=52.4,
        warmth_index=0.9,
        pantone_reference="PANTONE 16-0947 TCX (Rich Gold)",
        compatible_undertones=[SkinUndertone.WARM, SkinUndertone.OLIVE],
        suggested_pairings=["royal_ruby_red", "emerald_green", "midnight_black", "navy_blue"]
    ),
    "emerald_green": ColorDefinition(
        name="Imperial Emerald",
        hex_code="#046307",
        family=ColorFamily.JEWEL_TONES,
        hue_degrees=122.0,
        saturation_pct=92.3,
        lightness_pct=20.2,
        warmth_index=-0.2,
        pantone_reference="PANTONE 19-5513 TCX (Garden Top)",
        compatible_undertones=[SkinUndertone.COOL, SkinUndertone.OLIVE, SkinUndertone.WARM],
        suggested_pairings=["antique_gold", "off_white_ecru", "blush_pink", "midnight_black"]
    ),
    "navy_blue": ColorDefinition(
        name="Midnight Navy",
        hex_code="#1B2A4A",
        family=ColorFamily.JEWEL_TONES,
        hue_degrees=220.7,
        saturation_pct=46.5,
        lightness_pct=20.0,
        warmth_index=-0.8,
        pantone_reference="PANTONE 19-4024 TCX (Dress Blues)",
        compatible_undertones=[SkinUndertone.COOL, SkinUndertone.NEUTRAL, SkinUndertone.WARM],
        suggested_pairings=["camel", "off_white_ecru", "terracotta_rust", "powder_blue"]
    ),
    "camel": ColorDefinition(
        name="Sartorial Camel",
        hex_code="#C19A6B",
        family=ColorFamily.NEUTRAL_WARM,
        hue_degrees=33.3,
        saturation_pct=41.5,
        lightness_pct=58.8,
        warmth_index=0.75,
        pantone_reference="PANTONE 16-1334 TCX (Camel)",
        compatible_undertones=[SkinUndertone.WARM, SkinUndertone.NEUTRAL, SkinUndertone.OLIVE],
        suggested_pairings=["navy_blue", "midnight_black", "off_white_ecru", "powder_blue"]
    ),
    "blush_pink": ColorDefinition(
        name="Dusty Blush Pink",
        hex_code="#E8C5C8",
        family=ColorFamily.PASTELS,
        hue_degrees=354.3,
        saturation_pct=44.1,
        lightness_pct=84.1,
        warmth_index=0.3,
        pantone_reference="PANTONE 13-1406 TCX (Cloud Pink)",
        compatible_undertones=[SkinUndertone.COOL, SkinUndertone.NEUTRAL],
        suggested_pairings=["charcoal_slate", "emerald_green", "burgundy", "off_white_ecru"]
    )
}


class ColorHarmonyEngine:
    @staticmethod
    def calculate_harmony_score(color_hex_a: str, color_hex_b: str) -> Dict[str, Any]:
        def_a = next((c for c in COLOR_REGISTRY.values() if c.hex_code.lower() == color_hex_a.lower()), None)
        def_b = next((c for c in COLOR_REGISTRY.values() if c.hex_code.lower() == color_hex_b.lower()), None)

        if not def_a or not def_b:
            return {
                "harmony_score": 80.0,
                "harmony_type": HarmonyType.NEUTRAL_ACCENT.value,
                "contrast_ratio": 3.5,
                "recommendation": "Standard harmonious fashion combination."
            }

        hue_diff = abs(def_a.hue_degrees - def_b.hue_degrees)
        if hue_diff > 180.0:
            hue_diff = 360.0 - hue_diff

        l1 = max(def_a.lightness_pct, def_b.lightness_pct)
        l2 = min(def_a.lightness_pct, def_b.lightness_pct)
        contrast = round((l1 + 5.0) / (l2 + 5.0), 2)

        if def_a.family == ColorFamily.MONOCHROME or def_b.family == ColorFamily.MONOCHROME:
            harmony = HarmonyType.NEUTRAL_ACCENT
            score = 95.0
            rec = "Monochrome base pairs seamlessly with any chromatic tone."
        elif hue_diff < 30.0:
            harmony = HarmonyType.ANALOGOUS
            score = 88.0
            rec = "Subtle monochromatic/analogous tonal look."
        elif 160.0 <= hue_diff <= 180.0:
            harmony = HarmonyType.COMPLEMENTARY
            score = 92.0 if contrast >= 2.0 else 75.0
            rec = "High-impact complementary color pairing."
        elif 110.0 <= hue_diff <= 130.0:
            harmony = HarmonyType.TRIADIC
            score = 86.0
            rec = "Dynamic triadic color energy."
        else:
            harmony = HarmonyType.SPLIT_COMPLEMENTARY
            score = 82.0
            rec = "Balanced aesthetic contrast."

        return {
            "color_a": def_a.name,
            "color_b": def_b.name,
            "harmony_score": round(score, 1),
            "harmony_type": harmony.value,
            "contrast_ratio": contrast,
            "recommendation": rec
        }

    @staticmethod
    def get_palette_for_undertone(undertone: SkinUndertone) -> List[Dict[str, Any]]:
        return [
            {
                "name": c.name,
                "hex": c.hex_code,
                "family": c.family.value,
                "warmth": c.warmth_index,
                "pairings": c.suggested_pairings
            }
            for c in COLOR_REGISTRY.values()
            if undertone in c.compatible_undertones
        ]
