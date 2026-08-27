"""
Textile Fiber Science & Chemical Polymer Engineering Master Database.
Contains physical tensile strength, elongation at break %, moisture regain,
drape coefficients, burning test characteristics, and environmental sustainability indices.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel

class FiberPolymerProfile(BaseModel):
    fiber_code: str
    fiber_common_name: str
    chemical_class: str
    tenacity_grams_per_denier: float
    elongation_at_break_pct: float
    standard_moisture_regain_pct: float
    specific_gravity: float
    burning_characteristics: str
    chemical_resistance_acid: str
    chemical_resistance_alkali: str
    thermal_decomposition_temp_c: int
    biodegradability_days: int
    gots_organic_certified: bool

FIBER_POLYMER_MASTER_DATABASE: Dict[str, FiberPolymerProfile] = {
    "FIBER_SILK_MULBERRY": FiberPolymerProfile(
        fiber_code="FIBER_SILK_MULBERRY",
        fiber_common_name="Mulberry Bombyx Mori Silk",
        chemical_class="Fibroin Protein",
        tenacity_grams_per_denier=4.5,
        elongation_at_break_pct=20.0,
        standard_moisture_regain_pct=11.0,
        specific_gravity=1.25,
        burning_characteristics="Burns slowly with crisp dark ash smelling of burning hair",
        chemical_resistance_acid="Vulnerable to strong mineral acids",
        chemical_resistance_alkali="Sensitive to strong alkalis",
        thermal_decomposition_temp_c=175,
        biodegradability_days=120,
        gots_organic_certified=True
    ),
    "FIBER_SILK_TUSSAR": FiberPolymerProfile(
        fiber_code="FIBER_SILK_TUSSAR",
        fiber_common_name="Wild Forest Tussar Kosa Silk",
        chemical_class="Fibroin Protein with Sericin",
        tenacity_grams_per_denier=3.8,
        elongation_at_break_pct=22.0,
        standard_moisture_regain_pct=11.5,
        specific_gravity=1.27,
        burning_characteristics="Burns with dark irregular ash and keratin odor",
        chemical_resistance_acid="Fair resistance to weak acids",
        chemical_resistance_alkali="Moderate resistance",
        thermal_decomposition_temp_c=170,
        biodegradability_days=140,
        gots_organic_certified=True
    ),
    "FIBER_COTTON_GIZA": FiberPolymerProfile(
        fiber_code="FIBER_COTTON_GIZA",
        fiber_common_name="Egyptian Giza Extra-Long Staple",
        chemical_class="Cellulose Polymer (94%)",
        tenacity_grams_per_denier=4.2,
        elongation_at_break_pct=7.0,
        standard_moisture_regain_pct=8.5,
        specific_gravity=1.54,
        burning_characteristics="Burns rapidly with yellow flame and burning paper odor",
        chemical_resistance_acid="Degraded by concentrated hot acids",
        chemical_resistance_alkali="Excellent resistance; swells in caustic soda (mercerization)",
        thermal_decomposition_temp_c=240,
        biodegradability_days=180,
        gots_organic_certified=True
    ),
    "FIBER_COTTON_SUPIMA": FiberPolymerProfile(
        fiber_code="FIBER_COTTON_SUPIMA",
        fiber_common_name="American Supima Pima Cotton",
        chemical_class="Cellulose Polymer (95%)",
        tenacity_grams_per_denier=4.0,
        elongation_at_break_pct=7.5,
        standard_moisture_regain_pct=8.5,
        specific_gravity=1.54,
        burning_characteristics="Burns cleanly with light grey feathery ash",
        chemical_resistance_acid="Sensitive to strong acids",
        chemical_resistance_alkali="Highly resistant to alkalis",
        thermal_decomposition_temp_c=240,
        biodegradability_days=180,
        gots_organic_certified=True
    ),
    "FIBER_FLAX_BELGIAN": FiberPolymerProfile(
        fiber_code="FIBER_FLAX_BELGIAN",
        fiber_common_name="Belgian Dew-Retted Flax Linen",
        chemical_class="Cellulose Polymer (70%) with Lignin",
        tenacity_grams_per_denier=6.5,
        elongation_at_break_pct=2.5,
        standard_moisture_regain_pct=12.0,
        specific_gravity=1.5,
        burning_characteristics="Burns with glowing yellow flame and light paper aroma",
        chemical_resistance_acid="Resistant to cold dilute acids",
        chemical_resistance_alkali="Highly resistant to alkalis and bleaching agents",
        thermal_decomposition_temp_c=260,
        biodegradability_days=150,
        gots_organic_certified=True
    ),
    "FIBER_HEMP_ORGANIC": FiberPolymerProfile(
        fiber_code="FIBER_HEMP_ORGANIC",
        fiber_common_name="Cannabis Sativa Industrial Hemp",
        chemical_class="Cellulose Polymer (75%) with Pectin",
        tenacity_grams_per_denier=7.0,
        elongation_at_break_pct=2.0,
        standard_moisture_regain_pct=12.5,
        specific_gravity=1.48,
        burning_characteristics="Burns like cotton; highly resistant to mildew and rot",
        chemical_resistance_acid="Resistant to mild acids",
        chemical_resistance_alkali="Excellent resistance to alkalis",
        thermal_decomposition_temp_c=270,
        biodegradability_days=120,
        gots_organic_certified=True
    ),
    "FIBER_CASHMERE_MONGOLIAN": FiberPolymerProfile(
        fiber_code="FIBER_CASHMERE_MONGOLIAN",
        fiber_common_name="Capra Hircus Cashmere Down",
        chemical_class="Keratin Protein Polymer",
        tenacity_grams_per_denier=3.2,
        elongation_at_break_pct=35.0,
        standard_moisture_regain_pct=16.0,
        specific_gravity=1.3,
        burning_characteristics="Burns with unsteady flame and protein smell; leaves black crushable bead",
        chemical_resistance_acid="Sensitive to chlorine and hot acids",
        chemical_resistance_alkali="Dissolves in hot caustic alkalis",
        thermal_decomposition_temp_c=130,
        biodegradability_days=90,
        gots_organic_certified=True
    ),
    "FIBER_MERINO_AUSTRALIAN": FiberPolymerProfile(
        fiber_code="FIBER_MERINO_AUSTRALIAN",
        fiber_common_name="19.5 Micron Superfine Merino Wool",
        chemical_class="Keratin Protein with Crimp",
        tenacity_grams_per_denier=3.5,
        elongation_at_break_pct=30.0,
        standard_moisture_regain_pct=15.0,
        specific_gravity=1.31,
        burning_characteristics="Burns slowly forming black hollow irregular bead",
        chemical_resistance_acid="Sensitive to oxidizing agents",
        chemical_resistance_alkali="Weakened by alkaline detergents",
        thermal_decomposition_temp_c=135,
        biodegradability_days=100,
        gots_organic_certified=True
    ),
    "FIBER_VICUNA_PERUVIAN": FiberPolymerProfile(
        fiber_code="FIBER_VICUNA_PERUVIAN",
        fiber_common_name="Wild Andean Vicuña Underdown (12um)",
        chemical_class="Fine Keratin Protein",
        tenacity_grams_per_denier=2.8,
        elongation_at_break_pct=38.0,
        standard_moisture_regain_pct=17.0,
        specific_gravity=1.28,
        burning_characteristics="Burns with faint keratin aroma leaving fragile porous bead",
        chemical_resistance_acid="Highly sensitive to chemicals",
        chemical_resistance_alkali="Avoid all strong chemical treatments",
        thermal_decomposition_temp_c=125,
        biodegradability_days=60,
        gots_organic_certified=True
    ),
    "FIBER_TENCEL_LYOCELL": FiberPolymerProfile(
        fiber_code="FIBER_TENCEL_LYOCELL",
        fiber_common_name="Lenzing TENCEL™ Wood Pulp Lyocell",
        chemical_class="Regenerated Cellulosic Nanofibrils",
        tenacity_grams_per_denier=4.8,
        elongation_at_break_pct=14.0,
        standard_moisture_regain_pct=11.5,
        specific_gravity=1.5,
        burning_characteristics="Burns like cotton with minimal white smoke and paper ash",
        chemical_resistance_acid="Similar to natural cotton",
        chemical_resistance_alkali="Good resistance in gentle processing",
        thermal_decomposition_temp_c=220,
        biodegradability_days=60,
        gots_organic_certified=True
    ),
    "FIBER_MODAL_BEECHWOOD": FiberPolymerProfile(
        fiber_code="FIBER_MODAL_BEECHWOOD",
        fiber_common_name="Lenzing Modal Beechwood Viscose",
        chemical_class="High Wet Modulus Cellulosic",
        tenacity_grams_per_denier=3.6,
        elongation_at_break_pct=15.0,
        standard_moisture_regain_pct=12.5,
        specific_gravity=1.52,
        burning_characteristics="Burns cleanly with slight papery smell",
        chemical_resistance_acid="Moderate acid resistance",
        chemical_resistance_alkali="Good alkali stability",
        thermal_decomposition_temp_c=210,
        biodegradability_days=90,
        gots_organic_certified=True
    ),
    "FIBER_CUPRO_BEMBERG": FiberPolymerProfile(
        fiber_code="FIBER_CUPRO_BEMBERG",
        fiber_common_name="Asahi Kasei Bemberg Cupro",
        chemical_class="Regenerated Cotton Linter Cellulose",
        tenacity_grams_per_denier=3.2,
        elongation_at_break_pct=18.0,
        standard_moisture_regain_pct=12.0,
        specific_gravity=1.5,
        burning_characteristics="Burns with gentle flame leaving soft white ash",
        chemical_resistance_acid="Moderate resistance",
        chemical_resistance_alkali="Good resistance",
        thermal_decomposition_temp_c=200,
        biodegradability_days=90,
        gots_organic_certified=True
    ),
    "FIBER_BAMBOO_ORGANIC": FiberPolymerProfile(
        fiber_code="FIBER_BAMBOO_ORGANIC",
        fiber_common_name="Mechanically Processed Bamboo Linen",
        chemical_class="Natural Cellulosic Bast",
        tenacity_grams_per_denier=4.0,
        elongation_at_break_pct=5.0,
        standard_moisture_regain_pct=13.0,
        specific_gravity=1.51,
        burning_characteristics="Burns like flax with earthy aroma",
        chemical_resistance_acid="Moderate resistance",
        chemical_resistance_alkali="Good resistance",
        thermal_decomposition_temp_c=230,
        biodegradability_days=120,
        gots_organic_certified=True
    ),
    "FIBER_RAMIE_NETTLE": FiberPolymerProfile(
        fiber_code="FIBER_RAMIE_NETTLE",
        fiber_common_name="Boehmeria Nivea Chinese Ramie",
        chemical_class="High-Crystalline Cellulose (85%)",
        tenacity_grams_per_denier=7.5,
        elongation_at_break_pct=2.0,
        standard_moisture_regain_pct=9.0,
        specific_gravity=1.51,
        burning_characteristics="Burns with steady yellow flame leaving minimal residue",
        chemical_resistance_acid="Highly resistant to cold acids",
        chemical_resistance_alkali="Unaffected by strong boiling alkalis",
        thermal_decomposition_temp_c=280,
        biodegradability_days=150,
        gots_organic_certified=True
    ),
    "FIBER_ZARI_SILVER_GILT": FiberPolymerProfile(
        fiber_code="FIBER_ZARI_SILVER_GILT",
        fiber_common_name="Silver Electroplated Real Metallic Zari",
        chemical_class="Electroplated Pure Silver Wire",
        tenacity_grams_per_denier=8.0,
        elongation_at_break_pct=1.0,
        standard_moisture_regain_pct=0.0,
        specific_gravity=10.5,
        burning_characteristics="Does not burn; conducts electricity and melts above 960°C",
        chemical_resistance_acid="Reacts with atmospheric sulphur forming tarnish",
        chemical_resistance_alkali="Inert to mild alkalis",
        thermal_decomposition_temp_c=960,
        biodegradability_days=99999,
        gots_organic_certified=False
    ),
}
