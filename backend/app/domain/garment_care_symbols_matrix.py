"""
ISO 3758 & ASTM D5489 International Garment Care Labelling Master Matrix.
Contains standardized textile care symbols, temperature thresholds,
chemical restrictions, mechanical agitation limits, and customer laundry directives.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel


class CareSymbolDefinition(BaseModel):
    symbol_code: str
    iso_category: str  # "WASHING", "BLEACHING", "DRYING", "IRONING", "PROFESSIONAL_CLEANING"
    symbol_unicode_icon: str
    standard_name: str
    action_directive: str
    temperature_celsius_limit: Optional[int] = None
    prohibited_actions: List[str]
    recommended_fabrics: List[str]
    consumer_plain_english_note: str


CARE_DEFINITIONS = [
    ("SYM_WASH_30", "WASHING", "🛁 30°", "Machine Wash 30°C Delicate", "Wash at or below 30°C with gentle cycle and reduced spin", 30, ["Do not boil", "Do not wring"], ["Mulberry Silk", "Cashmere Blend", "Fine Modal"], "Delicate cold wash only"),
    ("SYM_WASH_40", "WASHING", "🛁 40°", "Machine Wash 40°C Standard", "Wash at or below 40°C with normal mechanical action", 40, ["Do not wash above 40°C"], ["100% Cotton Poplin", "Linen", "Denim"], "Standard warm wash"),
    ("SYM_HAND_ONLY", "WASHING", "🖐️ 20°", "Hand Wash Only Cold", "Hand wash cold at maximum 20°C using pH-neutral silk detergent", 20, ["No machine agitation", "No spin cycle"], ["Chiffon Silk", "Organza", "Pashmina"], "Hand wash in cold water with gentle squeeze"),
    ("SYM_NO_BLEACH", "BLEACHING", "🔺✖️", "Do Not Bleach", "Do not use chlorine or oxygen-based bleach", None, ["Chlorine bleach prohibited"], ["All dyed fabrics", "Silk", "Wool"], "Do not use bleach products"),
    ("SYM_LINE_DRY", "DRYING", "👕 ☀️", "Line Dry in Shade", "Hang garment to dry vertically in shade out of direct sunlight", None, ["No tumble dry", "No direct UV exposure"], ["Linen", "Wool Knitwear", "Silk Blends"], "Hang to dry away from strong sun"),
    ("SYM_IRON_LOW", "IRONING", "🏷️ •", "Iron Low Temperature (110°C)", "Steam or dry iron at soleplate temperature up to 110°C", 110, ["No high heat", "Do not press on velvet pile"], ["Silk", "Rayon", "Acetate"], "Use low heat iron with press cloth"),
    ("SYM_DRY_CLEAN_P", "PROFESSIONAL_CLEANING", "⭕ P", "Professional Dry Clean Tetrachloroethene", "Professional dry clean with perchlorethylene and normal cycle", None, ["Do not wash in home machine"], ["Tailored Suits", "Brocade", "Heavy Outerwear"], "Dry clean only by specialist")
]

CARE_SYMBOLS_MASTER_REGISTRY: Dict[str, CareSymbolDefinition] = {
    code: CareSymbolDefinition(
        symbol_code=code,
        iso_category=cat,
        symbol_unicode_icon=icon,
        standard_name=name,
        action_directive=directive,
        temperature_celsius_limit=temp,
        prohibited_actions=prohib,
        recommended_fabrics=fabrics,
        consumer_plain_english_note=note
    )
    for code, cat, icon, name, directive, temp, prohib, fabrics, note in CARE_DEFINITIONS
}
