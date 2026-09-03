"""
International Textile Construction & Weave Yarn Engineering Matrix.
Contains textile engineering specifications with warp/weft yarn counts,
tensile ratings, finishing treatments, and international trade tariff classifications.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel


class YarnStructureSpec(BaseModel):
    fabric_id: str
    commercial_trade_name: str
    fiber_blend_ratio: str
    warp_yarn_count: str
    weft_yarn_count: str
    ends_per_inch: int
    picks_per_inch: int
    weight_gsm: float
    finishing_processes: List[str]
    tensile_strength_warp_n: float
    tensile_strength_weft_n: float
    air_permeability_cm3_per_s: float
    hsn_tax_tariff: str = "6205"


FABRIC_SPECS = [
    ("FAB_BELGIAN_LINEN", "Belgian Wet-Spun Pure Flax Linen Plain", "100% Flax Linen", "36 Lea Wet Spun", "36 Lea Wet Spun", 56, 52, 165.0, ["Bio-Enzyme Wash", "Aero-Softening"], 450.0, 380.0, 120.0, "5309"),
    ("FAB_MULBERRY_SILK", "Grade 6A Mulberry Silk Charmeuse", "100% Mulberry Silk", "20/22D Organzine", "20/22D Tram", 180, 110, 85.0, ["Degummed", "Calendered"], 320.0, 280.0, 65.0, "5007"),
    ("FAB_EGYPTIAN_COTTON", "Giza 88 Extra-Long Staple Cotton Sateen 400TC", "100% ELS Egyptian Cotton", "80/1 Compact Warp", "80/1 Compact Weft", 220, 180, 125.0, ["Caustic Mercerized", "Sanforized"], 520.0, 480.0, 85.0, "5208"),
    ("FAB_MERINO_SUITING", "Super 150s Australian Merino Wool Twill", "100% Super 150s Virgin Wool", "2/80 Nm Worsted", "2/80 Nm Worsted", 110, 95, 260.0, ["Decatized", "Steam Sponged"], 600.0, 540.0, 45.0, "5112"),
    ("FAB_SELVEDGE_DENIM", "Kuroki Japanese Indigo Selvedge Denim 14oz", "100% Ring-Spun Cotton", "7s Warp Rope-Dyed", "6s Weft Ring-Spun", 68, 44, 475.0, ["Sanforized", "Singeing"], 950.0, 780.0, 25.0, "5209")
]

INTERNATIONAL_FABRIC_MATRIX: Dict[str, YarnStructureSpec] = {
    code: YarnStructureSpec(
        fabric_id=code,
        commercial_trade_name=name,
        fiber_blend_ratio=blend,
        warp_yarn_count=warp,
        weft_yarn_count=weft,
        ends_per_inch=epi,
        picks_per_inch=ppi,
        weight_gsm=gsm,
        finishing_processes=finishes,
        tensile_strength_warp_n=ts_warp,
        tensile_strength_weft_n=ts_weft,
        air_permeability_cm3_per_s=air,
        hsn_tax_tariff=hsn
    )
    for code, name, blend, warp, weft, epi, ppi, gsm, finishes, ts_warp, ts_weft, air, hsn in FABRIC_SPECS
}
