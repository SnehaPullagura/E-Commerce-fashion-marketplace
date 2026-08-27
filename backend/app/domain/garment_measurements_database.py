"""
Comprehensive Garment Anthropometric Measurement & Grading Specification Database.
Defines grade increments, tolerance thresholds, and dimensional specifications
for 120+ standard fashion silhouettes across 8 international sizes (XXS to 3XL).
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

class GarmentSizeSpec(BaseModel):
    size_label: str
    chest_circumference_in: float
    waist_circumference_in: float
    hip_circumference_in: float
    garment_length_in: float
    shoulder_width_in: float
    sleeve_length_in: float
    bicep_circumference_in: float
    neck_circumference_in: float
    tolerance_margin_in: float = 0.5

class SilhouetteGradingChart(BaseModel):
    silhouette_code: str
    silhouette_name: str
    gender: str
    category: str
    fit_type: str
    sizes: Dict[str, GarmentSizeSpec]

GARMENT_MEASUREMENT_DATABASE: Dict[str, SilhouetteGradingChart] = {
    "M_SHIRT_SLIM": SilhouetteGradingChart(
        silhouette_code="M_SHIRT_SLIM",
        silhouette_name="Men's Slim Fit Oxford Shirt",
        gender="MEN",
        category="TOPS",
        fit_type="SLIM",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=32.0,
                waist_circumference_in=27.0,
                hip_circumference_in=32.0,
                garment_length_in=27.5,
                shoulder_width_in=15.7,
                sleeve_length_in=23.9,
                bicep_circumference_in=12.5,
                neck_circumference_in=13.9
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=34.0,
                waist_circumference_in=29.0,
                hip_circumference_in=34.0,
                garment_length_in=28.0,
                shoulder_width_in=16.1,
                sleeve_length_in=24.2,
                bicep_circumference_in=13.0,
                neck_circumference_in=14.2
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=36.0,
                waist_circumference_in=31.0,
                hip_circumference_in=36.0,
                garment_length_in=28.5,
                shoulder_width_in=16.5,
                sleeve_length_in=24.5,
                bicep_circumference_in=13.5,
                neck_circumference_in=14.5
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=38.0,
                waist_circumference_in=33.0,
                hip_circumference_in=38.0,
                garment_length_in=29.0,
                shoulder_width_in=16.9,
                sleeve_length_in=24.8,
                bicep_circumference_in=14.0,
                neck_circumference_in=14.8
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=40.0,
                waist_circumference_in=35.0,
                hip_circumference_in=40.0,
                garment_length_in=29.5,
                shoulder_width_in=17.3,
                sleeve_length_in=25.1,
                bicep_circumference_in=14.5,
                neck_circumference_in=15.1
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=42.0,
                waist_circumference_in=37.0,
                hip_circumference_in=42.0,
                garment_length_in=30.0,
                shoulder_width_in=17.7,
                sleeve_length_in=25.4,
                bicep_circumference_in=15.0,
                neck_circumference_in=15.4
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=44.0,
                waist_circumference_in=39.0,
                hip_circumference_in=44.0,
                garment_length_in=30.5,
                shoulder_width_in=18.1,
                sleeve_length_in=25.7,
                bicep_circumference_in=15.5,
                neck_circumference_in=15.7
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=46.0,
                waist_circumference_in=41.0,
                hip_circumference_in=46.0,
                garment_length_in=31.0,
                shoulder_width_in=18.5,
                sleeve_length_in=26.0,
                bicep_circumference_in=16.0,
                neck_circumference_in=16.0
            ),
        }
    ),
    "M_SHIRT_REG": SilhouetteGradingChart(
        silhouette_code="M_SHIRT_REG",
        silhouette_name="Men's Regular Fit Business Shirt",
        gender="MEN",
        category="TOPS",
        fit_type="REGULAR",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=34.0,
                waist_circumference_in=30.0,
                hip_circumference_in=34.0,
                garment_length_in=28.5,
                shoulder_width_in=16.7,
                sleeve_length_in=24.4,
                bicep_circumference_in=13.5,
                neck_circumference_in=14.4
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=36.0,
                waist_circumference_in=32.0,
                hip_circumference_in=36.0,
                garment_length_in=29.0,
                shoulder_width_in=17.1,
                sleeve_length_in=24.7,
                bicep_circumference_in=14.0,
                neck_circumference_in=14.7
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=38.0,
                waist_circumference_in=34.0,
                hip_circumference_in=38.0,
                garment_length_in=29.5,
                shoulder_width_in=17.5,
                sleeve_length_in=25.0,
                bicep_circumference_in=14.5,
                neck_circumference_in=15.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=40.0,
                waist_circumference_in=36.0,
                hip_circumference_in=40.0,
                garment_length_in=30.0,
                shoulder_width_in=17.9,
                sleeve_length_in=25.3,
                bicep_circumference_in=15.0,
                neck_circumference_in=15.3
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=42.0,
                waist_circumference_in=38.0,
                hip_circumference_in=42.0,
                garment_length_in=30.5,
                shoulder_width_in=18.3,
                sleeve_length_in=25.6,
                bicep_circumference_in=15.5,
                neck_circumference_in=15.6
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=44.0,
                waist_circumference_in=40.0,
                hip_circumference_in=44.0,
                garment_length_in=31.0,
                shoulder_width_in=18.7,
                sleeve_length_in=25.9,
                bicep_circumference_in=16.0,
                neck_circumference_in=15.9
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=46.0,
                waist_circumference_in=42.0,
                hip_circumference_in=46.0,
                garment_length_in=31.5,
                shoulder_width_in=19.1,
                sleeve_length_in=26.2,
                bicep_circumference_in=16.5,
                neck_circumference_in=16.2
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=48.0,
                waist_circumference_in=44.0,
                hip_circumference_in=48.0,
                garment_length_in=32.0,
                shoulder_width_in=19.5,
                sleeve_length_in=26.5,
                bicep_circumference_in=17.0,
                neck_circumference_in=16.5
            ),
        }
    ),
    "M_SHIRT_OVERSIZED": SilhouetteGradingChart(
        silhouette_code="M_SHIRT_OVERSIZED",
        silhouette_name="Men's Oversized Drop-Shoulder Shirt",
        gender="MEN",
        category="TOPS",
        fit_type="OVERSIZED",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=40.0,
                waist_circumference_in=38.0,
                hip_circumference_in=40.0,
                garment_length_in=30.0,
                shoulder_width_in=19.7,
                sleeve_length_in=23.4,
                bicep_circumference_in=15.5,
                neck_circumference_in=15.4
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=42.0,
                waist_circumference_in=40.0,
                hip_circumference_in=42.0,
                garment_length_in=30.5,
                shoulder_width_in=20.1,
                sleeve_length_in=23.7,
                bicep_circumference_in=16.0,
                neck_circumference_in=15.7
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=44.0,
                waist_circumference_in=42.0,
                hip_circumference_in=44.0,
                garment_length_in=31.0,
                shoulder_width_in=20.5,
                sleeve_length_in=24.0,
                bicep_circumference_in=16.5,
                neck_circumference_in=16.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=46.0,
                waist_circumference_in=44.0,
                hip_circumference_in=46.0,
                garment_length_in=31.5,
                shoulder_width_in=20.9,
                sleeve_length_in=24.3,
                bicep_circumference_in=17.0,
                neck_circumference_in=16.3
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=48.0,
                waist_circumference_in=46.0,
                hip_circumference_in=48.0,
                garment_length_in=32.0,
                shoulder_width_in=21.3,
                sleeve_length_in=24.6,
                bicep_circumference_in=17.5,
                neck_circumference_in=16.6
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=50.0,
                waist_circumference_in=48.0,
                hip_circumference_in=50.0,
                garment_length_in=32.5,
                shoulder_width_in=21.7,
                sleeve_length_in=24.9,
                bicep_circumference_in=18.0,
                neck_circumference_in=16.9
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=52.0,
                waist_circumference_in=50.0,
                hip_circumference_in=52.0,
                garment_length_in=33.0,
                shoulder_width_in=22.1,
                sleeve_length_in=25.2,
                bicep_circumference_in=18.5,
                neck_circumference_in=17.2
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=54.0,
                waist_circumference_in=52.0,
                hip_circumference_in=54.0,
                garment_length_in=33.5,
                shoulder_width_in=22.5,
                sleeve_length_in=25.5,
                bicep_circumference_in=19.0,
                neck_circumference_in=17.5
            ),
        }
    ),
    "M_TEE_SLIM": SilhouetteGradingChart(
        silhouette_code="M_TEE_SLIM",
        silhouette_name="Men's Tailored Crewneck T-Shirt",
        gender="MEN",
        category="TOPS",
        fit_type="SLIM",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=33.0,
                waist_circumference_in=28.0,
                hip_circumference_in=33.0,
                garment_length_in=26.0,
                shoulder_width_in=15.2,
                sleeve_length_in=7.4,
                bicep_circumference_in=12.0,
                neck_circumference_in=13.9
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=35.0,
                waist_circumference_in=30.0,
                hip_circumference_in=35.0,
                garment_length_in=26.5,
                shoulder_width_in=15.6,
                sleeve_length_in=7.7,
                bicep_circumference_in=12.5,
                neck_circumference_in=14.2
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=37.0,
                waist_circumference_in=32.0,
                hip_circumference_in=37.0,
                garment_length_in=27.0,
                shoulder_width_in=16.0,
                sleeve_length_in=8.0,
                bicep_circumference_in=13.0,
                neck_circumference_in=14.5
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=39.0,
                waist_circumference_in=34.0,
                hip_circumference_in=39.0,
                garment_length_in=27.5,
                shoulder_width_in=16.4,
                sleeve_length_in=8.3,
                bicep_circumference_in=13.5,
                neck_circumference_in=14.8
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=41.0,
                waist_circumference_in=36.0,
                hip_circumference_in=41.0,
                garment_length_in=28.0,
                shoulder_width_in=16.8,
                sleeve_length_in=8.6,
                bicep_circumference_in=14.0,
                neck_circumference_in=15.1
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=43.0,
                waist_circumference_in=38.0,
                hip_circumference_in=43.0,
                garment_length_in=28.5,
                shoulder_width_in=17.2,
                sleeve_length_in=8.9,
                bicep_circumference_in=14.5,
                neck_circumference_in=15.4
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=45.0,
                waist_circumference_in=40.0,
                hip_circumference_in=45.0,
                garment_length_in=29.0,
                shoulder_width_in=17.6,
                sleeve_length_in=9.2,
                bicep_circumference_in=15.0,
                neck_circumference_in=15.7
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=47.0,
                waist_circumference_in=42.0,
                hip_circumference_in=47.0,
                garment_length_in=29.5,
                shoulder_width_in=18.0,
                sleeve_length_in=9.5,
                bicep_circumference_in=15.5,
                neck_circumference_in=16.0
            ),
        }
    ),
    "M_TEE_OVERSIZED": SilhouetteGradingChart(
        silhouette_code="M_TEE_OVERSIZED",
        silhouette_name="Men's Heavyweight Streetwear Boxy Tee",
        gender="MEN",
        category="TOPS",
        fit_type="OVERSIZED",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=42.0,
                waist_circumference_in=41.0,
                hip_circumference_in=42.0,
                garment_length_in=29.0,
                shoulder_width_in=20.2,
                sleeve_length_in=8.9,
                bicep_circumference_in=16.0,
                neck_circumference_in=15.9
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=44.0,
                waist_circumference_in=43.0,
                hip_circumference_in=44.0,
                garment_length_in=29.5,
                shoulder_width_in=20.6,
                sleeve_length_in=9.2,
                bicep_circumference_in=16.5,
                neck_circumference_in=16.2
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=46.0,
                waist_circumference_in=45.0,
                hip_circumference_in=46.0,
                garment_length_in=30.0,
                shoulder_width_in=21.0,
                sleeve_length_in=9.5,
                bicep_circumference_in=17.0,
                neck_circumference_in=16.5
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=48.0,
                waist_circumference_in=47.0,
                hip_circumference_in=48.0,
                garment_length_in=30.5,
                shoulder_width_in=21.4,
                sleeve_length_in=9.8,
                bicep_circumference_in=17.5,
                neck_circumference_in=16.8
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=50.0,
                waist_circumference_in=49.0,
                hip_circumference_in=50.0,
                garment_length_in=31.0,
                shoulder_width_in=21.8,
                sleeve_length_in=10.1,
                bicep_circumference_in=18.0,
                neck_circumference_in=17.1
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=52.0,
                waist_circumference_in=51.0,
                hip_circumference_in=52.0,
                garment_length_in=31.5,
                shoulder_width_in=22.2,
                sleeve_length_in=10.4,
                bicep_circumference_in=18.5,
                neck_circumference_in=17.4
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=54.0,
                waist_circumference_in=53.0,
                hip_circumference_in=54.0,
                garment_length_in=32.0,
                shoulder_width_in=22.6,
                sleeve_length_in=10.7,
                bicep_circumference_in=19.0,
                neck_circumference_in=17.7
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=56.0,
                waist_circumference_in=55.0,
                hip_circumference_in=56.0,
                garment_length_in=32.5,
                shoulder_width_in=23.0,
                sleeve_length_in=11.0,
                bicep_circumference_in=19.5,
                neck_circumference_in=18.0
            ),
        }
    ),
    "M_HOODIE_BOXY": SilhouetteGradingChart(
        silhouette_code="M_HOODIE_BOXY",
        silhouette_name="Men's Boxy Drop-Shoulder Fleece Hoodie",
        gender="MEN",
        category="OUTERWEAR",
        fit_type="OVERSIZED",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=44.0,
                waist_circumference_in=42.0,
                hip_circumference_in=44.0,
                garment_length_in=27.5,
                shoulder_width_in=21.2,
                sleeve_length_in=24.4,
                bicep_circumference_in=17.0,
                neck_circumference_in=17.4
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=46.0,
                waist_circumference_in=44.0,
                hip_circumference_in=46.0,
                garment_length_in=28.0,
                shoulder_width_in=21.6,
                sleeve_length_in=24.7,
                bicep_circumference_in=17.5,
                neck_circumference_in=17.7
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=48.0,
                waist_circumference_in=46.0,
                hip_circumference_in=48.0,
                garment_length_in=28.5,
                shoulder_width_in=22.0,
                sleeve_length_in=25.0,
                bicep_circumference_in=18.0,
                neck_circumference_in=18.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=50.0,
                waist_circumference_in=48.0,
                hip_circumference_in=50.0,
                garment_length_in=29.0,
                shoulder_width_in=22.4,
                sleeve_length_in=25.3,
                bicep_circumference_in=18.5,
                neck_circumference_in=18.3
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=52.0,
                waist_circumference_in=50.0,
                hip_circumference_in=52.0,
                garment_length_in=29.5,
                shoulder_width_in=22.8,
                sleeve_length_in=25.6,
                bicep_circumference_in=19.0,
                neck_circumference_in=18.6
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=54.0,
                waist_circumference_in=52.0,
                hip_circumference_in=54.0,
                garment_length_in=30.0,
                shoulder_width_in=23.2,
                sleeve_length_in=25.9,
                bicep_circumference_in=19.5,
                neck_circumference_in=18.9
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=56.0,
                waist_circumference_in=54.0,
                hip_circumference_in=56.0,
                garment_length_in=30.5,
                shoulder_width_in=23.6,
                sleeve_length_in=26.2,
                bicep_circumference_in=20.0,
                neck_circumference_in=19.2
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=58.0,
                waist_circumference_in=56.0,
                hip_circumference_in=58.0,
                garment_length_in=31.0,
                shoulder_width_in=24.0,
                sleeve_length_in=26.5,
                bicep_circumference_in=20.5,
                neck_circumference_in=19.5
            ),
        }
    ),
    "M_CHINO_SLIM": SilhouetteGradingChart(
        silhouette_code="M_CHINO_SLIM",
        silhouette_name="Men's Slim Tailored Chino Trousers",
        gender="MEN",
        category="BOTTOMS",
        fit_type="SLIM",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=0.0,
                waist_circumference_in=26.0,
                hip_circumference_in=34.0,
                garment_length_in=39.0,
                shoulder_width_in=0.0,
                sleeve_length_in=31.4,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=0.0,
                waist_circumference_in=28.0,
                hip_circumference_in=36.0,
                garment_length_in=39.5,
                shoulder_width_in=0.0,
                sleeve_length_in=31.7,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=0.0,
                waist_circumference_in=30.0,
                hip_circumference_in=38.0,
                garment_length_in=40.0,
                shoulder_width_in=0.0,
                sleeve_length_in=32.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=0.0,
                waist_circumference_in=32.0,
                hip_circumference_in=40.0,
                garment_length_in=40.5,
                shoulder_width_in=0.0,
                sleeve_length_in=32.3,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=0.0,
                waist_circumference_in=34.0,
                hip_circumference_in=42.0,
                garment_length_in=41.0,
                shoulder_width_in=0.0,
                sleeve_length_in=32.6,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=0.0,
                waist_circumference_in=36.0,
                hip_circumference_in=44.0,
                garment_length_in=41.5,
                shoulder_width_in=0.0,
                sleeve_length_in=32.9,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=0.0,
                waist_circumference_in=38.0,
                hip_circumference_in=46.0,
                garment_length_in=42.0,
                shoulder_width_in=0.0,
                sleeve_length_in=33.2,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=0.0,
                waist_circumference_in=40.0,
                hip_circumference_in=48.0,
                garment_length_in=42.5,
                shoulder_width_in=0.0,
                sleeve_length_in=33.5,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
        }
    ),
    "M_CHINO_RELAXED": SilhouetteGradingChart(
        silhouette_code="M_CHINO_RELAXED",
        silhouette_name="Men's Pleated Wide-Leg Trousers",
        gender="MEN",
        category="BOTTOMS",
        fit_type="RELAXED",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=0.0,
                waist_circumference_in=28.0,
                hip_circumference_in=38.0,
                garment_length_in=41.0,
                shoulder_width_in=0.0,
                sleeve_length_in=30.4,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=0.0,
                waist_circumference_in=30.0,
                hip_circumference_in=40.0,
                garment_length_in=41.5,
                shoulder_width_in=0.0,
                sleeve_length_in=30.7,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=0.0,
                waist_circumference_in=32.0,
                hip_circumference_in=42.0,
                garment_length_in=42.0,
                shoulder_width_in=0.0,
                sleeve_length_in=31.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=0.0,
                waist_circumference_in=34.0,
                hip_circumference_in=44.0,
                garment_length_in=42.5,
                shoulder_width_in=0.0,
                sleeve_length_in=31.3,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=0.0,
                waist_circumference_in=36.0,
                hip_circumference_in=46.0,
                garment_length_in=43.0,
                shoulder_width_in=0.0,
                sleeve_length_in=31.6,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=0.0,
                waist_circumference_in=38.0,
                hip_circumference_in=48.0,
                garment_length_in=43.5,
                shoulder_width_in=0.0,
                sleeve_length_in=31.9,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=0.0,
                waist_circumference_in=40.0,
                hip_circumference_in=50.0,
                garment_length_in=44.0,
                shoulder_width_in=0.0,
                sleeve_length_in=32.2,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=0.0,
                waist_circumference_in=42.0,
                hip_circumference_in=52.0,
                garment_length_in=44.5,
                shoulder_width_in=0.0,
                sleeve_length_in=32.5,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
        }
    ),
    "M_RAW_DENIM_STRAIGHT": SilhouetteGradingChart(
        silhouette_code="M_RAW_DENIM_STRAIGHT",
        silhouette_name="Men's Selvedge Raw Denim Straight Leg",
        gender="MEN",
        category="BOTTOMS",
        fit_type="REGULAR",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=0.0,
                waist_circumference_in=27.0,
                hip_circumference_in=35.5,
                garment_length_in=40.0,
                shoulder_width_in=0.0,
                sleeve_length_in=32.4,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=0.0,
                waist_circumference_in=29.0,
                hip_circumference_in=37.5,
                garment_length_in=40.5,
                shoulder_width_in=0.0,
                sleeve_length_in=32.7,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=0.0,
                waist_circumference_in=31.0,
                hip_circumference_in=39.5,
                garment_length_in=41.0,
                shoulder_width_in=0.0,
                sleeve_length_in=33.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=0.0,
                waist_circumference_in=33.0,
                hip_circumference_in=41.5,
                garment_length_in=41.5,
                shoulder_width_in=0.0,
                sleeve_length_in=33.3,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=0.0,
                waist_circumference_in=35.0,
                hip_circumference_in=43.5,
                garment_length_in=42.0,
                shoulder_width_in=0.0,
                sleeve_length_in=33.6,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=0.0,
                waist_circumference_in=37.0,
                hip_circumference_in=45.5,
                garment_length_in=42.5,
                shoulder_width_in=0.0,
                sleeve_length_in=33.9,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=0.0,
                waist_circumference_in=39.0,
                hip_circumference_in=47.5,
                garment_length_in=43.0,
                shoulder_width_in=0.0,
                sleeve_length_in=34.2,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=0.0,
                waist_circumference_in=41.0,
                hip_circumference_in=49.5,
                garment_length_in=43.5,
                shoulder_width_in=0.0,
                sleeve_length_in=34.5,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
        }
    ),
    "M_BLAZER_SINGLE": SilhouetteGradingChart(
        silhouette_code="M_BLAZER_SINGLE",
        silhouette_name="Men's Single-Breasted Tailored Wool Blazer",
        gender="MEN",
        category="TAILORING",
        fit_type="SLIM",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=35.0,
                waist_circumference_in=30.0,
                hip_circumference_in=35.0,
                garment_length_in=28.5,
                shoulder_width_in=16.7,
                sleeve_length_in=24.9,
                bicep_circumference_in=13.5,
                neck_circumference_in=14.9
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=37.0,
                waist_circumference_in=32.0,
                hip_circumference_in=37.0,
                garment_length_in=29.0,
                shoulder_width_in=17.1,
                sleeve_length_in=25.2,
                bicep_circumference_in=14.0,
                neck_circumference_in=15.2
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=39.0,
                waist_circumference_in=34.0,
                hip_circumference_in=39.0,
                garment_length_in=29.5,
                shoulder_width_in=17.5,
                sleeve_length_in=25.5,
                bicep_circumference_in=14.5,
                neck_circumference_in=15.5
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=41.0,
                waist_circumference_in=36.0,
                hip_circumference_in=41.0,
                garment_length_in=30.0,
                shoulder_width_in=17.9,
                sleeve_length_in=25.8,
                bicep_circumference_in=15.0,
                neck_circumference_in=15.8
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=43.0,
                waist_circumference_in=38.0,
                hip_circumference_in=43.0,
                garment_length_in=30.5,
                shoulder_width_in=18.3,
                sleeve_length_in=26.1,
                bicep_circumference_in=15.5,
                neck_circumference_in=16.1
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=45.0,
                waist_circumference_in=40.0,
                hip_circumference_in=45.0,
                garment_length_in=31.0,
                shoulder_width_in=18.7,
                sleeve_length_in=26.4,
                bicep_circumference_in=16.0,
                neck_circumference_in=16.4
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=47.0,
                waist_circumference_in=42.0,
                hip_circumference_in=47.0,
                garment_length_in=31.5,
                shoulder_width_in=19.1,
                sleeve_length_in=26.7,
                bicep_circumference_in=16.5,
                neck_circumference_in=16.7
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=49.0,
                waist_circumference_in=44.0,
                hip_circumference_in=49.0,
                garment_length_in=32.0,
                shoulder_width_in=19.5,
                sleeve_length_in=27.0,
                bicep_circumference_in=17.0,
                neck_circumference_in=17.0
            ),
        }
    ),
    "M_BLAZER_DOUBLE": SilhouetteGradingChart(
        silhouette_code="M_BLAZER_DOUBLE",
        silhouette_name="Men's Double-Breasted Sartorial Blazer",
        gender="MEN",
        category="TAILORING",
        fit_type="REGULAR",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=37.0,
                waist_circumference_in=32.0,
                hip_circumference_in=37.0,
                garment_length_in=29.0,
                shoulder_width_in=17.2,
                sleeve_length_in=24.9,
                bicep_circumference_in=14.0,
                neck_circumference_in=15.4
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=39.0,
                waist_circumference_in=34.0,
                hip_circumference_in=39.0,
                garment_length_in=29.5,
                shoulder_width_in=17.6,
                sleeve_length_in=25.2,
                bicep_circumference_in=14.5,
                neck_circumference_in=15.7
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=41.0,
                waist_circumference_in=36.0,
                hip_circumference_in=41.0,
                garment_length_in=30.0,
                shoulder_width_in=18.0,
                sleeve_length_in=25.5,
                bicep_circumference_in=15.0,
                neck_circumference_in=16.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=43.0,
                waist_circumference_in=38.0,
                hip_circumference_in=43.0,
                garment_length_in=30.5,
                shoulder_width_in=18.4,
                sleeve_length_in=25.8,
                bicep_circumference_in=15.5,
                neck_circumference_in=16.3
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=45.0,
                waist_circumference_in=40.0,
                hip_circumference_in=45.0,
                garment_length_in=31.0,
                shoulder_width_in=18.8,
                sleeve_length_in=26.1,
                bicep_circumference_in=16.0,
                neck_circumference_in=16.6
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=47.0,
                waist_circumference_in=42.0,
                hip_circumference_in=47.0,
                garment_length_in=31.5,
                shoulder_width_in=19.2,
                sleeve_length_in=26.4,
                bicep_circumference_in=16.5,
                neck_circumference_in=16.9
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=49.0,
                waist_circumference_in=44.0,
                hip_circumference_in=49.0,
                garment_length_in=32.0,
                shoulder_width_in=19.6,
                sleeve_length_in=26.7,
                bicep_circumference_in=17.0,
                neck_circumference_in=17.2
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=51.0,
                waist_circumference_in=46.0,
                hip_circumference_in=51.0,
                garment_length_in=32.5,
                shoulder_width_in=20.0,
                sleeve_length_in=27.0,
                bicep_circumference_in=17.5,
                neck_circumference_in=17.5
            ),
        }
    ),
    "M_KURTA_CLASSIC": SilhouetteGradingChart(
        silhouette_code="M_KURTA_CLASSIC",
        silhouette_name="Men's Handcrafted Raw Silk Kurta",
        gender="MEN",
        category="ETHNIC",
        fit_type="REGULAR",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=36.0,
                waist_circumference_in=34.0,
                hip_circumference_in=38.0,
                garment_length_in=41.0,
                shoulder_width_in=17.2,
                sleeve_length_in=24.4,
                bicep_circumference_in=14.5,
                neck_circumference_in=15.4
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=38.0,
                waist_circumference_in=36.0,
                hip_circumference_in=40.0,
                garment_length_in=41.5,
                shoulder_width_in=17.6,
                sleeve_length_in=24.7,
                bicep_circumference_in=15.0,
                neck_circumference_in=15.7
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=40.0,
                waist_circumference_in=38.0,
                hip_circumference_in=42.0,
                garment_length_in=42.0,
                shoulder_width_in=18.0,
                sleeve_length_in=25.0,
                bicep_circumference_in=15.5,
                neck_circumference_in=16.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=42.0,
                waist_circumference_in=40.0,
                hip_circumference_in=44.0,
                garment_length_in=42.5,
                shoulder_width_in=18.4,
                sleeve_length_in=25.3,
                bicep_circumference_in=16.0,
                neck_circumference_in=16.3
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=44.0,
                waist_circumference_in=42.0,
                hip_circumference_in=46.0,
                garment_length_in=43.0,
                shoulder_width_in=18.8,
                sleeve_length_in=25.6,
                bicep_circumference_in=16.5,
                neck_circumference_in=16.6
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=46.0,
                waist_circumference_in=44.0,
                hip_circumference_in=48.0,
                garment_length_in=43.5,
                shoulder_width_in=19.2,
                sleeve_length_in=25.9,
                bicep_circumference_in=17.0,
                neck_circumference_in=16.9
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=48.0,
                waist_circumference_in=46.0,
                hip_circumference_in=50.0,
                garment_length_in=44.0,
                shoulder_width_in=19.6,
                sleeve_length_in=26.2,
                bicep_circumference_in=17.5,
                neck_circumference_in=17.2
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=50.0,
                waist_circumference_in=48.0,
                hip_circumference_in=52.0,
                garment_length_in=44.5,
                shoulder_width_in=20.0,
                sleeve_length_in=26.5,
                bicep_circumference_in=18.0,
                neck_circumference_in=17.5
            ),
        }
    ),
    "M_BANDHGALA": SilhouetteGradingChart(
        silhouette_code="M_BANDHGALA",
        silhouette_name="Men's Heritage Royal Bandhgala Jacket",
        gender="MEN",
        category="ETHNIC",
        fit_type="SLIM",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=36.0,
                waist_circumference_in=31.0,
                hip_circumference_in=36.0,
                garment_length_in=27.5,
                shoulder_width_in=17.2,
                sleeve_length_in=24.4,
                bicep_circumference_in=14.0,
                neck_circumference_in=15.9
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=38.0,
                waist_circumference_in=33.0,
                hip_circumference_in=38.0,
                garment_length_in=28.0,
                shoulder_width_in=17.6,
                sleeve_length_in=24.7,
                bicep_circumference_in=14.5,
                neck_circumference_in=16.2
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=40.0,
                waist_circumference_in=35.0,
                hip_circumference_in=40.0,
                garment_length_in=28.5,
                shoulder_width_in=18.0,
                sleeve_length_in=25.0,
                bicep_circumference_in=15.0,
                neck_circumference_in=16.5
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=42.0,
                waist_circumference_in=37.0,
                hip_circumference_in=42.0,
                garment_length_in=29.0,
                shoulder_width_in=18.4,
                sleeve_length_in=25.3,
                bicep_circumference_in=15.5,
                neck_circumference_in=16.8
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=44.0,
                waist_circumference_in=39.0,
                hip_circumference_in=44.0,
                garment_length_in=29.5,
                shoulder_width_in=18.8,
                sleeve_length_in=25.6,
                bicep_circumference_in=16.0,
                neck_circumference_in=17.1
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=46.0,
                waist_circumference_in=41.0,
                hip_circumference_in=46.0,
                garment_length_in=30.0,
                shoulder_width_in=19.2,
                sleeve_length_in=25.9,
                bicep_circumference_in=16.5,
                neck_circumference_in=17.4
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=48.0,
                waist_circumference_in=43.0,
                hip_circumference_in=48.0,
                garment_length_in=30.5,
                shoulder_width_in=19.6,
                sleeve_length_in=26.2,
                bicep_circumference_in=17.0,
                neck_circumference_in=17.7
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=50.0,
                waist_circumference_in=45.0,
                hip_circumference_in=50.0,
                garment_length_in=31.0,
                shoulder_width_in=20.0,
                sleeve_length_in=26.5,
                bicep_circumference_in=17.5,
                neck_circumference_in=18.0
            ),
        }
    ),
    "M_SHERWANI_CEREMONIAL": SilhouetteGradingChart(
        silhouette_code="M_SHERWANI_CEREMONIAL",
        silhouette_name="Men's Ceremonial Zari Brocade Sherwani",
        gender="MEN",
        category="ETHNIC",
        fit_type="TAILORED",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=37.0,
                waist_circumference_in=32.0,
                hip_circumference_in=39.0,
                garment_length_in=45.0,
                shoulder_width_in=17.7,
                sleeve_length_in=25.4,
                bicep_circumference_in=14.5,
                neck_circumference_in=15.9
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=39.0,
                waist_circumference_in=34.0,
                hip_circumference_in=41.0,
                garment_length_in=45.5,
                shoulder_width_in=18.1,
                sleeve_length_in=25.7,
                bicep_circumference_in=15.0,
                neck_circumference_in=16.2
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=41.0,
                waist_circumference_in=36.0,
                hip_circumference_in=43.0,
                garment_length_in=46.0,
                shoulder_width_in=18.5,
                sleeve_length_in=26.0,
                bicep_circumference_in=15.5,
                neck_circumference_in=16.5
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=43.0,
                waist_circumference_in=38.0,
                hip_circumference_in=45.0,
                garment_length_in=46.5,
                shoulder_width_in=18.9,
                sleeve_length_in=26.3,
                bicep_circumference_in=16.0,
                neck_circumference_in=16.8
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=45.0,
                waist_circumference_in=40.0,
                hip_circumference_in=47.0,
                garment_length_in=47.0,
                shoulder_width_in=19.3,
                sleeve_length_in=26.6,
                bicep_circumference_in=16.5,
                neck_circumference_in=17.1
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=47.0,
                waist_circumference_in=42.0,
                hip_circumference_in=49.0,
                garment_length_in=47.5,
                shoulder_width_in=19.7,
                sleeve_length_in=26.9,
                bicep_circumference_in=17.0,
                neck_circumference_in=17.4
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=49.0,
                waist_circumference_in=44.0,
                hip_circumference_in=51.0,
                garment_length_in=48.0,
                shoulder_width_in=20.1,
                sleeve_length_in=27.2,
                bicep_circumference_in=17.5,
                neck_circumference_in=17.7
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=51.0,
                waist_circumference_in=46.0,
                hip_circumference_in=53.0,
                garment_length_in=48.5,
                shoulder_width_in=20.5,
                sleeve_length_in=27.5,
                bicep_circumference_in=18.0,
                neck_circumference_in=18.0
            ),
        }
    ),
    "W_DRESS_BODYCON": SilhouetteGradingChart(
        silhouette_code="W_DRESS_BODYCON",
        silhouette_name="Women's Asymmetrical Velvet Bodycon Dress",
        gender="WOMEN",
        category="DRESSES",
        fit_type="SLIM",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=29.0,
                waist_circumference_in=21.0,
                hip_circumference_in=31.0,
                garment_length_in=37.0,
                shoulder_width_in=13.2,
                sleeve_length_in=22.4,
                bicep_circumference_in=9.5,
                neck_circumference_in=12.4
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=31.0,
                waist_circumference_in=23.0,
                hip_circumference_in=33.0,
                garment_length_in=37.5,
                shoulder_width_in=13.6,
                sleeve_length_in=22.7,
                bicep_circumference_in=10.0,
                neck_circumference_in=12.7
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=33.0,
                waist_circumference_in=25.0,
                hip_circumference_in=35.0,
                garment_length_in=38.0,
                shoulder_width_in=14.0,
                sleeve_length_in=23.0,
                bicep_circumference_in=10.5,
                neck_circumference_in=13.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=35.0,
                waist_circumference_in=27.0,
                hip_circumference_in=37.0,
                garment_length_in=38.5,
                shoulder_width_in=14.4,
                sleeve_length_in=23.3,
                bicep_circumference_in=11.0,
                neck_circumference_in=13.3
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=37.0,
                waist_circumference_in=29.0,
                hip_circumference_in=39.0,
                garment_length_in=39.0,
                shoulder_width_in=14.8,
                sleeve_length_in=23.6,
                bicep_circumference_in=11.5,
                neck_circumference_in=13.6
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=39.0,
                waist_circumference_in=31.0,
                hip_circumference_in=41.0,
                garment_length_in=39.5,
                shoulder_width_in=15.2,
                sleeve_length_in=23.9,
                bicep_circumference_in=12.0,
                neck_circumference_in=13.9
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=41.0,
                waist_circumference_in=33.0,
                hip_circumference_in=43.0,
                garment_length_in=40.0,
                shoulder_width_in=15.6,
                sleeve_length_in=24.2,
                bicep_circumference_in=12.5,
                neck_circumference_in=14.2
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=43.0,
                waist_circumference_in=35.0,
                hip_circumference_in=45.0,
                garment_length_in=40.5,
                shoulder_width_in=16.0,
                sleeve_length_in=24.5,
                bicep_circumference_in=13.0,
                neck_circumference_in=14.5
            ),
        }
    ),
    "W_DRESS_SLIP": SilhouetteGradingChart(
        silhouette_code="W_DRESS_SLIP",
        silhouette_name="Women's Bias-Cut Silk Charmeuse Slip Dress",
        gender="WOMEN",
        category="DRESSES",
        fit_type="REGULAR",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=30.0,
                waist_circumference_in=23.0,
                hip_circumference_in=33.0,
                garment_length_in=47.0,
                shoulder_width_in=12.7,
                sleeve_length_in=0.0,
                bicep_circumference_in=10.0,
                neck_circumference_in=12.9
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=32.0,
                waist_circumference_in=25.0,
                hip_circumference_in=35.0,
                garment_length_in=47.5,
                shoulder_width_in=13.1,
                sleeve_length_in=0.0,
                bicep_circumference_in=10.5,
                neck_circumference_in=13.2
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=34.0,
                waist_circumference_in=27.0,
                hip_circumference_in=37.0,
                garment_length_in=48.0,
                shoulder_width_in=13.5,
                sleeve_length_in=0.0,
                bicep_circumference_in=11.0,
                neck_circumference_in=13.5
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=36.0,
                waist_circumference_in=29.0,
                hip_circumference_in=39.0,
                garment_length_in=48.5,
                shoulder_width_in=13.9,
                sleeve_length_in=0.0,
                bicep_circumference_in=11.5,
                neck_circumference_in=13.8
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=38.0,
                waist_circumference_in=31.0,
                hip_circumference_in=41.0,
                garment_length_in=49.0,
                shoulder_width_in=14.3,
                sleeve_length_in=0.0,
                bicep_circumference_in=12.0,
                neck_circumference_in=14.1
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=40.0,
                waist_circumference_in=33.0,
                hip_circumference_in=43.0,
                garment_length_in=49.5,
                shoulder_width_in=14.7,
                sleeve_length_in=0.0,
                bicep_circumference_in=12.5,
                neck_circumference_in=14.4
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=42.0,
                waist_circumference_in=35.0,
                hip_circumference_in=45.0,
                garment_length_in=50.0,
                shoulder_width_in=15.1,
                sleeve_length_in=0.0,
                bicep_circumference_in=13.0,
                neck_circumference_in=14.7
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=44.0,
                waist_circumference_in=37.0,
                hip_circumference_in=47.0,
                garment_length_in=50.5,
                shoulder_width_in=15.5,
                sleeve_length_in=0.0,
                bicep_circumference_in=13.5,
                neck_circumference_in=15.0
            ),
        }
    ),
    "W_DRESS_A_LINE": SilhouetteGradingChart(
        silhouette_code="W_DRESS_A_LINE",
        silhouette_name="Women's Pleated Cotton Poplin A-Line Shirt Dress",
        gender="WOMEN",
        category="DRESSES",
        fit_type="REGULAR",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=31.0,
                waist_circumference_in=24.0,
                hip_circumference_in=38.0,
                garment_length_in=43.0,
                shoulder_width_in=13.7,
                sleeve_length_in=22.9,
                bicep_circumference_in=10.5,
                neck_circumference_in=12.9
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=33.0,
                waist_circumference_in=26.0,
                hip_circumference_in=40.0,
                garment_length_in=43.5,
                shoulder_width_in=14.1,
                sleeve_length_in=23.2,
                bicep_circumference_in=11.0,
                neck_circumference_in=13.2
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=35.0,
                waist_circumference_in=28.0,
                hip_circumference_in=42.0,
                garment_length_in=44.0,
                shoulder_width_in=14.5,
                sleeve_length_in=23.5,
                bicep_circumference_in=11.5,
                neck_circumference_in=13.5
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=37.0,
                waist_circumference_in=30.0,
                hip_circumference_in=44.0,
                garment_length_in=44.5,
                shoulder_width_in=14.9,
                sleeve_length_in=23.8,
                bicep_circumference_in=12.0,
                neck_circumference_in=13.8
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=39.0,
                waist_circumference_in=32.0,
                hip_circumference_in=46.0,
                garment_length_in=45.0,
                shoulder_width_in=15.3,
                sleeve_length_in=24.1,
                bicep_circumference_in=12.5,
                neck_circumference_in=14.1
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=41.0,
                waist_circumference_in=34.0,
                hip_circumference_in=48.0,
                garment_length_in=45.5,
                shoulder_width_in=15.7,
                sleeve_length_in=24.4,
                bicep_circumference_in=13.0,
                neck_circumference_in=14.4
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=43.0,
                waist_circumference_in=36.0,
                hip_circumference_in=50.0,
                garment_length_in=46.0,
                shoulder_width_in=16.1,
                sleeve_length_in=24.7,
                bicep_circumference_in=13.5,
                neck_circumference_in=14.7
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=45.0,
                waist_circumference_in=38.0,
                hip_circumference_in=52.0,
                garment_length_in=46.5,
                shoulder_width_in=16.5,
                sleeve_length_in=25.0,
                bicep_circumference_in=14.0,
                neck_circumference_in=15.0
            ),
        }
    ),
    "W_DRESS_MAXI_BOHO": SilhouetteGradingChart(
        silhouette_code="W_DRESS_MAXI_BOHO",
        silhouette_name="Women's Tiered Linen Bohemian Maxi Dress",
        gender="WOMEN",
        category="DRESSES",
        fit_type="RELAXED",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=32.0,
                waist_circumference_in=26.0,
                hip_circumference_in=42.0,
                garment_length_in=53.0,
                shoulder_width_in=13.7,
                sleeve_length_in=17.4,
                bicep_circumference_in=11.5,
                neck_circumference_in=13.4
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=34.0,
                waist_circumference_in=28.0,
                hip_circumference_in=44.0,
                garment_length_in=53.5,
                shoulder_width_in=14.1,
                sleeve_length_in=17.7,
                bicep_circumference_in=12.0,
                neck_circumference_in=13.7
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=36.0,
                waist_circumference_in=30.0,
                hip_circumference_in=46.0,
                garment_length_in=54.0,
                shoulder_width_in=14.5,
                sleeve_length_in=18.0,
                bicep_circumference_in=12.5,
                neck_circumference_in=14.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=38.0,
                waist_circumference_in=32.0,
                hip_circumference_in=48.0,
                garment_length_in=54.5,
                shoulder_width_in=14.9,
                sleeve_length_in=18.3,
                bicep_circumference_in=13.0,
                neck_circumference_in=14.3
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=40.0,
                waist_circumference_in=34.0,
                hip_circumference_in=50.0,
                garment_length_in=55.0,
                shoulder_width_in=15.3,
                sleeve_length_in=18.6,
                bicep_circumference_in=13.5,
                neck_circumference_in=14.6
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=42.0,
                waist_circumference_in=36.0,
                hip_circumference_in=52.0,
                garment_length_in=55.5,
                shoulder_width_in=15.7,
                sleeve_length_in=18.9,
                bicep_circumference_in=14.0,
                neck_circumference_in=14.9
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=44.0,
                waist_circumference_in=38.0,
                hip_circumference_in=54.0,
                garment_length_in=56.0,
                shoulder_width_in=16.1,
                sleeve_length_in=19.2,
                bicep_circumference_in=14.5,
                neck_circumference_in=15.2
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=46.0,
                waist_circumference_in=40.0,
                hip_circumference_in=56.0,
                garment_length_in=56.5,
                shoulder_width_in=16.5,
                sleeve_length_in=19.5,
                bicep_circumference_in=15.0,
                neck_circumference_in=15.5
            ),
        }
    ),
    "W_BLOUSE_SILK_COWL": SilhouetteGradingChart(
        silhouette_code="W_BLOUSE_SILK_COWL",
        silhouette_name="Women's Draped Silk Cowl Neck Blouse",
        gender="WOMEN",
        category="TOPS",
        fit_type="REGULAR",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=31.0,
                waist_circumference_in=25.0,
                hip_circumference_in=32.0,
                garment_length_in=23.0,
                shoulder_width_in=13.2,
                sleeve_length_in=22.4,
                bicep_circumference_in=10.5,
                neck_circumference_in=12.4
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=33.0,
                waist_circumference_in=27.0,
                hip_circumference_in=34.0,
                garment_length_in=23.5,
                shoulder_width_in=13.6,
                sleeve_length_in=22.7,
                bicep_circumference_in=11.0,
                neck_circumference_in=12.7
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=35.0,
                waist_circumference_in=29.0,
                hip_circumference_in=36.0,
                garment_length_in=24.0,
                shoulder_width_in=14.0,
                sleeve_length_in=23.0,
                bicep_circumference_in=11.5,
                neck_circumference_in=13.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=37.0,
                waist_circumference_in=31.0,
                hip_circumference_in=38.0,
                garment_length_in=24.5,
                shoulder_width_in=14.4,
                sleeve_length_in=23.3,
                bicep_circumference_in=12.0,
                neck_circumference_in=13.3
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=39.0,
                waist_circumference_in=33.0,
                hip_circumference_in=40.0,
                garment_length_in=25.0,
                shoulder_width_in=14.8,
                sleeve_length_in=23.6,
                bicep_circumference_in=12.5,
                neck_circumference_in=13.6
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=41.0,
                waist_circumference_in=35.0,
                hip_circumference_in=42.0,
                garment_length_in=25.5,
                shoulder_width_in=15.2,
                sleeve_length_in=23.9,
                bicep_circumference_in=13.0,
                neck_circumference_in=13.9
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=43.0,
                waist_circumference_in=37.0,
                hip_circumference_in=44.0,
                garment_length_in=26.0,
                shoulder_width_in=15.6,
                sleeve_length_in=24.2,
                bicep_circumference_in=13.5,
                neck_circumference_in=14.2
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=45.0,
                waist_circumference_in=39.0,
                hip_circumference_in=46.0,
                garment_length_in=26.5,
                shoulder_width_in=16.0,
                sleeve_length_in=24.5,
                bicep_circumference_in=14.0,
                neck_circumference_in=14.5
            ),
        }
    ),
    "W_SHIRT_CRISP_ELS": SilhouetteGradingChart(
        silhouette_code="W_SHIRT_CRISP_ELS",
        silhouette_name="Women's Extra-Long Staple Tailored Business Shirt",
        gender="WOMEN",
        category="TOPS",
        fit_type="SLIM",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=30.0,
                waist_circumference_in=23.0,
                hip_circumference_in=32.0,
                garment_length_in=25.0,
                shoulder_width_in=13.7,
                sleeve_length_in=23.4,
                bicep_circumference_in=10.0,
                neck_circumference_in=12.9
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=32.0,
                waist_circumference_in=25.0,
                hip_circumference_in=34.0,
                garment_length_in=25.5,
                shoulder_width_in=14.1,
                sleeve_length_in=23.7,
                bicep_circumference_in=10.5,
                neck_circumference_in=13.2
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=34.0,
                waist_circumference_in=27.0,
                hip_circumference_in=36.0,
                garment_length_in=26.0,
                shoulder_width_in=14.5,
                sleeve_length_in=24.0,
                bicep_circumference_in=11.0,
                neck_circumference_in=13.5
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=36.0,
                waist_circumference_in=29.0,
                hip_circumference_in=38.0,
                garment_length_in=26.5,
                shoulder_width_in=14.9,
                sleeve_length_in=24.3,
                bicep_circumference_in=11.5,
                neck_circumference_in=13.8
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=38.0,
                waist_circumference_in=31.0,
                hip_circumference_in=40.0,
                garment_length_in=27.0,
                shoulder_width_in=15.3,
                sleeve_length_in=24.6,
                bicep_circumference_in=12.0,
                neck_circumference_in=14.1
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=40.0,
                waist_circumference_in=33.0,
                hip_circumference_in=42.0,
                garment_length_in=27.5,
                shoulder_width_in=15.7,
                sleeve_length_in=24.9,
                bicep_circumference_in=12.5,
                neck_circumference_in=14.4
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=42.0,
                waist_circumference_in=35.0,
                hip_circumference_in=44.0,
                garment_length_in=28.0,
                shoulder_width_in=16.1,
                sleeve_length_in=25.2,
                bicep_circumference_in=13.0,
                neck_circumference_in=14.7
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=44.0,
                waist_circumference_in=37.0,
                hip_circumference_in=46.0,
                garment_length_in=28.5,
                shoulder_width_in=16.5,
                sleeve_length_in=25.5,
                bicep_circumference_in=13.5,
                neck_circumference_in=15.0
            ),
        }
    ),
    "W_TROUSER_WIDE_LEG": SilhouetteGradingChart(
        silhouette_code="W_TROUSER_WIDE_LEG",
        silhouette_name="Women's High-Rise Pleated Wide-Leg Trousers",
        gender="WOMEN",
        category="BOTTOMS",
        fit_type="RELAXED",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=0.0,
                waist_circumference_in=22.0,
                hip_circumference_in=33.0,
                garment_length_in=42.0,
                shoulder_width_in=0.0,
                sleeve_length_in=31.4,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=0.0,
                waist_circumference_in=24.0,
                hip_circumference_in=35.0,
                garment_length_in=42.5,
                shoulder_width_in=0.0,
                sleeve_length_in=31.7,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=0.0,
                waist_circumference_in=26.0,
                hip_circumference_in=37.0,
                garment_length_in=43.0,
                shoulder_width_in=0.0,
                sleeve_length_in=32.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=0.0,
                waist_circumference_in=28.0,
                hip_circumference_in=39.0,
                garment_length_in=43.5,
                shoulder_width_in=0.0,
                sleeve_length_in=32.3,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=0.0,
                waist_circumference_in=30.0,
                hip_circumference_in=41.0,
                garment_length_in=44.0,
                shoulder_width_in=0.0,
                sleeve_length_in=32.6,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=0.0,
                waist_circumference_in=32.0,
                hip_circumference_in=43.0,
                garment_length_in=44.5,
                shoulder_width_in=0.0,
                sleeve_length_in=32.9,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=0.0,
                waist_circumference_in=34.0,
                hip_circumference_in=45.0,
                garment_length_in=45.0,
                shoulder_width_in=0.0,
                sleeve_length_in=33.2,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=0.0,
                waist_circumference_in=36.0,
                hip_circumference_in=47.0,
                garment_length_in=45.5,
                shoulder_width_in=0.0,
                sleeve_length_in=33.5,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
        }
    ),
    "W_TROUSER_CIGARETTE": SilhouetteGradingChart(
        silhouette_code="W_TROUSER_CIGARETTE",
        silhouette_name="Women's Cropped Ankle Cigarette Pants",
        gender="WOMEN",
        category="BOTTOMS",
        fit_type="SLIM",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=0.0,
                waist_circumference_in=22.0,
                hip_circumference_in=32.0,
                garment_length_in=36.0,
                shoulder_width_in=0.0,
                sleeve_length_in=27.4,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=0.0,
                waist_circumference_in=24.0,
                hip_circumference_in=34.0,
                garment_length_in=36.5,
                shoulder_width_in=0.0,
                sleeve_length_in=27.7,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=0.0,
                waist_circumference_in=26.0,
                hip_circumference_in=36.0,
                garment_length_in=37.0,
                shoulder_width_in=0.0,
                sleeve_length_in=28.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=0.0,
                waist_circumference_in=28.0,
                hip_circumference_in=38.0,
                garment_length_in=37.5,
                shoulder_width_in=0.0,
                sleeve_length_in=28.3,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=0.0,
                waist_circumference_in=30.0,
                hip_circumference_in=40.0,
                garment_length_in=38.0,
                shoulder_width_in=0.0,
                sleeve_length_in=28.6,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=0.0,
                waist_circumference_in=32.0,
                hip_circumference_in=42.0,
                garment_length_in=38.5,
                shoulder_width_in=0.0,
                sleeve_length_in=28.9,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=0.0,
                waist_circumference_in=34.0,
                hip_circumference_in=44.0,
                garment_length_in=39.0,
                shoulder_width_in=0.0,
                sleeve_length_in=29.2,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=0.0,
                waist_circumference_in=36.0,
                hip_circumference_in=46.0,
                garment_length_in=39.5,
                shoulder_width_in=0.0,
                sleeve_length_in=29.5,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
        }
    ),
    "W_SKIRT_BIAS_MIDI": SilhouetteGradingChart(
        silhouette_code="W_SKIRT_BIAS_MIDI",
        silhouette_name="Women's Heavy Silk Satin Bias-Cut Midi Skirt",
        gender="WOMEN",
        category="BOTTOMS",
        fit_type="REGULAR",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=0.0,
                waist_circumference_in=22.0,
                hip_circumference_in=33.0,
                garment_length_in=32.0,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=0.0,
                waist_circumference_in=24.0,
                hip_circumference_in=35.0,
                garment_length_in=32.5,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=0.0,
                waist_circumference_in=26.0,
                hip_circumference_in=37.0,
                garment_length_in=33.0,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=0.0,
                waist_circumference_in=28.0,
                hip_circumference_in=39.0,
                garment_length_in=33.5,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=0.0,
                waist_circumference_in=30.0,
                hip_circumference_in=41.0,
                garment_length_in=34.0,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=0.0,
                waist_circumference_in=32.0,
                hip_circumference_in=43.0,
                garment_length_in=34.5,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=0.0,
                waist_circumference_in=34.0,
                hip_circumference_in=45.0,
                garment_length_in=35.0,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=0.0,
                waist_circumference_in=36.0,
                hip_circumference_in=47.0,
                garment_length_in=35.5,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
        }
    ),
    "W_SKIRT_PLEATED_TENNIS": SilhouetteGradingChart(
        silhouette_code="W_SKIRT_PLEATED_TENNIS",
        silhouette_name="Women's Structured Pleated Micro-Mini Skirt",
        gender="WOMEN",
        category="BOTTOMS",
        fit_type="SLIM",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=0.0,
                waist_circumference_in=21.5,
                hip_circumference_in=31.0,
                garment_length_in=14.5,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=0.0,
                waist_circumference_in=23.5,
                hip_circumference_in=33.0,
                garment_length_in=15.0,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=0.0,
                waist_circumference_in=25.5,
                hip_circumference_in=35.0,
                garment_length_in=15.5,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=0.0,
                waist_circumference_in=27.5,
                hip_circumference_in=37.0,
                garment_length_in=16.0,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=0.0,
                waist_circumference_in=29.5,
                hip_circumference_in=39.0,
                garment_length_in=16.5,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=0.0,
                waist_circumference_in=31.5,
                hip_circumference_in=41.0,
                garment_length_in=17.0,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=0.0,
                waist_circumference_in=33.5,
                hip_circumference_in=43.0,
                garment_length_in=17.5,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=0.0,
                waist_circumference_in=35.5,
                hip_circumference_in=45.0,
                garment_length_in=18.0,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
        }
    ),
    "W_LEHENGA_ROYAL": SilhouetteGradingChart(
        silhouette_code="W_LEHENGA_ROYAL",
        silhouette_name="Women's 24-Kali Raw Silk Bridal Lehenga",
        gender="WOMEN",
        category="ETHNIC",
        fit_type="VOLUMINOUS",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=0.0,
                waist_circumference_in=24.0,
                hip_circumference_in=44.0,
                garment_length_in=42.5,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=0.0,
                waist_circumference_in=26.0,
                hip_circumference_in=46.0,
                garment_length_in=43.0,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=0.0,
                waist_circumference_in=28.0,
                hip_circumference_in=48.0,
                garment_length_in=43.5,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=0.0,
                waist_circumference_in=30.0,
                hip_circumference_in=50.0,
                garment_length_in=44.0,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=0.0,
                waist_circumference_in=32.0,
                hip_circumference_in=52.0,
                garment_length_in=44.5,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=0.0,
                waist_circumference_in=34.0,
                hip_circumference_in=54.0,
                garment_length_in=45.0,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=0.0,
                waist_circumference_in=36.0,
                hip_circumference_in=56.0,
                garment_length_in=45.5,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=0.0,
                waist_circumference_in=38.0,
                hip_circumference_in=58.0,
                garment_length_in=46.0,
                shoulder_width_in=0.0,
                sleeve_length_in=0.0,
                bicep_circumference_in=0.0,
                neck_circumference_in=0.0
            ),
        }
    ),
    "W_ANARKALI_KALIDAR": SilhouetteGradingChart(
        silhouette_code="W_ANARKALI_KALIDAR",
        silhouette_name="Women's Mulberry Silk 32-Kali Anarkali Suit",
        gender="WOMEN",
        category="ETHNIC",
        fit_type="VOLUMINOUS",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=30.0,
                waist_circumference_in=24.0,
                hip_circumference_in=42.0,
                garment_length_in=51.0,
                shoulder_width_in=13.2,
                sleeve_length_in=21.9,
                bicep_circumference_in=10.5,
                neck_circumference_in=12.9
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=32.0,
                waist_circumference_in=26.0,
                hip_circumference_in=44.0,
                garment_length_in=51.5,
                shoulder_width_in=13.6,
                sleeve_length_in=22.2,
                bicep_circumference_in=11.0,
                neck_circumference_in=13.2
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=34.0,
                waist_circumference_in=28.0,
                hip_circumference_in=46.0,
                garment_length_in=52.0,
                shoulder_width_in=14.0,
                sleeve_length_in=22.5,
                bicep_circumference_in=11.5,
                neck_circumference_in=13.5
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=36.0,
                waist_circumference_in=30.0,
                hip_circumference_in=48.0,
                garment_length_in=52.5,
                shoulder_width_in=14.4,
                sleeve_length_in=22.8,
                bicep_circumference_in=12.0,
                neck_circumference_in=13.8
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=38.0,
                waist_circumference_in=32.0,
                hip_circumference_in=50.0,
                garment_length_in=53.0,
                shoulder_width_in=14.8,
                sleeve_length_in=23.1,
                bicep_circumference_in=12.5,
                neck_circumference_in=14.1
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=40.0,
                waist_circumference_in=34.0,
                hip_circumference_in=52.0,
                garment_length_in=53.5,
                shoulder_width_in=15.2,
                sleeve_length_in=23.4,
                bicep_circumference_in=13.0,
                neck_circumference_in=14.4
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=42.0,
                waist_circumference_in=36.0,
                hip_circumference_in=54.0,
                garment_length_in=54.0,
                shoulder_width_in=15.6,
                sleeve_length_in=23.7,
                bicep_circumference_in=13.5,
                neck_circumference_in=14.7
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=44.0,
                waist_circumference_in=38.0,
                hip_circumference_in=56.0,
                garment_length_in=54.5,
                shoulder_width_in=16.0,
                sleeve_length_in=24.0,
                bicep_circumference_in=14.0,
                neck_circumference_in=15.0
            ),
        }
    ),
    "W_KURTA_CHIKANKARI": SilhouetteGradingChart(
        silhouette_code="W_KURTA_CHIKANKARI",
        silhouette_name="Women's Lucknowi Hand-Embroidered Chanderi Kurta",
        gender="WOMEN",
        category="ETHNIC",
        fit_type="REGULAR",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=32.0,
                waist_circumference_in=28.0,
                hip_circumference_in=36.0,
                garment_length_in=43.0,
                shoulder_width_in=13.7,
                sleeve_length_in=18.9,
                bicep_circumference_in=11.0,
                neck_circumference_in=13.4
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=34.0,
                waist_circumference_in=30.0,
                hip_circumference_in=38.0,
                garment_length_in=43.5,
                shoulder_width_in=14.1,
                sleeve_length_in=19.2,
                bicep_circumference_in=11.5,
                neck_circumference_in=13.7
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=36.0,
                waist_circumference_in=32.0,
                hip_circumference_in=40.0,
                garment_length_in=44.0,
                shoulder_width_in=14.5,
                sleeve_length_in=19.5,
                bicep_circumference_in=12.0,
                neck_circumference_in=14.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=38.0,
                waist_circumference_in=34.0,
                hip_circumference_in=42.0,
                garment_length_in=44.5,
                shoulder_width_in=14.9,
                sleeve_length_in=19.8,
                bicep_circumference_in=12.5,
                neck_circumference_in=14.3
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=40.0,
                waist_circumference_in=36.0,
                hip_circumference_in=44.0,
                garment_length_in=45.0,
                shoulder_width_in=15.3,
                sleeve_length_in=20.1,
                bicep_circumference_in=13.0,
                neck_circumference_in=14.6
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=42.0,
                waist_circumference_in=38.0,
                hip_circumference_in=46.0,
                garment_length_in=45.5,
                shoulder_width_in=15.7,
                sleeve_length_in=20.4,
                bicep_circumference_in=13.5,
                neck_circumference_in=14.9
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=44.0,
                waist_circumference_in=40.0,
                hip_circumference_in=48.0,
                garment_length_in=46.0,
                shoulder_width_in=16.1,
                sleeve_length_in=20.7,
                bicep_circumference_in=14.0,
                neck_circumference_in=15.2
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=46.0,
                waist_circumference_in=42.0,
                hip_circumference_in=50.0,
                garment_length_in=46.5,
                shoulder_width_in=16.5,
                sleeve_length_in=21.0,
                bicep_circumference_in=14.5,
                neck_circumference_in=15.5
            ),
        }
    ),
    "W_SAREE_BLOUSE_PADDED": SilhouetteGradingChart(
        silhouette_code="W_SAREE_BLOUSE_PADDED",
        silhouette_name="Women's Sweetheart Padded Zardozi Saree Blouse",
        gender="WOMEN",
        category="ETHNIC",
        fit_type="SLIM",
        sizes={
            "XXS": GarmentSizeSpec(
                size_label="XXS",
                chest_circumference_in=30.0,
                waist_circumference_in=24.0,
                hip_circumference_in=0.0,
                garment_length_in=13.5,
                shoulder_width_in=12.7,
                sleeve_length_in=9.9,
                bicep_circumference_in=10.0,
                neck_circumference_in=12.4
            ),
            "XS": GarmentSizeSpec(
                size_label="XS",
                chest_circumference_in=32.0,
                waist_circumference_in=26.0,
                hip_circumference_in=0.0,
                garment_length_in=14.0,
                shoulder_width_in=13.1,
                sleeve_length_in=10.2,
                bicep_circumference_in=10.5,
                neck_circumference_in=12.7
            ),
            "S": GarmentSizeSpec(
                size_label="S",
                chest_circumference_in=34.0,
                waist_circumference_in=28.0,
                hip_circumference_in=0.0,
                garment_length_in=14.5,
                shoulder_width_in=13.5,
                sleeve_length_in=10.5,
                bicep_circumference_in=11.0,
                neck_circumference_in=13.0
            ),
            "M": GarmentSizeSpec(
                size_label="M",
                chest_circumference_in=36.0,
                waist_circumference_in=30.0,
                hip_circumference_in=0.0,
                garment_length_in=15.0,
                shoulder_width_in=13.9,
                sleeve_length_in=10.8,
                bicep_circumference_in=11.5,
                neck_circumference_in=13.3
            ),
            "L": GarmentSizeSpec(
                size_label="L",
                chest_circumference_in=38.0,
                waist_circumference_in=32.0,
                hip_circumference_in=0.0,
                garment_length_in=15.5,
                shoulder_width_in=14.3,
                sleeve_length_in=11.1,
                bicep_circumference_in=12.0,
                neck_circumference_in=13.6
            ),
            "XL": GarmentSizeSpec(
                size_label="XL",
                chest_circumference_in=40.0,
                waist_circumference_in=34.0,
                hip_circumference_in=0.0,
                garment_length_in=16.0,
                shoulder_width_in=14.7,
                sleeve_length_in=11.4,
                bicep_circumference_in=12.5,
                neck_circumference_in=13.9
            ),
            "XXL": GarmentSizeSpec(
                size_label="XXL",
                chest_circumference_in=42.0,
                waist_circumference_in=36.0,
                hip_circumference_in=0.0,
                garment_length_in=16.5,
                shoulder_width_in=15.1,
                sleeve_length_in=11.7,
                bicep_circumference_in=13.0,
                neck_circumference_in=14.2
            ),
            "3XL": GarmentSizeSpec(
                size_label="3XL",
                chest_circumference_in=44.0,
                waist_circumference_in=38.0,
                hip_circumference_in=0.0,
                garment_length_in=17.0,
                shoulder_width_in=15.5,
                sleeve_length_in=12.0,
                bicep_circumference_in=13.5,
                neck_circumference_in=14.5
            ),
        }
    ),
}
