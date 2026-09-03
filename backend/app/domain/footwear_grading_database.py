"""
International Footwear Sizing, Last Geometry & Width Fitting Database.
Contains precision Mondopoint (mm), UK, US Men, US Women, and EU sizes
across artisanal shoe silhouettes with foot volume ease calculations.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel


class FootwearSizeSpec(BaseModel):
    mondopoint_mm: float
    uk_size: float
    us_men_size: float
    us_women_size: float
    eu_size: float
    insole_length_cm: float
    ball_girth_circumference_cm: float
    instep_girth_cm: float
    heel_width_cm: float
    width_grade: str  # "NARROW_B", "STANDARD_D", "WIDE_EE", "EXTRA_WIDE_4E"


class FootwearModelSpec(BaseModel):
    model_code: str
    model_name: str
    style_category: str  # "SARTORIAL_LOAFER", "COURT_SNEAKER", "HERITAGE_MOJARI", "CHELSEA_BOOT"
    upper_material: str
    sole_construction: str  # "GOODYEAR_WELT", "BLAKE_STITCH", "VULCANIZED", "HAND_STITCHED"
    break_in_period_wears: int
    size_specifications: Dict[str, FootwearSizeSpec]


def _build_footwear_sizes() -> Dict[str, FootwearSizeSpec]:
    specs = {}
    eu_sizes = [38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0]
    for idx, eu in enumerate(eu_sizes):
        uk = round(eu - 33.0, 1)
        us_m = round(uk + 1.0, 1)
        us_w = round(uk + 2.5, 1)
        mondo = round(240.0 + (idx * 6.5), 1)
        specs[f"EU_{int(eu)}"] = FootwearSizeSpec(
            mondopoint_mm=mondo,
            uk_size=uk,
            us_men_size=us_m,
            us_women_size=us_w,
            eu_size=eu,
            insole_length_cm=round(mondo / 10.0, 1),
            ball_girth_circumference_cm=round(23.0 + (idx * 0.4), 1),
            instep_girth_cm=round(24.0 + (idx * 0.4), 1),
            heel_width_cm=round(6.5 + (idx * 0.15), 1),
            width_grade="STANDARD_D"
        )
    return specs


FOOTWEAR_MODELS = [
    ("FTW_LOAFER_01", "Artisanal Penny Loafer", "SARTORIAL_LOAFER", "Full Grain Calfskin", "GOODYEAR_WELT", 5),
    ("FTW_CHELSEA_02", "Heritage Chelsea Boot", "CHELSEA_BOOT", "Waxed Suede", "GOODYEAR_WELT", 7),
    ("FTW_SNEAKER_03", "Minimal Court Sneaker", "COURT_SNEAKER", "Italian Napa Leather", "VULCANIZED", 2),
    ("FTW_MOJARI_04", "Royal Embroidered Mojari", "HERITAGE_MOJARI", "Raw Silk & Soft Leather", "HAND_STITCHED", 3),
    ("FTW_MONK_05", "Double Monk Strap Oxford", "SARTORIAL_LOAFER", "Burnished Crust Leather", "BLAKE_STITCH", 6)
]

FOOTWEAR_DATABASE: Dict[str, FootwearModelSpec] = {
    code: FootwearModelSpec(
        model_code=code,
        model_name=name,
        style_category=cat,
        upper_material=mat,
        sole_construction=sole,
        break_in_period_wears=wears,
        size_specifications=_build_footwear_sizes()
    )
    for code, name, cat, mat, sole, wears in FOOTWEAR_MODELS
}
