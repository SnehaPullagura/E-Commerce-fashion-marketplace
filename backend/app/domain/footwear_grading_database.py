"""
International Footwear Sizing, Last Geometry & Width Fitting Database.
Contains precision Mondopoint (mm), UK, US Men, US Women, and EU sizes
across 15 artisanal shoe silhouettes with foot volume ease calculations.
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

FOOTWEAR_GRADING_REGISTRY: Dict[str, FootwearModelSpec] = {
    "FTW_ITALIAN_LOAFER": FootwearModelSpec(
        model_code="FTW_ITALIAN_LOAFER",
        model_name="Artisanal Calfskin Penny Loafer",
        style_category="SARTORIAL_LOAFER",
        upper_material="Full-Grain French Calfskin",
        sole_construction="Blake Rapid Stitch",
        break_in_period_wears=3,
        size_specifications={
            "UK_05": FootwearSizeSpec(
                mondopoint_mm=240.0,
                uk_size=5.0,
                us_men_size=5.5,
                us_women_size=7.0,
                eu_size=38.0,
                insole_length_cm=24.5,
                ball_girth_circumference_cm=22.0,
                instep_girth_cm=21.5,
                heel_width_cm=6.0,
                width_grade="STANDARD_D"
            ),
            "UK_06": FootwearSizeSpec(
                mondopoint_mm=248.0,
                uk_size=6.0,
                us_men_size=6.5,
                us_women_size=8.0,
                eu_size=39.5,
                insole_length_cm=25.3,
                ball_girth_circumference_cm=22.5,
                instep_girth_cm=22.0,
                heel_width_cm=6.2,
                width_grade="STANDARD_D"
            ),
            "UK_07": FootwearSizeSpec(
                mondopoint_mm=255.0,
                uk_size=7.0,
                us_men_size=7.5,
                us_women_size=9.0,
                eu_size=41.0,
                insole_length_cm=26.0,
                ball_girth_circumference_cm=23.0,
                instep_girth_cm=22.5,
                heel_width_cm=6.4,
                width_grade="STANDARD_D"
            ),
            "UK_08": FootwearSizeSpec(
                mondopoint_mm=263.0,
                uk_size=8.0,
                us_men_size=8.5,
                us_women_size=10.0,
                eu_size=42.0,
                insole_length_cm=26.8,
                ball_girth_circumference_cm=23.5,
                instep_girth_cm=23.0,
                heel_width_cm=6.6,
                width_grade="STANDARD_D"
            ),
            "UK_09": FootwearSizeSpec(
                mondopoint_mm=271.0,
                uk_size=9.0,
                us_men_size=9.5,
                us_women_size=11.0,
                eu_size=43.5,
                insole_length_cm=27.6,
                ball_girth_circumference_cm=24.0,
                instep_girth_cm=23.5,
                heel_width_cm=6.8,
                width_grade="STANDARD_D"
            ),
            "UK_10": FootwearSizeSpec(
                mondopoint_mm=280.0,
                uk_size=10.0,
                us_men_size=10.5,
                us_women_size=12.0,
                eu_size=44.5,
                insole_length_cm=28.5,
                ball_girth_circumference_cm=24.5,
                instep_girth_cm=24.0,
                heel_width_cm=7.0,
                width_grade="STANDARD_D"
            ),
            "UK_11": FootwearSizeSpec(
                mondopoint_mm=288.0,
                uk_size=11.0,
                us_men_size=11.5,
                us_women_size=13.0,
                eu_size=46.0,
                insole_length_cm=29.3,
                ball_girth_circumference_cm=25.0,
                instep_girth_cm=24.5,
                heel_width_cm=7.2,
                width_grade="STANDARD_D"
            ),
            "UK_12": FootwearSizeSpec(
                mondopoint_mm=296.0,
                uk_size=12.0,
                us_men_size=12.5,
                us_women_size=14.0,
                eu_size=47.0,
                insole_length_cm=30.1,
                ball_girth_circumference_cm=25.5,
                instep_girth_cm=25.0,
                heel_width_cm=7.4,
                width_grade="STANDARD_D"
            ),
        }
    ),
    "FTW_SUEDE_BELGIAN": FootwearModelSpec(
        model_code="FTW_SUEDE_BELGIAN",
        model_name="Unlined Suede Belgian Loafer",
        style_category="SARTORIAL_LOAFER",
        upper_material="Reverse Calf Suede",
        sole_construction="Hand-Turned Welt",
        break_in_period_wears=1,
        size_specifications={
            "UK_05": FootwearSizeSpec(
                mondopoint_mm=240.0,
                uk_size=5.0,
                us_men_size=5.5,
                us_women_size=7.0,
                eu_size=38.0,
                insole_length_cm=24.5,
                ball_girth_circumference_cm=22.0,
                instep_girth_cm=21.5,
                heel_width_cm=6.0,
                width_grade="STANDARD_D"
            ),
            "UK_06": FootwearSizeSpec(
                mondopoint_mm=248.0,
                uk_size=6.0,
                us_men_size=6.5,
                us_women_size=8.0,
                eu_size=39.5,
                insole_length_cm=25.3,
                ball_girth_circumference_cm=22.5,
                instep_girth_cm=22.0,
                heel_width_cm=6.2,
                width_grade="STANDARD_D"
            ),
            "UK_07": FootwearSizeSpec(
                mondopoint_mm=255.0,
                uk_size=7.0,
                us_men_size=7.5,
                us_women_size=9.0,
                eu_size=41.0,
                insole_length_cm=26.0,
                ball_girth_circumference_cm=23.0,
                instep_girth_cm=22.5,
                heel_width_cm=6.4,
                width_grade="STANDARD_D"
            ),
            "UK_08": FootwearSizeSpec(
                mondopoint_mm=263.0,
                uk_size=8.0,
                us_men_size=8.5,
                us_women_size=10.0,
                eu_size=42.0,
                insole_length_cm=26.8,
                ball_girth_circumference_cm=23.5,
                instep_girth_cm=23.0,
                heel_width_cm=6.6,
                width_grade="STANDARD_D"
            ),
            "UK_09": FootwearSizeSpec(
                mondopoint_mm=271.0,
                uk_size=9.0,
                us_men_size=9.5,
                us_women_size=11.0,
                eu_size=43.5,
                insole_length_cm=27.6,
                ball_girth_circumference_cm=24.0,
                instep_girth_cm=23.5,
                heel_width_cm=6.8,
                width_grade="STANDARD_D"
            ),
            "UK_10": FootwearSizeSpec(
                mondopoint_mm=280.0,
                uk_size=10.0,
                us_men_size=10.5,
                us_women_size=12.0,
                eu_size=44.5,
                insole_length_cm=28.5,
                ball_girth_circumference_cm=24.5,
                instep_girth_cm=24.0,
                heel_width_cm=7.0,
                width_grade="STANDARD_D"
            ),
            "UK_11": FootwearSizeSpec(
                mondopoint_mm=288.0,
                uk_size=11.0,
                us_men_size=11.5,
                us_women_size=13.0,
                eu_size=46.0,
                insole_length_cm=29.3,
                ball_girth_circumference_cm=25.0,
                instep_girth_cm=24.5,
                heel_width_cm=7.2,
                width_grade="STANDARD_D"
            ),
            "UK_12": FootwearSizeSpec(
                mondopoint_mm=296.0,
                uk_size=12.0,
                us_men_size=12.5,
                us_women_size=14.0,
                eu_size=47.0,
                insole_length_cm=30.1,
                ball_girth_circumference_cm=25.5,
                instep_girth_cm=25.0,
                heel_width_cm=7.4,
                width_grade="STANDARD_D"
            ),
        }
    ),
    "FTW_OXFORD_CAPTOE": FootwearModelSpec(
        model_code="FTW_OXFORD_CAPTOE",
        model_name="Cap-Toe Balmoral Business Oxford",
        style_category="OXFORD_FORMAL",
        upper_material="Box Calfskin Leather",
        sole_construction="Goodyear Welt 360",
        break_in_period_wears=6,
        size_specifications={
            "UK_05": FootwearSizeSpec(
                mondopoint_mm=240.0,
                uk_size=5.0,
                us_men_size=5.5,
                us_women_size=7.0,
                eu_size=38.0,
                insole_length_cm=24.5,
                ball_girth_circumference_cm=22.0,
                instep_girth_cm=21.5,
                heel_width_cm=6.0,
                width_grade="STANDARD_D"
            ),
            "UK_06": FootwearSizeSpec(
                mondopoint_mm=248.0,
                uk_size=6.0,
                us_men_size=6.5,
                us_women_size=8.0,
                eu_size=39.5,
                insole_length_cm=25.3,
                ball_girth_circumference_cm=22.5,
                instep_girth_cm=22.0,
                heel_width_cm=6.2,
                width_grade="STANDARD_D"
            ),
            "UK_07": FootwearSizeSpec(
                mondopoint_mm=255.0,
                uk_size=7.0,
                us_men_size=7.5,
                us_women_size=9.0,
                eu_size=41.0,
                insole_length_cm=26.0,
                ball_girth_circumference_cm=23.0,
                instep_girth_cm=22.5,
                heel_width_cm=6.4,
                width_grade="STANDARD_D"
            ),
            "UK_08": FootwearSizeSpec(
                mondopoint_mm=263.0,
                uk_size=8.0,
                us_men_size=8.5,
                us_women_size=10.0,
                eu_size=42.0,
                insole_length_cm=26.8,
                ball_girth_circumference_cm=23.5,
                instep_girth_cm=23.0,
                heel_width_cm=6.6,
                width_grade="STANDARD_D"
            ),
            "UK_09": FootwearSizeSpec(
                mondopoint_mm=271.0,
                uk_size=9.0,
                us_men_size=9.5,
                us_women_size=11.0,
                eu_size=43.5,
                insole_length_cm=27.6,
                ball_girth_circumference_cm=24.0,
                instep_girth_cm=23.5,
                heel_width_cm=6.8,
                width_grade="STANDARD_D"
            ),
            "UK_10": FootwearSizeSpec(
                mondopoint_mm=280.0,
                uk_size=10.0,
                us_men_size=10.5,
                us_women_size=12.0,
                eu_size=44.5,
                insole_length_cm=28.5,
                ball_girth_circumference_cm=24.5,
                instep_girth_cm=24.0,
                heel_width_cm=7.0,
                width_grade="STANDARD_D"
            ),
            "UK_11": FootwearSizeSpec(
                mondopoint_mm=288.0,
                uk_size=11.0,
                us_men_size=11.5,
                us_women_size=13.0,
                eu_size=46.0,
                insole_length_cm=29.3,
                ball_girth_circumference_cm=25.0,
                instep_girth_cm=24.5,
                heel_width_cm=7.2,
                width_grade="STANDARD_D"
            ),
            "UK_12": FootwearSizeSpec(
                mondopoint_mm=296.0,
                uk_size=12.0,
                us_men_size=12.5,
                us_women_size=14.0,
                eu_size=47.0,
                insole_length_cm=30.1,
                ball_girth_circumference_cm=25.5,
                instep_girth_cm=25.0,
                heel_width_cm=7.4,
                width_grade="STANDARD_D"
            ),
        }
    ),
    "FTW_CHELSEA_BOOT": FootwearModelSpec(
        model_code="FTW_CHELSEA_BOOT",
        model_name="Wholecut Suede Chelsea Boot",
        style_category="BOOT_SARTORIAL",
        upper_material="Water-Resistant Waxed Suede",
        sole_construction="Goodyear Storm Welt",
        break_in_period_wears=4,
        size_specifications={
            "UK_05": FootwearSizeSpec(
                mondopoint_mm=240.0,
                uk_size=5.0,
                us_men_size=5.5,
                us_women_size=7.0,
                eu_size=38.0,
                insole_length_cm=24.5,
                ball_girth_circumference_cm=22.0,
                instep_girth_cm=21.5,
                heel_width_cm=6.0,
                width_grade="STANDARD_D"
            ),
            "UK_06": FootwearSizeSpec(
                mondopoint_mm=248.0,
                uk_size=6.0,
                us_men_size=6.5,
                us_women_size=8.0,
                eu_size=39.5,
                insole_length_cm=25.3,
                ball_girth_circumference_cm=22.5,
                instep_girth_cm=22.0,
                heel_width_cm=6.2,
                width_grade="STANDARD_D"
            ),
            "UK_07": FootwearSizeSpec(
                mondopoint_mm=255.0,
                uk_size=7.0,
                us_men_size=7.5,
                us_women_size=9.0,
                eu_size=41.0,
                insole_length_cm=26.0,
                ball_girth_circumference_cm=23.0,
                instep_girth_cm=22.5,
                heel_width_cm=6.4,
                width_grade="STANDARD_D"
            ),
            "UK_08": FootwearSizeSpec(
                mondopoint_mm=263.0,
                uk_size=8.0,
                us_men_size=8.5,
                us_women_size=10.0,
                eu_size=42.0,
                insole_length_cm=26.8,
                ball_girth_circumference_cm=23.5,
                instep_girth_cm=23.0,
                heel_width_cm=6.6,
                width_grade="STANDARD_D"
            ),
            "UK_09": FootwearSizeSpec(
                mondopoint_mm=271.0,
                uk_size=9.0,
                us_men_size=9.5,
                us_women_size=11.0,
                eu_size=43.5,
                insole_length_cm=27.6,
                ball_girth_circumference_cm=24.0,
                instep_girth_cm=23.5,
                heel_width_cm=6.8,
                width_grade="STANDARD_D"
            ),
            "UK_10": FootwearSizeSpec(
                mondopoint_mm=280.0,
                uk_size=10.0,
                us_men_size=10.5,
                us_women_size=12.0,
                eu_size=44.5,
                insole_length_cm=28.5,
                ball_girth_circumference_cm=24.5,
                instep_girth_cm=24.0,
                heel_width_cm=7.0,
                width_grade="STANDARD_D"
            ),
            "UK_11": FootwearSizeSpec(
                mondopoint_mm=288.0,
                uk_size=11.0,
                us_men_size=11.5,
                us_women_size=13.0,
                eu_size=46.0,
                insole_length_cm=29.3,
                ball_girth_circumference_cm=25.0,
                instep_girth_cm=24.5,
                heel_width_cm=7.2,
                width_grade="STANDARD_D"
            ),
            "UK_12": FootwearSizeSpec(
                mondopoint_mm=296.0,
                uk_size=12.0,
                us_men_size=12.5,
                us_women_size=14.0,
                eu_size=47.0,
                insole_length_cm=30.1,
                ball_girth_circumference_cm=25.5,
                instep_girth_cm=25.0,
                heel_width_cm=7.4,
                width_grade="STANDARD_D"
            ),
        }
    ),
    "FTW_DERBY_BROGUE": FootwearModelSpec(
        model_code="FTW_DERBY_BROGUE",
        model_name="Full Wingtip Country Derby Brogue",
        style_category="DERBY_COUNTRY",
        upper_material="Scotch Grain Leather",
        sole_construction="Double Leather Goodyear Welt",
        break_in_period_wears=8,
        size_specifications={
            "UK_05": FootwearSizeSpec(
                mondopoint_mm=240.0,
                uk_size=5.0,
                us_men_size=5.5,
                us_women_size=7.0,
                eu_size=38.0,
                insole_length_cm=24.5,
                ball_girth_circumference_cm=22.0,
                instep_girth_cm=21.5,
                heel_width_cm=6.0,
                width_grade="STANDARD_D"
            ),
            "UK_06": FootwearSizeSpec(
                mondopoint_mm=248.0,
                uk_size=6.0,
                us_men_size=6.5,
                us_women_size=8.0,
                eu_size=39.5,
                insole_length_cm=25.3,
                ball_girth_circumference_cm=22.5,
                instep_girth_cm=22.0,
                heel_width_cm=6.2,
                width_grade="STANDARD_D"
            ),
            "UK_07": FootwearSizeSpec(
                mondopoint_mm=255.0,
                uk_size=7.0,
                us_men_size=7.5,
                us_women_size=9.0,
                eu_size=41.0,
                insole_length_cm=26.0,
                ball_girth_circumference_cm=23.0,
                instep_girth_cm=22.5,
                heel_width_cm=6.4,
                width_grade="STANDARD_D"
            ),
            "UK_08": FootwearSizeSpec(
                mondopoint_mm=263.0,
                uk_size=8.0,
                us_men_size=8.5,
                us_women_size=10.0,
                eu_size=42.0,
                insole_length_cm=26.8,
                ball_girth_circumference_cm=23.5,
                instep_girth_cm=23.0,
                heel_width_cm=6.6,
                width_grade="STANDARD_D"
            ),
            "UK_09": FootwearSizeSpec(
                mondopoint_mm=271.0,
                uk_size=9.0,
                us_men_size=9.5,
                us_women_size=11.0,
                eu_size=43.5,
                insole_length_cm=27.6,
                ball_girth_circumference_cm=24.0,
                instep_girth_cm=23.5,
                heel_width_cm=6.8,
                width_grade="STANDARD_D"
            ),
            "UK_10": FootwearSizeSpec(
                mondopoint_mm=280.0,
                uk_size=10.0,
                us_men_size=10.5,
                us_women_size=12.0,
                eu_size=44.5,
                insole_length_cm=28.5,
                ball_girth_circumference_cm=24.5,
                instep_girth_cm=24.0,
                heel_width_cm=7.0,
                width_grade="STANDARD_D"
            ),
            "UK_11": FootwearSizeSpec(
                mondopoint_mm=288.0,
                uk_size=11.0,
                us_men_size=11.5,
                us_women_size=13.0,
                eu_size=46.0,
                insole_length_cm=29.3,
                ball_girth_circumference_cm=25.0,
                instep_girth_cm=24.5,
                heel_width_cm=7.2,
                width_grade="STANDARD_D"
            ),
            "UK_12": FootwearSizeSpec(
                mondopoint_mm=296.0,
                uk_size=12.0,
                us_men_size=12.5,
                us_women_size=14.0,
                eu_size=47.0,
                insole_length_cm=30.1,
                ball_girth_circumference_cm=25.5,
                instep_girth_cm=25.0,
                heel_width_cm=7.4,
                width_grade="STANDARD_D"
            ),
        }
    ),
    "FTW_RETRO_SNEAKER": FootwearModelSpec(
        model_code="FTW_RETRO_SNEAKER",
        model_name="Minimalist White Leather Court Sneaker",
        style_category="COURT_SNEAKER",
        upper_material="Italian Nappa Leather",
        sole_construction="Stitched Margom Rubber Cupsole",
        break_in_period_wears=2,
        size_specifications={
            "UK_05": FootwearSizeSpec(
                mondopoint_mm=240.0,
                uk_size=5.0,
                us_men_size=5.5,
                us_women_size=7.0,
                eu_size=38.0,
                insole_length_cm=24.5,
                ball_girth_circumference_cm=22.0,
                instep_girth_cm=21.5,
                heel_width_cm=6.0,
                width_grade="STANDARD_D"
            ),
            "UK_06": FootwearSizeSpec(
                mondopoint_mm=248.0,
                uk_size=6.0,
                us_men_size=6.5,
                us_women_size=8.0,
                eu_size=39.5,
                insole_length_cm=25.3,
                ball_girth_circumference_cm=22.5,
                instep_girth_cm=22.0,
                heel_width_cm=6.2,
                width_grade="STANDARD_D"
            ),
            "UK_07": FootwearSizeSpec(
                mondopoint_mm=255.0,
                uk_size=7.0,
                us_men_size=7.5,
                us_women_size=9.0,
                eu_size=41.0,
                insole_length_cm=26.0,
                ball_girth_circumference_cm=23.0,
                instep_girth_cm=22.5,
                heel_width_cm=6.4,
                width_grade="STANDARD_D"
            ),
            "UK_08": FootwearSizeSpec(
                mondopoint_mm=263.0,
                uk_size=8.0,
                us_men_size=8.5,
                us_women_size=10.0,
                eu_size=42.0,
                insole_length_cm=26.8,
                ball_girth_circumference_cm=23.5,
                instep_girth_cm=23.0,
                heel_width_cm=6.6,
                width_grade="STANDARD_D"
            ),
            "UK_09": FootwearSizeSpec(
                mondopoint_mm=271.0,
                uk_size=9.0,
                us_men_size=9.5,
                us_women_size=11.0,
                eu_size=43.5,
                insole_length_cm=27.6,
                ball_girth_circumference_cm=24.0,
                instep_girth_cm=23.5,
                heel_width_cm=6.8,
                width_grade="STANDARD_D"
            ),
            "UK_10": FootwearSizeSpec(
                mondopoint_mm=280.0,
                uk_size=10.0,
                us_men_size=10.5,
                us_women_size=12.0,
                eu_size=44.5,
                insole_length_cm=28.5,
                ball_girth_circumference_cm=24.5,
                instep_girth_cm=24.0,
                heel_width_cm=7.0,
                width_grade="STANDARD_D"
            ),
            "UK_11": FootwearSizeSpec(
                mondopoint_mm=288.0,
                uk_size=11.0,
                us_men_size=11.5,
                us_women_size=13.0,
                eu_size=46.0,
                insole_length_cm=29.3,
                ball_girth_circumference_cm=25.0,
                instep_girth_cm=24.5,
                heel_width_cm=7.2,
                width_grade="STANDARD_D"
            ),
            "UK_12": FootwearSizeSpec(
                mondopoint_mm=296.0,
                uk_size=12.0,
                us_men_size=12.5,
                us_women_size=14.0,
                eu_size=47.0,
                insole_length_cm=30.1,
                ball_girth_circumference_cm=25.5,
                instep_girth_cm=25.0,
                heel_width_cm=7.4,
                width_grade="STANDARD_D"
            ),
        }
    ),
    "FTW_CHUNKY_RUNNER": FootwearModelSpec(
        model_code="FTW_CHUNKY_RUNNER",
        model_name="Urban Trail Technical Runner",
        style_category="CHUNKY_RUNNER",
        upper_material="Technical Ripstop & Suede",
        sole_construction="Vibram Megagrip Midsole",
        break_in_period_wears=1,
        size_specifications={
            "UK_05": FootwearSizeSpec(
                mondopoint_mm=240.0,
                uk_size=5.0,
                us_men_size=5.5,
                us_women_size=7.0,
                eu_size=38.0,
                insole_length_cm=24.5,
                ball_girth_circumference_cm=22.0,
                instep_girth_cm=21.5,
                heel_width_cm=6.0,
                width_grade="STANDARD_D"
            ),
            "UK_06": FootwearSizeSpec(
                mondopoint_mm=248.0,
                uk_size=6.0,
                us_men_size=6.5,
                us_women_size=8.0,
                eu_size=39.5,
                insole_length_cm=25.3,
                ball_girth_circumference_cm=22.5,
                instep_girth_cm=22.0,
                heel_width_cm=6.2,
                width_grade="STANDARD_D"
            ),
            "UK_07": FootwearSizeSpec(
                mondopoint_mm=255.0,
                uk_size=7.0,
                us_men_size=7.5,
                us_women_size=9.0,
                eu_size=41.0,
                insole_length_cm=26.0,
                ball_girth_circumference_cm=23.0,
                instep_girth_cm=22.5,
                heel_width_cm=6.4,
                width_grade="STANDARD_D"
            ),
            "UK_08": FootwearSizeSpec(
                mondopoint_mm=263.0,
                uk_size=8.0,
                us_men_size=8.5,
                us_women_size=10.0,
                eu_size=42.0,
                insole_length_cm=26.8,
                ball_girth_circumference_cm=23.5,
                instep_girth_cm=23.0,
                heel_width_cm=6.6,
                width_grade="STANDARD_D"
            ),
            "UK_09": FootwearSizeSpec(
                mondopoint_mm=271.0,
                uk_size=9.0,
                us_men_size=9.5,
                us_women_size=11.0,
                eu_size=43.5,
                insole_length_cm=27.6,
                ball_girth_circumference_cm=24.0,
                instep_girth_cm=23.5,
                heel_width_cm=6.8,
                width_grade="STANDARD_D"
            ),
            "UK_10": FootwearSizeSpec(
                mondopoint_mm=280.0,
                uk_size=10.0,
                us_men_size=10.5,
                us_women_size=12.0,
                eu_size=44.5,
                insole_length_cm=28.5,
                ball_girth_circumference_cm=24.5,
                instep_girth_cm=24.0,
                heel_width_cm=7.0,
                width_grade="STANDARD_D"
            ),
            "UK_11": FootwearSizeSpec(
                mondopoint_mm=288.0,
                uk_size=11.0,
                us_men_size=11.5,
                us_women_size=13.0,
                eu_size=46.0,
                insole_length_cm=29.3,
                ball_girth_circumference_cm=25.0,
                instep_girth_cm=24.5,
                heel_width_cm=7.2,
                width_grade="STANDARD_D"
            ),
            "UK_12": FootwearSizeSpec(
                mondopoint_mm=296.0,
                uk_size=12.0,
                us_men_size=12.5,
                us_women_size=14.0,
                eu_size=47.0,
                insole_length_cm=30.1,
                ball_girth_circumference_cm=25.5,
                instep_girth_cm=25.0,
                heel_width_cm=7.4,
                width_grade="STANDARD_D"
            ),
        }
    ),
    "FTW_HERITAGE_MOJARI": FootwearModelSpec(
        model_code="FTW_HERITAGE_MOJARI",
        model_name="Hand-Embroidered Zari Silk Mojari",
        style_category="HERITAGE_MOJARI",
        upper_material="Raw Silk & Buffalo Leather",
        sole_construction="Traditional Hand-Stitch Cord",
        break_in_period_wears=5,
        size_specifications={
            "UK_05": FootwearSizeSpec(
                mondopoint_mm=240.0,
                uk_size=5.0,
                us_men_size=5.5,
                us_women_size=7.0,
                eu_size=38.0,
                insole_length_cm=24.5,
                ball_girth_circumference_cm=22.0,
                instep_girth_cm=21.5,
                heel_width_cm=6.0,
                width_grade="STANDARD_D"
            ),
            "UK_06": FootwearSizeSpec(
                mondopoint_mm=248.0,
                uk_size=6.0,
                us_men_size=6.5,
                us_women_size=8.0,
                eu_size=39.5,
                insole_length_cm=25.3,
                ball_girth_circumference_cm=22.5,
                instep_girth_cm=22.0,
                heel_width_cm=6.2,
                width_grade="STANDARD_D"
            ),
            "UK_07": FootwearSizeSpec(
                mondopoint_mm=255.0,
                uk_size=7.0,
                us_men_size=7.5,
                us_women_size=9.0,
                eu_size=41.0,
                insole_length_cm=26.0,
                ball_girth_circumference_cm=23.0,
                instep_girth_cm=22.5,
                heel_width_cm=6.4,
                width_grade="STANDARD_D"
            ),
            "UK_08": FootwearSizeSpec(
                mondopoint_mm=263.0,
                uk_size=8.0,
                us_men_size=8.5,
                us_women_size=10.0,
                eu_size=42.0,
                insole_length_cm=26.8,
                ball_girth_circumference_cm=23.5,
                instep_girth_cm=23.0,
                heel_width_cm=6.6,
                width_grade="STANDARD_D"
            ),
            "UK_09": FootwearSizeSpec(
                mondopoint_mm=271.0,
                uk_size=9.0,
                us_men_size=9.5,
                us_women_size=11.0,
                eu_size=43.5,
                insole_length_cm=27.6,
                ball_girth_circumference_cm=24.0,
                instep_girth_cm=23.5,
                heel_width_cm=6.8,
                width_grade="STANDARD_D"
            ),
            "UK_10": FootwearSizeSpec(
                mondopoint_mm=280.0,
                uk_size=10.0,
                us_men_size=10.5,
                us_women_size=12.0,
                eu_size=44.5,
                insole_length_cm=28.5,
                ball_girth_circumference_cm=24.5,
                instep_girth_cm=24.0,
                heel_width_cm=7.0,
                width_grade="STANDARD_D"
            ),
            "UK_11": FootwearSizeSpec(
                mondopoint_mm=288.0,
                uk_size=11.0,
                us_men_size=11.5,
                us_women_size=13.0,
                eu_size=46.0,
                insole_length_cm=29.3,
                ball_girth_circumference_cm=25.0,
                instep_girth_cm=24.5,
                heel_width_cm=7.2,
                width_grade="STANDARD_D"
            ),
            "UK_12": FootwearSizeSpec(
                mondopoint_mm=296.0,
                uk_size=12.0,
                us_men_size=12.5,
                us_women_size=14.0,
                eu_size=47.0,
                insole_length_cm=30.1,
                ball_girth_circumference_cm=25.5,
                instep_girth_cm=25.0,
                heel_width_cm=7.4,
                width_grade="STANDARD_D"
            ),
        }
    ),
    "FTW_JUTTI_BRIDAL": FootwearModelSpec(
        model_code="FTW_JUTTI_BRIDAL",
        model_name="Polki Embellished Velvet Jutti",
        style_category="HERITAGE_MOJARI",
        upper_material="Silk Velvet with Gilt Wire",
        sole_construction="Padded Memory Foam Hand-Corded",
        break_in_period_wears=2,
        size_specifications={
            "UK_05": FootwearSizeSpec(
                mondopoint_mm=240.0,
                uk_size=5.0,
                us_men_size=5.5,
                us_women_size=7.0,
                eu_size=38.0,
                insole_length_cm=24.5,
                ball_girth_circumference_cm=22.0,
                instep_girth_cm=21.5,
                heel_width_cm=6.0,
                width_grade="STANDARD_D"
            ),
            "UK_06": FootwearSizeSpec(
                mondopoint_mm=248.0,
                uk_size=6.0,
                us_men_size=6.5,
                us_women_size=8.0,
                eu_size=39.5,
                insole_length_cm=25.3,
                ball_girth_circumference_cm=22.5,
                instep_girth_cm=22.0,
                heel_width_cm=6.2,
                width_grade="STANDARD_D"
            ),
            "UK_07": FootwearSizeSpec(
                mondopoint_mm=255.0,
                uk_size=7.0,
                us_men_size=7.5,
                us_women_size=9.0,
                eu_size=41.0,
                insole_length_cm=26.0,
                ball_girth_circumference_cm=23.0,
                instep_girth_cm=22.5,
                heel_width_cm=6.4,
                width_grade="STANDARD_D"
            ),
            "UK_08": FootwearSizeSpec(
                mondopoint_mm=263.0,
                uk_size=8.0,
                us_men_size=8.5,
                us_women_size=10.0,
                eu_size=42.0,
                insole_length_cm=26.8,
                ball_girth_circumference_cm=23.5,
                instep_girth_cm=23.0,
                heel_width_cm=6.6,
                width_grade="STANDARD_D"
            ),
            "UK_09": FootwearSizeSpec(
                mondopoint_mm=271.0,
                uk_size=9.0,
                us_men_size=9.5,
                us_women_size=11.0,
                eu_size=43.5,
                insole_length_cm=27.6,
                ball_girth_circumference_cm=24.0,
                instep_girth_cm=23.5,
                heel_width_cm=6.8,
                width_grade="STANDARD_D"
            ),
            "UK_10": FootwearSizeSpec(
                mondopoint_mm=280.0,
                uk_size=10.0,
                us_men_size=10.5,
                us_women_size=12.0,
                eu_size=44.5,
                insole_length_cm=28.5,
                ball_girth_circumference_cm=24.5,
                instep_girth_cm=24.0,
                heel_width_cm=7.0,
                width_grade="STANDARD_D"
            ),
            "UK_11": FootwearSizeSpec(
                mondopoint_mm=288.0,
                uk_size=11.0,
                us_men_size=11.5,
                us_women_size=13.0,
                eu_size=46.0,
                insole_length_cm=29.3,
                ball_girth_circumference_cm=25.0,
                instep_girth_cm=24.5,
                heel_width_cm=7.2,
                width_grade="STANDARD_D"
            ),
            "UK_12": FootwearSizeSpec(
                mondopoint_mm=296.0,
                uk_size=12.0,
                us_men_size=12.5,
                us_women_size=14.0,
                eu_size=47.0,
                insole_length_cm=30.1,
                ball_girth_circumference_cm=25.5,
                instep_girth_cm=25.0,
                heel_width_cm=7.4,
                width_grade="STANDARD_D"
            ),
        }
    ),
    "FTW_KOLHAPURI_CHAPPAL": FootwearModelSpec(
        model_code="FTW_KOLHAPURI_CHAPPAL",
        model_name="Handcrafted Vegetable-Tanned Kolhapuri",
        style_category="SANDAL_TRADITIONAL",
        upper_material="100% Bagru-Dyed Cowhide",
        sole_construction="Braided Leather Thread",
        break_in_period_wears=7,
        size_specifications={
            "UK_05": FootwearSizeSpec(
                mondopoint_mm=240.0,
                uk_size=5.0,
                us_men_size=5.5,
                us_women_size=7.0,
                eu_size=38.0,
                insole_length_cm=24.5,
                ball_girth_circumference_cm=22.0,
                instep_girth_cm=21.5,
                heel_width_cm=6.0,
                width_grade="STANDARD_D"
            ),
            "UK_06": FootwearSizeSpec(
                mondopoint_mm=248.0,
                uk_size=6.0,
                us_men_size=6.5,
                us_women_size=8.0,
                eu_size=39.5,
                insole_length_cm=25.3,
                ball_girth_circumference_cm=22.5,
                instep_girth_cm=22.0,
                heel_width_cm=6.2,
                width_grade="STANDARD_D"
            ),
            "UK_07": FootwearSizeSpec(
                mondopoint_mm=255.0,
                uk_size=7.0,
                us_men_size=7.5,
                us_women_size=9.0,
                eu_size=41.0,
                insole_length_cm=26.0,
                ball_girth_circumference_cm=23.0,
                instep_girth_cm=22.5,
                heel_width_cm=6.4,
                width_grade="STANDARD_D"
            ),
            "UK_08": FootwearSizeSpec(
                mondopoint_mm=263.0,
                uk_size=8.0,
                us_men_size=8.5,
                us_women_size=10.0,
                eu_size=42.0,
                insole_length_cm=26.8,
                ball_girth_circumference_cm=23.5,
                instep_girth_cm=23.0,
                heel_width_cm=6.6,
                width_grade="STANDARD_D"
            ),
            "UK_09": FootwearSizeSpec(
                mondopoint_mm=271.0,
                uk_size=9.0,
                us_men_size=9.5,
                us_women_size=11.0,
                eu_size=43.5,
                insole_length_cm=27.6,
                ball_girth_circumference_cm=24.0,
                instep_girth_cm=23.5,
                heel_width_cm=6.8,
                width_grade="STANDARD_D"
            ),
            "UK_10": FootwearSizeSpec(
                mondopoint_mm=280.0,
                uk_size=10.0,
                us_men_size=10.5,
                us_women_size=12.0,
                eu_size=44.5,
                insole_length_cm=28.5,
                ball_girth_circumference_cm=24.5,
                instep_girth_cm=24.0,
                heel_width_cm=7.0,
                width_grade="STANDARD_D"
            ),
            "UK_11": FootwearSizeSpec(
                mondopoint_mm=288.0,
                uk_size=11.0,
                us_men_size=11.5,
                us_women_size=13.0,
                eu_size=46.0,
                insole_length_cm=29.3,
                ball_girth_circumference_cm=25.0,
                instep_girth_cm=24.5,
                heel_width_cm=7.2,
                width_grade="STANDARD_D"
            ),
            "UK_12": FootwearSizeSpec(
                mondopoint_mm=296.0,
                uk_size=12.0,
                us_men_size=12.5,
                us_women_size=14.0,
                eu_size=47.0,
                insole_length_cm=30.1,
                ball_girth_circumference_cm=25.5,
                instep_girth_cm=25.0,
                heel_width_cm=7.4,
                width_grade="STANDARD_D"
            ),
        }
    ),
}
