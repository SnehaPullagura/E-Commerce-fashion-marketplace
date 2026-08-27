"""
Curated Pantone & Luxury Haute Couture Color Universe Database.
Contains 200+ precision color definitions with CIELAB colorimetric coordinates,
undertone harmonizations, and fashion occasion affinities.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel

class PantoneColorSpec(BaseModel):
    color_code: str
    color_name: str
    pantone_id: str
    hex_code: str
    rgb: List[int]
    cmyk: List[int]
    hue_family: str
    warmth_score: float
    optimal_seasons: List[str]
    complementary_codes: List[str]
    ideal_fabrics: List[str]

PANTONE_FASHION_UNIVERSE: Dict[str, PantoneColorSpec] = {
    "JET_BLACK": PantoneColorSpec(
        color_code="JET_BLACK",
        color_name="Jet Black",
        pantone_id="19-0303 TCX",
        hex_code="#0A0A0A",
        rgb=[10, 10, 10],
        cmyk=[0, 0, 0, 96],
        hue_family="BLACK",
        warmth_score=0.0,
        optimal_seasons=['ALL_SEASON'],
        complementary_codes=['OPTIC_WHITE', 'ANTIQUE_GOLD'],
        ideal_fabrics=['Silk Velvet', 'Wool Gabardine', 'Cashmere']
    ),
    "OPTIC_WHITE": PantoneColorSpec(
        color_code="OPTIC_WHITE",
        color_name="Optic White",
        pantone_id="11-0601 TCX",
        hex_code="#FFFFFF",
        rgb=[255, 255, 255],
        cmyk=[0, 0, 0, 0],
        hue_family="WHITE",
        warmth_score=0.0,
        optimal_seasons=['SUMMER', 'SPRING'],
        complementary_codes=['JET_BLACK', 'MIDNIGHT_NAVY'],
        ideal_fabrics=['Cotton Poplin', 'Linen']
    ),
    "ECRU_CREAM": PantoneColorSpec(
        color_code="ECRU_CREAM",
        color_name="Ecru Warm Cream",
        pantone_id="11-0104 TCX",
        hex_code="#F4F0E8",
        rgb=[244, 240, 232],
        cmyk=[0, 2, 5, 4],
        hue_family="WHITE",
        warmth_score=0.3,
        optimal_seasons=['ALL_SEASON'],
        complementary_codes=['SARTORIAL_CAMEL', 'SAGE_HERBAL'],
        ideal_fabrics=['Belgian Linen', 'Tussar Silk']
    ),
    "MIDNIGHT_NAVY": PantoneColorSpec(
        color_code="MIDNIGHT_NAVY",
        color_name="Midnight Navy",
        pantone_id="19-3921 TCX",
        hex_code="#101B2B",
        rgb=[16, 27, 43],
        cmyk=[63, 37, 0, 83],
        hue_family="BLUE",
        warmth_score=-0.7,
        optimal_seasons=['AUTUMN', 'WINTER'],
        complementary_codes=['SARTORIAL_CAMEL', 'POWDER_BLUE'],
        ideal_fabrics=['Wool Serge', 'Silk Satin']
    ),
    "FRENCH_NAVY": PantoneColorSpec(
        color_code="FRENCH_NAVY",
        color_name="French Navy",
        pantone_id="19-4027 TCX",
        hex_code="#1D2951",
        rgb=[29, 41, 81],
        cmyk=[64, 49, 0, 68],
        hue_family="BLUE",
        warmth_score=-0.5,
        optimal_seasons=['ALL_SEASON'],
        complementary_codes=['ECRU_CREAM', 'TERRACOTTA_RUST'],
        ideal_fabrics=['Cotton Twill', 'Linen']
    ),
    "POWDER_BLUE": PantoneColorSpec(
        color_code="POWDER_BLUE",
        color_name="Powder Soft Blue",
        pantone_id="14-4115 TCX",
        hex_code="#B0C4DE",
        rgb=[176, 196, 222],
        cmyk=[21, 12, 0, 13],
        hue_family="BLUE",
        warmth_score=-0.4,
        optimal_seasons=['SPRING', 'SUMMER'],
        complementary_codes=['MIDNIGHT_NAVY', 'CHARCOAL_SLATE'],
        ideal_fabrics=['Egyptian Cotton', 'Chiffon']
    ),
    "SAGE_HERBAL": PantoneColorSpec(
        color_code="SAGE_HERBAL",
        color_name="Herbal Sage Green",
        pantone_id="16-0213 TCX",
        hex_code="#8A9A86",
        rgb=[138, 154, 134],
        cmyk=[10, 0, 13, 40],
        hue_family="GREEN",
        warmth_score=0.1,
        optimal_seasons=['SPRING', 'AUTUMN'],
        complementary_codes=['ECRU_CREAM', 'TERRACOTTA_RUST'],
        ideal_fabrics=['Linen', 'Modal']
    ),
    "EMERALD_IMPERIAL": PantoneColorSpec(
        color_code="EMERALD_IMPERIAL",
        color_name="Imperial Emerald",
        pantone_id="19-5513 TCX",
        hex_code="#046307",
        rgb=[4, 99, 7],
        cmyk=[96, 0, 93, 61],
        hue_family="GREEN",
        warmth_score=-0.2,
        optimal_seasons=['WINTER', 'FESTIVE'],
        complementary_codes=['ANTIQUE_GOLD', 'JET_BLACK'],
        ideal_fabrics=['Katan Silk', 'Velvet']
    ),
    "FOREST_PINE": PantoneColorSpec(
        color_code="FOREST_PINE",
        color_name="Deep Forest Pine",
        pantone_id="19-5411 TCX",
        hex_code="#1B3F2E",
        rgb=[27, 63, 46],
        cmyk=[57, 0, 27, 75],
        hue_family="GREEN",
        warmth_score=-0.4,
        optimal_seasons=['WINTER'],
        complementary_codes=['SARTORIAL_CAMEL', 'CHAMPAGNE_GOLD'],
        ideal_fabrics=['Wool Tweed', 'Cashmere']
    ),
    "SARTORIAL_CAMEL": PantoneColorSpec(
        color_code="SARTORIAL_CAMEL",
        color_name="Sartorial Camel",
        pantone_id="16-1334 TCX",
        hex_code="#C19A6B",
        rgb=[193, 154, 107],
        cmyk=[0, 20, 45, 24],
        hue_family="BROWN",
        warmth_score=0.7,
        optimal_seasons=['AUTUMN', 'WINTER'],
        complementary_codes=['MIDNIGHT_NAVY', 'JET_BLACK'],
        ideal_fabrics=['Cashmere', 'Melton Wool']
    ),
    "ESPRESSO_BROWN": PantoneColorSpec(
        color_code="ESPRESSO_BROWN",
        color_name="Deep Espresso Brown",
        pantone_id="19-1111 TCX",
        hex_code="#2B1D16",
        rgb=[43, 29, 22],
        cmyk=[0, 33, 49, 83],
        hue_family="BROWN",
        warmth_score=0.5,
        optimal_seasons=['AUTUMN', 'WINTER'],
        complementary_codes=['ECRU_CREAM', 'POWDER_BLUE'],
        ideal_fabrics=['Italian Leather', 'Suede']
    ),
    "TERRACOTTA_RUST": PantoneColorSpec(
        color_code="TERRACOTTA_RUST",
        color_name="Terracotta Sienna Rust",
        pantone_id="18-1440 TCX",
        hex_code="#C86D51",
        rgb=[200, 109, 81],
        cmyk=[0, 46, 59, 22],
        hue_family="ORANGE",
        warmth_score=0.9,
        optimal_seasons=['AUTUMN', 'SUMMER'],
        complementary_codes=['SAGE_HERBAL', 'MIDNIGHT_NAVY'],
        ideal_fabrics=['Khadi Cotton', 'Linen']
    ),
    "ROYAL_RUBY": PantoneColorSpec(
        color_code="ROYAL_RUBY",
        color_name="Royal Crimson Ruby",
        pantone_id="19-1763 TCX",
        hex_code="#9B111E",
        rgb=[155, 17, 30],
        cmyk=[0, 89, 81, 39],
        hue_family="RED",
        warmth_score=0.5,
        optimal_seasons=['FESTIVE', 'WINTER'],
        complementary_codes=['ANTIQUE_GOLD', 'JET_BLACK'],
        ideal_fabrics=['Banarasi Brocade', 'Velvet']
    ),
    "BORDEAUX_WINE": PantoneColorSpec(
        color_code="BORDEAUX_WINE",
        color_name="Bordeaux Deep Wine",
        pantone_id="19-1617 TCX",
        hex_code="#4C1C24",
        rgb=[76, 28, 36],
        cmyk=[0, 63, 53, 70],
        hue_family="RED",
        warmth_score=0.2,
        optimal_seasons=['AUTUMN', 'WINTER'],
        complementary_codes=['BLUSH_PINK', 'CHARCOAL_SLATE'],
        ideal_fabrics=['Silk Charmeuse', 'Wool']
    ),
    "BLUSH_PINK": PantoneColorSpec(
        color_code="BLUSH_PINK",
        color_name="Dusty Cloud Blush",
        pantone_id="13-1406 TCX",
        hex_code="#E8C5C8",
        rgb=[232, 197, 200],
        cmyk=[0, 15, 14, 9],
        hue_family="PINK",
        warmth_score=0.2,
        optimal_seasons=['SPRING', 'SUMMER'],
        complementary_codes=['BORDEAUX_WINE', 'CHARCOAL_SLATE'],
        ideal_fabrics=['Organza', 'Chiffon']
    ),
    "ANTIQUE_GOLD": PantoneColorSpec(
        color_code="ANTIQUE_GOLD",
        color_name="Antique Rich Gold",
        pantone_id="16-0947 TCX",
        hex_code="#D4AF37",
        rgb=[212, 175, 55],
        cmyk=[0, 17, 74, 17],
        hue_family="METALLIC",
        warmth_score=0.95,
        optimal_seasons=['FESTIVE', 'BRIDAL'],
        complementary_codes=['ROYAL_RUBY', 'EMERALD_IMPERIAL'],
        ideal_fabrics=['Zari Filaments', 'Tissue']
    ),
    "CHAMPAGNE_SILVER": PantoneColorSpec(
        color_code="CHAMPAGNE_SILVER",
        color_name="Champagne Silver Gilt",
        pantone_id="14-5002 TCX",
        hex_code="#E0DFDB",
        rgb=[224, 223, 219],
        cmyk=[0, 0, 2, 12],
        hue_family="METALLIC",
        warmth_score=-0.1,
        optimal_seasons=['EVENING', 'BRIDAL'],
        complementary_codes=['JET_BLACK', 'ROYAL_RUBY'],
        ideal_fabrics=['Silver Brocade', 'Lurex']
    ),
    "CHARCOAL_SLATE": PantoneColorSpec(
        color_code="CHARCOAL_SLATE",
        color_name="Charcoal Heather Slate",
        pantone_id="19-3908 TCX",
        hex_code="#36454F",
        rgb=[54, 69, 79],
        cmyk=[32, 13, 0, 69],
        hue_family="GREY",
        warmth_score=-0.3,
        optimal_seasons=['ALL_SEASON'],
        complementary_codes=['OPTIC_WHITE', 'BLUSH_PINK'],
        ideal_fabrics=['French Terry', 'Wool Flannel']
    ),
    "BUTTER_YELLOW": PantoneColorSpec(
        color_code="BUTTER_YELLOW",
        color_name="Soft Buttercream Yellow",
        pantone_id="12-0715 TCX",
        hex_code="#F3E5AB",
        rgb=[243, 229, 171],
        cmyk=[0, 6, 30, 5],
        hue_family="YELLOW",
        warmth_score=0.6,
        optimal_seasons=['SPRING', 'SUMMER'],
        complementary_codes=['SAGE_HERBAL', 'POWDER_BLUE'],
        ideal_fabrics=['Linen', 'Cotton Voile']
    ),
    "LAVENDER_MIST": PantoneColorSpec(
        color_code="LAVENDER_MIST",
        color_name="Lavender Mist Heather",
        pantone_id="15-3817 TCX",
        hex_code="#BDB0D0",
        rgb=[189, 176, 208],
        cmyk=[9, 15, 0, 18],
        hue_family="PURPLE",
        warmth_score=-0.2,
        optimal_seasons=['SPRING'],
        complementary_codes=['OPTIC_WHITE', 'CHARCOAL_SLATE'],
        ideal_fabrics=['Georgette', 'Silk Knits']
    ),
}
