"""
AI Fashion Stylist, Color Harmony Engine & Capsule Wardrobe Coordinator.
Provides algorithmic color wheel theory, undertone harmonic compatibility,
and multi-occasion capsule wardrobe generation.
"""

from typing import Dict, List, Optional, Any, Tuple
from pydantic import BaseModel, Field
from enum import Enum
import colorsys
import math


class UndertoneType(str, Enum):
    WARM = "WARM"      # Golden, yellow, peachy undertones
    COOL = "COOL"      # Pink, red, bluish undertones
    NEUTRAL = "NEUTRAL"# Balanced mix of warm and cool
    OLIVE = "OLIVE"    # Greenish, neutral-golden undertones


class HarmonyModel(str, Enum):
    MONOCHROMATIC = "MONOCHROMATIC"
    COMPLEMENTARY = "COMPLEMENTARY"
    ANALOGOUS = "ANALOGOUS"
    TRIADIC = "TRIADIC"
    SPLIT_COMPLEMENTARY = "SPLIT_COMPLEMENTARY"


class ColorTheoryEngine:
    @staticmethod
    def hex_to_hsl(hex_str: str) -> Tuple[float, float, float]:
        """Converts hex color string to Hue (0-360), Saturation (0-100), Lightness (0-100)."""
        clean_hex = hex_str.lstrip('#')
        if len(clean_hex) != 6:
            clean_hex = "000000"
        r, g, b = [int(clean_hex[i:i+2], 16) / 255.0 for i in (0, 2, 4)]
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        return (round(h * 360.0, 1), round(s * 100.0, 1), round(l * 100.0, 1))

    @staticmethod
    def calculate_color_harmony_score(hex_a: str, hex_b: str) -> Dict[str, Any]:
        """Evaluates chromatic harmony between two garment colors."""
        h1, s1, l1 = ColorTheoryEngine.hex_to_hsl(hex_a)
        h2, s2, l2 = ColorTheoryEngine.hex_to_hsl(hex_b)

        hue_diff = abs(h1 - h2)
        if hue_diff > 180.0:
            hue_diff = 360.0 - hue_diff

        # Identify harmony type
        if hue_diff <= 30.0 and abs(l1 - l2) >= 10.0:
            harmony = HarmonyModel.MONOCHROMATIC
            base_score = 92.0
        elif 145.0 <= hue_diff <= 215.0:
            harmony = HarmonyModel.COMPLEMENTARY
            base_score = 95.0
        elif 30.0 < hue_diff <= 65.0:
            harmony = HarmonyModel.ANALOGOUS
            base_score = 88.0
        elif 105.0 <= hue_diff <= 135.0:
            harmony = HarmonyModel.TRIADIC
            base_score = 86.0
        else:
            harmony = HarmonyModel.SPLIT_COMPLEMENTARY
            base_score = 78.0

        # Contrast balance bonus
        contrast = abs(l1 - l2)
        contrast_bonus = 5.0 if 25.0 <= contrast <= 60.0 else 0.0

        final_score = min(100.0, base_score + contrast_bonus)

        return {
            "color_a": hex_a,
            "color_b": hex_b,
            "hue_distance_deg": round(hue_diff, 1),
            "detected_harmony": harmony.value,
            "harmony_score": round(final_score, 1),
            "stylist_notes": (
                "Striking high-contrast complementary balance" if harmony == HarmonyModel.COMPLEMENTARY else
                ("Elegant ton-sur-ton monochromatic layering" if harmony == HarmonyModel.MONOCHROMATIC else
                 "Cohesive analogous flow ideal for refined styling")
            )
        }

    @staticmethod
    def get_palette_for_undertone(undertone: UndertoneType) -> Dict[str, Any]:
        """Returns optimal color palette and recommended power accents."""
        palettes = {
            UndertoneType.WARM: {
                "core_neutrals": ["#F5F5DC", "#8B5A2B", "#D2B48C", "#4A3728"],
                "signature_accents": ["#E2583E", "#FFBF00", "#556B2F", "#DAA520", "#C34A2C"],
                "avoid": ["#00FFFF", "#E0FFFF", "#C0C0C0", "#FF1493"],
                "description": "Earth tones, golden terracottas, warm ochres, and olive greens elevate natural radiance."
            },
            UndertoneType.COOL: {
                "core_neutrals": ["#000080", "#708090", "#FFFFFF", "#2F4F4F"],
                "signature_accents": ["#4169E1", "#800080", "#008080", "#C71585", "#4B0082"],
                "avoid": ["#FF8C00", "#DAA520", "#B8860B", "#D2691E"],
                "description": "Jewel tones, crisp royal navy, emerald, pure platinum white, and magenta enhance porcelain and deep cool complexions."
            },
            UndertoneType.NEUTRAL: {
                "core_neutrals": ["#808080", "#FAF0E6", "#2C3539", "#A9A9A9"],
                "signature_accents": ["#50C878", "#E6E6FA", "#DE5D83", "#778899", "#AF6E4D"],
                "avoid": ["#FF0000", "#FFFF00"],
                "description": "Universal soft pastels, dusty rose, sage green, and muted charcoals flatter neutral skin tones seamlessly."
            },
            UndertoneType.OLIVE: {
                "core_neutrals": ["#555555", "#C2B280", "#2E3B2B", "#3B312B"],
                "signature_accents": ["#808000", "#722F37", "#4B5320", "#CD853F", "#B7410E"],
                "avoid": ["#FFB6C1", "#E6E6FA"],
                "description": "Rich wine, deep forest moss, bronze gold, and warm saffron bring out subtle green-golden undertones."
            }
        }
        return palettes.get(undertone, palettes[UndertoneType.NEUTRAL])


