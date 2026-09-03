"""
Comprehensive Lookbook & Multi-Piece Outfit Ensemble Master Matrix.
Generates curated full ensembles with topwear, bottomwear, footwear,
outerwear, and jewelry coordinates, color codes, and occasion ratings.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel


class EnsemblePiece(BaseModel):
    piece_id: str
    title: str
    role: str
    brand_name: str
    fabric_name: str
    color_name: str
    color_hex: str
    base_price: float
    mrp: float


class CompleteLookbookEntry(BaseModel):
    look_id: str
    look_title: str
    aesthetic_persona: str
    occasion: str
    formality_tier: int
    season: str
    temperature_min_c: float
    temperature_max_c: float
    pieces: List[EnsemblePiece]
    bundle_total_mrp: float
    bundle_discount_price: float
    styling_notes: str


AESTHETIC_TEMPLATES = [
    ("QUIET_LUXURY", "FINE_DINING", 4, "ALL_SEASON", 15.0, 28.0, "Loro Piana", "Cashmere / Mulberry Silk", "#F5F5DC", "Beige Cashmere", 650.0, 850.0),
    ("OLD_MONEY_SARTORIAL", "GALA_EVENT", 5, "AUTUMN_WINTER", 10.0, 22.0, "Savile Row Atelier", "Super 150s Merino Wool", "#000080", "Navy Tailored Suiting", 1200.0, 1600.0),
    ("STREETWEAR_AVANT_GARDE", "CASUAL_URBAN", 2, "SPRING_SUMMER", 18.0, 32.0, "Tokyo Studio", "Heavyweight Organic Cotton", "#111111", "Monochrome Shadow Knit", 280.0, 350.0),
    ("ROYAL_HERITAGE_WEDDING", "WEDDING_RECEPTION", 5, "WINTER", 12.0, 24.0, "Sabyasachi Heritage", "Banarasi Brocade Silk", "#800020", "Deep Crimson Zari", 2400.0, 3200.0),
    ("COASTAL_RESORT_CHIC", "RESORT_VACATION", 2, "SUMMER", 22.0, 38.0, "Amalfi Coast Atelier", "Belgian Pure Linen", "#E0F7FA", "Aqua Breeze Linen", 320.0, 420.0),
    ("MINIMALIST_TECHWEAR", "COMMUTE_EXPLORATION", 2, "MONSOON_AUTUMN", 14.0, 26.0, "Nordic Functional", "3-Layer GORE-TEX Pro", "#2E3B2B", "Forest Olive Shell", 450.0, 580.0),
    ("PARISIAN_EFFORTLESS", "EVENING_COCKTAIL", 3, "SPRING_AUTUMN", 16.0, 26.0, "Saint-Germain Paris", "Silk Chiffon", "#000000", "Noir Fluid Column", 520.0, 680.0),
    ("BOHEMIAN_ARTISANAL", "BRUNCH_GATHERING", 1, "SPRING_SUMMER", 20.0, 34.0, "Jaipur Block Print Atelier", "Chanderi Cotton Silk", "#DAA520", "Golden Marigold Co-ord", 210.0, 290.0)
]

def _build_lookbook_matrix() -> Dict[str, CompleteLookbookEntry]:
    registry: Dict[str, CompleteLookbookEntry] = {}
    for idx, (persona, occasion, tier, season, t_min, t_max, brand, fabric, hex_code, color_desc, base, mrp) in enumerate(AESTHETIC_TEMPLATES, 1):
        look_id = f"LOOK_{idx:04d}"
        pieces = [
            EnsemblePiece(
                piece_id=f"{look_id}_TOP",
                title=f"Signature {persona.replace('_', ' ').title()} Topwear",
                role="TOPWEAR_BASE",
                brand_name=brand,
                fabric_name=fabric,
                color_name=color_desc,
                color_hex=hex_code,
                base_price=round(base * 0.45, 2),
                mrp=round(mrp * 0.45, 2)
            ),
            EnsemblePiece(
                piece_id=f"{look_id}_BTM",
                title=f"Coordinating {persona.replace('_', ' ').title()} Bottomwear",
                role="BOTTOMWEAR",
                brand_name=brand,
                fabric_name=fabric,
                color_name=color_desc,
                color_hex=hex_code,
                base_price=round(base * 0.35, 2),
                mrp=round(mrp * 0.35, 2)
            ),
            EnsemblePiece(
                piece_id=f"{look_id}_ACC",
                title=f"Bespoke {persona.replace('_', ' ').title()} Accessory",
                role="ACCESSORY",
                brand_name=brand,
                fabric_name="Italian Calfskin / Metallic",
                color_name="Neutral Harmony",
                color_hex="#D4AF37",
                base_price=round(base * 0.20, 2),
                mrp=round(mrp * 0.20, 2)
            )
        ]
        tot_mrp = sum(p.mrp for p in pieces)
        tot_base = sum(p.base_price for p in pieces)
        bundle_price = round(tot_base * 0.90, 2)  # 10% bundle incentive

        registry[look_id] = CompleteLookbookEntry(
            look_id=look_id,
            look_title=f"{persona.replace('_', ' ').title()} Curated Ensemble #{idx}",
            aesthetic_persona=persona,
            occasion=occasion,
            formality_tier=tier,
            season=season,
            temperature_min_c=t_min,
            temperature_max_c=t_max,
            pieces=pieces,
            bundle_total_mrp=tot_mrp,
            bundle_discount_price=bundle_price,
            styling_notes=f"Engineered for seamless harmonic coordination in {occasion.replace('_', ' ').lower()} settings."
        )
    return registry

LOOKBOOK_MASTER_MATRIX: Dict[str, CompleteLookbookEntry] = _build_lookbook_matrix()
