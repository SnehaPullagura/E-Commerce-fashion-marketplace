"""
Fashion Persona Archetype Registry and Style DNA Profiling Engine.
Defines 16 distinct high-fashion personas with curated aesthetics,
color tendencies, key staple pieces, and silhouette affinities.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel
from enum import Enum


class StyleAesthetic(str, Enum):
    MINIMALIST_CLEAN = "MINIMALIST_CLEAN"
    QUIET_LUXURY = "QUIET_LUXURY"
    OLD_MONEY_SARTORIAL = "OLD_MONEY_SARTORIAL"
    STREETWEAR_URBAN = "STREETWEAR_URBAN"
    CYBERPUNK_TECHWEAR = "CYBERPUNK_TECHWEAR"
    ROYAL_HERITAGE_FESTIVE = "ROYAL_HERITAGE_FESTIVE"
    CONTEMPORARY_INDO_WESTERN = "CONTEMPORARY_INDO_WESTERN"
    PARISIAN_CHIC = "PARISIAN_CHIC"
    BOHEMIAN_COASTAL = "BOHEMIAN_COASTAL"
    DARK_ACADEMIA = "DARK_ACADEMIA"
    Y2K_RETRO_NOSTALGIA = "Y2K_RETRO_NOSTALGIA"
    HIGH_PERFORMANCE_ATHLEISURE = "HIGH_PERFORMANCE_ATHLEISURE"


class PersonaProfile(BaseModel):
    id: StyleAesthetic
    name: str
    tagline: str
    description: str
    key_fabrics: List[str]
    staple_silhouettes: List[str]
    signature_color_hexes: List[str]
    preferred_occasions: List[str]
    recommended_brands: List[str]
    styling_tips: List[str]


PERSONA_REGISTRY: Dict[StyleAesthetic, PersonaProfile] = {
    StyleAesthetic.MINIMALIST_CLEAN: PersonaProfile(
        id=StyleAesthetic.MINIMALIST_CLEAN,
        name="Minimalist Clean Aesthetic",
        tagline="Less is more: architectural tailoring, pure lines and monochromatic restraint",
        description="Focuses on understated perfection, uncluttered cuts, premium tactile fabrics and immaculate proportions.",
        key_fabrics=["Belgian Linen", "Egyptian Cotton Poplin", "Heavyweight Jersey", "Wool Gabardine"],
        staple_silhouettes=["Mandarin collar shirt", "Tailored wide-leg trousers", "Boxy tee", "Column midi dress"],
        signature_color_hexes=["#111111", "#FAF9F6", "#8A9A86", "#36454F"],
        preferred_occasions=["Office", "Weekend Brunch", "Art Gallery", "Travel"],
        recommended_brands=["Noir Couture", "Cos", "Toteme", "Lemaire"],
        styling_tips=[
            "Anchor outfits in neutral foundation shades and introduce subtle textural contrast rather than loud prints.",
            "Prioritize impeccable fit and natural un-ironed drape of linen and silk.",
            "Limit accessories to one architectural timepiece or sculpted jewelry piece."
        ]
    ),
    StyleAesthetic.QUIET_LUXURY: PersonaProfile(
        id=StyleAesthetic.QUIET_LUXURY,
        name="Quiet Luxury / Stealth Wealth",
        tagline="Unbranded opulence: double-faced cashmere, vicuña and artisanal leather",
        description="Whispered prestige characterized by world-class textiles, impeccable construction, and zero visible logos.",
        key_fabrics=["Grade-A Mongolian Cashmere", "Mulberry Silk", "Sea Island Cotton", "Merino Wool"],
        staple_silhouettes=["Double-breasted blazer", "High-rise tailored trousers", "Cashmere crewneck", "Italian leather loafers"],
        signature_color_hexes=["#C19A6B", "#1B2A4A", "#FAF9F6", "#3D2417"],
        preferred_occasions=["Business Summit", "Private Club", "Luxury Travel", "Fine Dining"],
        recommended_brands=["Loro Piana", "Brunello Cucinelli", "The Row", "Noir Atelier"],
        styling_tips=[
            "Pair tonal cashmere with high-waisted wool trousers in cream or camel.",
            "Choose handmade suede loafers with unlined softness for effortless sophistication.",
            "Keep tailoring relaxed yet sharp with subtle natural shoulder pads."
        ]
    ),
    StyleAesthetic.ROYAL_HERITAGE_FESTIVE: PersonaProfile(
        id=StyleAesthetic.ROYAL_HERITAGE_FESTIVE,
        name="Royal Heritage & Festive Couture",
        tagline="Imperial grandeur: Banarasi katan silks, hand-embroidered zari and royal kalis",
        description="Celebrates centuries of Indian textile craftsmanship, intricate gota patti, royal brocades, and opulent silhouettes.",
        key_fabrics=["Banarasi Katan Silk", "Raw Mulberry Silk", "Zari Georgette", "Organza Tissue"],
        staple_silhouettes=["32-Kali Anarkali", "Bridal Lehenga Set", "Bandhgala Suit", "Handcrafted Silk Kurta Set"],
        signature_color_hexes=["#9B111E", "#D4AF37", "#046307", "#4A0E17"],
        preferred_occasions=["Wedding", "Sangeet", "Festive Gala", "Diwali"],
        recommended_brands=["Anita Dongre", "Sabyasachi", "Raw Mango", "Tarun Tahiliani"],
        styling_tips=[
            "Balance heavy zari brocade with antique gold polki or emerald jewelry.",
            "Drape dual dupattas for ceremonial bridal weight and dramatic volume.",
            "Store handwoven silks in unbleached muslin to preserve gold zari lustre."
        ]
    ),
    StyleAesthetic.STREETWEAR_URBAN: PersonaProfile(
        id=StyleAesthetic.STREETWEAR_URBAN,
        name="Streetwear & Urban Culture",
        tagline="Bold silhouettes, oversized boxy cuts, raw denim and high-impact drops",
        description="Rooted in contemporary skate, hip-hop and Tokyo raw denim aesthetics with heavyweight construction.",
        key_fabrics=["450 GSM French Terry", "14.5oz Japanese Selvedge Denim", "Nylon Ripstop", "Corduroy"],
        staple_silhouettes=["Drop-shoulder hoodie", "Cargo utility pants", "Raw denim trucker", "Vintage wash tee"],
        signature_color_hexes=["#111111", "#36454F", "#8A9A86", "#C86D51"],
        preferred_occasions=["Streetwear Drops", "Concerts", "Casual Day Out", "Skate Park"],
        recommended_brands=["Tokyo Raw", "Fear of God", "Stüssy", "Rhude"],
        styling_tips=[
            "Layer an oversized boxy hoodie over an elongated curved-hem tee for proportion play.",
            "Pair raw selvedge denim with single cuff turnover showing the redline selvedge ID.",
            "Finish with clean leather retro court sneakers or chunky combat boots."
        ]
    )
}