class CapsuleWardrobeCoordinator:
    @staticmethod
    def generate_7_day_capsule(
        capsule_items: List[Dict[str, Any]],
        style_persona: str = "SMART_ELEGANCE"
    ) -> Dict[str, Any]:
        """
        Synthesizes a 7-day capsule rotation (workday, dinner, weekend casual)
        from a minimalist base of 5-8 versatile wardrobe staples.
        """
        tops = [i for i in capsule_items if i.get("category", "").upper() in ["TOP", "SHIRT", "BLOUSE", "KNITWEAR"]]
        bottoms = [i for i in capsule_items if i.get("category", "").upper() in ["BOTTOM", "PANTS", "TROUSERS", "SKIRT", "JEANS"]]
        outerwear = [i for i in capsule_items if i.get("category", "").upper() in ["OUTERWEAR", "BLAZER", "COAT", "JACKET"]]
        shoes = [i for i in capsule_items if i.get("category", "").upper() in ["FOOTWEAR", "SHOES", "BOOTS", "LOAFERS"]]

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_themes = [
            ("Monday", "Executive Kickoff", "BUSINESS_FORMAL"),
            ("Tuesday", "Client Meetings & Lunch", "SMART_CASUAL"),
            ("Wednesday", "Focus Studio Work", "ELEVATED_CASUAL"),
            ("Thursday", "Gallery Opening & Dinner", "COCKTAIL_ELEGANCE"),
            ("Friday", "Casual Friday & Drinks", "SMART_CASUAL"),
            ("Saturday", "Weekend Brunch & Stroll", "RELAXED_CHIC"),
            ("Sunday", "Sunset Lounge & Travel", "MINIMALIST_COMFORT")
        ]

        outfit_schedule = []
        for idx, (day_name, theme, occasion) in enumerate(day_themes):
            chosen_top = tops[idx % len(tops)] if tops else {"title": "Tailored Silk Blouse"}
            chosen_bottom = bottoms[(idx + 1) % len(bottoms)] if bottoms else {"title": "High-Waist Wool Trousers"}
            chosen_outer = outerwear[idx % len(outerwear)] if outerwear else {"title": "Classic Structured Blazer"}
            chosen_shoes = shoes[idx % len(shoes)] if shoes else {"title": "Leather Bit Loafers"}

            outfit_schedule.append({
                "day": day_name,
                "theme": theme,
                "occasion": occasion,
                "ensemble": {
                    "top": chosen_top.get("title", "Core Top"),
                    "bottom": chosen_bottom.get("title", "Core Bottom"),
                    "outerwear": chosen_outer.get("title", "Core Outerwear"),
                    "footwear": chosen_shoes.get("title", "Core Footwear")
                },
                "styling_tip": f"Pair {chosen_top.get('title')} tucked into {chosen_bottom.get('title')} with draped {chosen_outer.get('title')} for effortless {theme.lower()}."
            })

        return {
            "persona": style_persona,
            "total_wardrobe_items": len(capsule_items),
            "generated_outfit_days": len(outfit_schedule),
            "versatility_multiplier": round(len(outfit_schedule) / max(1, len(capsule_items)), 2),
            "schedule": outfit_schedule
        }


class AIStylistAdvisor:
    @staticmethod
    def answer_styling_query(
        prompt: str,
        user_gender: Optional[str] = "FEMALE",
        occasion: Optional[str] = "WEDDING_GUEST"
    ) -> Dict[str, Any]:
        """Provides instant bespoke AI fashion styling recommendations."""
        clean_prompt = prompt.lower()

        if "beach" in clean_prompt or "resort" in clean_prompt:
            recommendation = {
                "vibe": "Resort Elegance & Sun-Drenched Luxe",
                "key_garment": "Tiered linen halter maxi dress or breezy silk crepe de chine co-ord",
                "footwear": "Metallic strappy leather espadrilles or woven leather slides",
                "accessories": ["Oversized raffia tote", "UV400 tortoiseshell sunglasses", "Hammered 18k gold huggies"],
                "color_palette": ["#F4E8C1", "#E07A5F", "#81B29A", "#3D405B"],
                "advice": "Prioritize breathable natural textiles (mulberry silk, organic linen) with fluid movement for breezy ocean settings."
            }
        elif "black tie" in clean_prompt or "gala" in clean_prompt or "red carpet" in clean_prompt:
            recommendation = {
                "vibe": "Haute Couture & Sculptural Glamour",
                "key_garment": "Column velvet gown with architectural shoulder drape or double-breasted midnight tuxedo",
                "footwear": "Crystal-embellished pointed pumps or patent leather derbies",
                "accessories": ["Satin minaudière clutch", "Diamond tennis necklace", "Silk pocket square"],
                "color_palette": ["#0B0B0B", "#1A2238", "#4A0E17", "#D4AF37"],
                "advice": "Ensure tailored hem lengths clear footwear by 0.5 cm to preserve pristine silhouette lines during stride."
            }
        else:
            recommendation = {
                "vibe": "Smart Modern Tailoring & Contemporary Capsule",
                "key_garment": "Relaxed double-faced wool blazer over mercerized cotton knit",
                "footwear": "Minimalist white calfskin sneakers or almond-toe leather chelsea boots",
                "accessories": ["Pebbled leather crossbody", "Clean brushed silver cuff watch"],
                "color_palette": ["#2B2D42", "#8D99AE", "#EDF2F4", "#EF233C"],
                "advice": "Balance structural rigidity with softer inner layers to create visual depth and versatile transition."
            }

        return {
            "query": prompt,
            "occasion": occasion,
            "stylist_curation": recommendation,
            "stylist_signature": "FashionIQ AI Advisory Suite v2.4"
        }
