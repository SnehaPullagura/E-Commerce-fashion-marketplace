"""
Textile Finishing Treatments, Functional Finishes & Chemical Processing Master Matrix.
Covers mechanical, thermal, and chemical textile finishing operations,
performance metrics, hand-feel transformations, and OEKO-TEX Standard 100 compliance.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel


class TextileFinishProtocol(BaseModel):
    finish_id: str
    finish_name: str
    finish_category: str  # "MECHANICAL_SURFACE", "THERMAL_SETTING", "BIO_ENZYMATIC", "CHEMICAL_FUNCTIONAL"
    purpose_and_effect: str
    applicable_fibers: List[str]
    hand_feel_transformation: str
    wash_durability_cycles: int
    oeko_tex_class_1_approved: bool
    environmental_hazard_rating: str  # "ZERO_DISCHARGE", "LOW_IMPACT", "MODERATE_RECLAIM", "RESTRICTED"


FINISH_DEFINITIONS = [
    ("FIN_SANFORIZED", "Sanforized Compressive Mechanical Shrinkage", "MECHANICAL_SURFACE", "Mechanically compacts warp yarns reducing residual laundry shrinkage to under 1%", ["Cotton", "Linen", "Denim", "Wool"], "Stable, dimensionally fixed hand", 999, True, "ZERO_DISCHARGE"),
    ("FIN_MERCERIZED", "Caustic Soda Mercerization Lustre Finish", "CHEMICAL_FUNCTIONAL", "Swells cotton fibers into cylindrical cross-section increasing tensile strength and light reflectance", ["Cotton", "Linen", "Cellulose"], "Silky, radiant sheen with enriched dye uptake", 999, True, "LOW_IMPACT"),
    ("FIN_BIO_POLISH", "Cellulase Bio-Enzymatic De-Pilling", "BIO_ENZYMATIC", "Hydrolyzes microscopic surface microfibrils preventing fuzz and pilling", ["Cotton", "Modal", "Lyocell"], "Buttery ultra-smooth peach-skin touch", 50, True, "ZERO_DISCHARGE"),
    ("FIN_DWR_ECO", "Fluorine-Free Eco Durable Water Repellent (PFC-Free)", "CHEMICAL_FUNCTIONAL", "Applies bio-based dendrimer barrier creating Lotus-leaf hydrophobic bead effect", ["Silk", "Wool", "Polyester", "Nylon"], "Supple drape with high surface tension water repellency", 40, True, "ZERO_DISCHARGE"),
    ("FIN_CALENDERED", "Heated Steel Cylinder Glazing & Chintz Calendering", "THERMAL_SETTING", "Flattens surface weave under 50 tons hydraulic pressure at 180°C", ["Silk", "Cotton", "Sateen"], "High-gloss mirror surface finish", 30, True, "LOW_IMPACT"),
    ("FIN_ANTIMICROBIAL", "Silver-Ion Bio-Static Odor Shield", "CHEMICAL_FUNCTIONAL", "Inhibits bacterial growth and odor-causing microbes on activewear", ["Merino Wool", "Performance Polyester"], "Fresh, odor-free breathable surface", 75, True, "ZERO_DISCHARGE"),
    ("FIN_CRUSH_WASH", "Artisanal Vintage Ozone Crushed Enzyme Wash", "BIO_ENZYMATIC", "Eco-friendly ozone gas wash imparting lived-in vintage patina without water waste", ["Denim", "Linen", "Hemp"], "Ultra-soft relaxed relaxed hand", 999, True, "ZERO_DISCHARGE")
]

TEXTILE_FINISH_CATALOG: Dict[str, TextileFinishProtocol] = {
    fid: TextileFinishProtocol(
        finish_id=fid,
        finish_name=name,
        finish_category=cat,
        purpose_and_effect=effect,
        applicable_fibers=fibers,
        hand_feel_transformation=feel,
        wash_durability_cycles=durability,
        oeko_tex_class_1_approved=oeko,
        environmental_hazard_rating=env
    )
    for fid, name, cat, effect, fibers, feel, durability, oeko, env in FINISH_DEFINITIONS
}
