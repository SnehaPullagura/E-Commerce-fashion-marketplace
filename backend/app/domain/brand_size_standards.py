"""
Designer Brand Sizing Standards & Anthropometric Deviation Registry.
Maintains official brand size charts, vanity sizing compensation factors,
and cut archetypes across 100 international luxury & designer brands.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel

class BrandSizeMeasurement(BaseModel):
    size_label: str
    chest_in: float
    waist_in: float
    hips_in: float
    inseam_in: float = 32.0
    shoulder_in: float = 17.5
    length_in: float = 29.0
    vanity_sizing_offset_in: float = 0.0

class BrandProfileSizing(BaseModel):
    brand_id: str
    brand_name: str
    origin_country: str
    cut_archetype: str  # "EUROPEAN_SLIM", "AMERICAN_RELAXED", "ASIAN_COMPACT", "INDIAN_CONTEMPORARY"
    tops_size_chart: Dict[str, BrandSizeMeasurement]
    bottoms_size_chart: Dict[str, BrandSizeMeasurement]

BRAND_SIZING_REGISTRY: Dict[str, BrandProfileSizing] = {
    "NOIR_COUTURE": BrandProfileSizing(
        brand_id="NOIR_COUTURE",
        brand_name="Noir Couture Atelier",
        origin_country="India",
        cut_archetype="INDIAN_CONTEMPORARY",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "ANITA_DONGRE": BrandProfileSizing(
        brand_id="ANITA_DONGRE",
        brand_name="Anita Dongre Haute Couture",
        origin_country="India",
        cut_archetype="INDIAN_CONTEMPORARY",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.5,
                waist_in=28.5,
                hips_in=35.5,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.5,
                waist_in=30.5,
                hips_in=37.5,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.5,
                waist_in=32.5,
                hips_in=39.5,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.5,
                waist_in=34.5,
                hips_in=41.5,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.5,
                waist_in=36.5,
                hips_in=43.5,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.5,
                waist_in=38.5,
                hips_in=45.5,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.5,
                waist_in=40.5,
                hips_in=47.5,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.5,
                waist_in=42.5,
                hips_in=49.5,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.5
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.5,
                hips_in=34.5,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.5,
                hips_in=36.5,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.5,
                hips_in=38.5,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.5,
                hips_in=40.5,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.5,
                hips_in=42.5,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.5,
                hips_in=44.5,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.5,
                hips_in=46.5,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.5,
                hips_in=48.5,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
        }
    ),
    "TOKYO_RAW": BrandProfileSizing(
        brand_id="TOKYO_RAW",
        brand_name="Tokyo Raw Denim & Streetwear",
        origin_country="Japan",
        cut_archetype="ASIAN_COMPACT",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=33.0,
                waist_in=27.0,
                hips_in=34.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=35.0,
                waist_in=29.0,
                hips_in=36.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=-1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=37.0,
                waist_in=31.0,
                hips_in=38.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=-1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=39.0,
                waist_in=33.0,
                hips_in=40.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=-1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=41.0,
                waist_in=35.0,
                hips_in=42.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=43.0,
                waist_in=37.0,
                hips_in=44.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=-1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=45.0,
                waist_in=39.0,
                hips_in=46.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=-1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=47.0,
                waist_in=41.0,
                hips_in=48.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=-1.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=25.0,
                hips_in=33.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=27.0,
                hips_in=35.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=29.0,
                hips_in=37.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=31.0,
                hips_in=39.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=33.0,
                hips_in=41.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=35.0,
                hips_in=43.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=37.0,
                hips_in=45.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=39.0,
                hips_in=47.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
        }
    ),
    "MILANO_SARTORIAL": BrandProfileSizing(
        brand_id="MILANO_SARTORIAL",
        brand_name="Milano Sartorial Goods",
        origin_country="Italy",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=33.5,
                waist_in=27.5,
                hips_in=34.5,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=35.5,
                waist_in=29.5,
                hips_in=36.5,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=-0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=37.5,
                waist_in=31.5,
                hips_in=38.5,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=-0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=39.5,
                waist_in=33.5,
                hips_in=40.5,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=-0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=41.5,
                waist_in=35.5,
                hips_in=42.5,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=43.5,
                waist_in=37.5,
                hips_in=44.5,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=-0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=45.5,
                waist_in=39.5,
                hips_in=46.5,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=-0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=47.5,
                waist_in=41.5,
                hips_in=48.5,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=-0.5
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=25.5,
                hips_in=33.5,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=27.5,
                hips_in=35.5,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=29.5,
                hips_in=37.5,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=31.5,
                hips_in=39.5,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=33.5,
                hips_in=41.5,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=35.5,
                hips_in=43.5,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=37.5,
                hips_in=45.5,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=39.5,
                hips_in=47.5,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
        }
    ),
    "SABYASACHI_HERITAGE": BrandProfileSizing(
        brand_id="SABYASACHI_HERITAGE",
        brand_name="Sabyasachi Heritage",
        origin_country="India",
        cut_archetype="INDIAN_CONTEMPORARY",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "RAW_MANGO": BrandProfileSizing(
        brand_id="RAW_MANGO",
        brand_name="Raw Mango Handwoven",
        origin_country="India",
        cut_archetype="INDIAN_CONTEMPORARY",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.5,
                waist_in=28.5,
                hips_in=35.5,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.5,
                waist_in=30.5,
                hips_in=37.5,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.5,
                waist_in=32.5,
                hips_in=39.5,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.5,
                waist_in=34.5,
                hips_in=41.5,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.5,
                waist_in=36.5,
                hips_in=43.5,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.5,
                waist_in=38.5,
                hips_in=45.5,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.5,
                waist_in=40.5,
                hips_in=47.5,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.5,
                waist_in=42.5,
                hips_in=49.5,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.5
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.5,
                hips_in=34.5,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.5,
                hips_in=36.5,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.5,
                hips_in=38.5,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.5,
                hips_in=40.5,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.5,
                hips_in=42.5,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.5,
                hips_in=44.5,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.5,
                hips_in=46.5,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.5,
                hips_in=48.5,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
        }
    ),
    "TARUN_TAHILIANI": BrandProfileSizing(
        brand_id="TARUN_TAHILIANI",
        brand_name="Tarun Tahiliani Drapes",
        origin_country="India",
        cut_archetype="INDIAN_CONTEMPORARY",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "ROHIT_BAL": BrandProfileSizing(
        brand_id="ROHIT_BAL",
        brand_name="Rohit Bal Couture",
        origin_country="India",
        cut_archetype="INDIAN_CONTEMPORARY",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "MANISH_MALHOTRA": BrandProfileSizing(
        brand_id="MANISH_MALHOTRA",
        brand_name="Manish Malhotra Glamour",
        origin_country="India",
        cut_archetype="INDIAN_CONTEMPORARY",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "RITU_KUMAR": BrandProfileSizing(
        brand_id="RITU_KUMAR",
        brand_name="House of Ritu Kumar",
        origin_country="India",
        cut_archetype="INDIAN_CONTEMPORARY",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.5,
                waist_in=28.5,
                hips_in=35.5,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.5,
                waist_in=30.5,
                hips_in=37.5,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.5,
                waist_in=32.5,
                hips_in=39.5,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.5,
                waist_in=34.5,
                hips_in=41.5,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.5,
                waist_in=36.5,
                hips_in=43.5,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.5,
                waist_in=38.5,
                hips_in=45.5,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.5,
                waist_in=40.5,
                hips_in=47.5,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.5,
                waist_in=42.5,
                hips_in=49.5,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.5
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.5,
                hips_in=34.5,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.5,
                hips_in=36.5,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.5,
                hips_in=38.5,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.5,
                hips_in=40.5,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.5,
                hips_in=42.5,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.5,
                hips_in=44.5,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.5,
                hips_in=46.5,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.5,
                hips_in=48.5,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
        }
    ),
    "ABU_JANI_SANDEEP_KHOSLA": BrandProfileSizing(
        brand_id="ABU_JANI_SANDEEP_KHOSLA",
        brand_name="Abu Jani Sandeep Khosla",
        origin_country="India",
        cut_archetype="INDIAN_CONTEMPORARY",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "GAURAV_GUPTA": BrandProfileSizing(
        brand_id="GAURAV_GUPTA",
        brand_name="Gaurav Gupta Sculptural",
        origin_country="India",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=33.5,
                waist_in=27.5,
                hips_in=34.5,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=35.5,
                waist_in=29.5,
                hips_in=36.5,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=-0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=37.5,
                waist_in=31.5,
                hips_in=38.5,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=-0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=39.5,
                waist_in=33.5,
                hips_in=40.5,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=-0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=41.5,
                waist_in=35.5,
                hips_in=42.5,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=43.5,
                waist_in=37.5,
                hips_in=44.5,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=-0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=45.5,
                waist_in=39.5,
                hips_in=46.5,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=-0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=47.5,
                waist_in=41.5,
                hips_in=48.5,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=-0.5
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=25.5,
                hips_in=33.5,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=27.5,
                hips_in=35.5,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=29.5,
                hips_in=37.5,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=31.5,
                hips_in=39.5,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=33.5,
                hips_in=41.5,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=35.5,
                hips_in=43.5,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=37.5,
                hips_in=45.5,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=39.5,
                hips_in=47.5,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
        }
    ),
    "AMIT_AGGARWAL": BrandProfileSizing(
        brand_id="AMIT_AGGARWAL",
        brand_name="Amit Aggarwal Industrial Couture",
        origin_country="India",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=33.5,
                waist_in=27.5,
                hips_in=34.5,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=35.5,
                waist_in=29.5,
                hips_in=36.5,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=-0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=37.5,
                waist_in=31.5,
                hips_in=38.5,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=-0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=39.5,
                waist_in=33.5,
                hips_in=40.5,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=-0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=41.5,
                waist_in=35.5,
                hips_in=42.5,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=43.5,
                waist_in=37.5,
                hips_in=44.5,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=-0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=45.5,
                waist_in=39.5,
                hips_in=46.5,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=-0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=47.5,
                waist_in=41.5,
                hips_in=48.5,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=-0.5
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=25.5,
                hips_in=33.5,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=27.5,
                hips_in=35.5,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=29.5,
                hips_in=37.5,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=31.5,
                hips_in=39.5,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=33.5,
                hips_in=41.5,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=35.5,
                hips_in=43.5,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=37.5,
                hips_in=45.5,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=39.5,
                hips_in=47.5,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
        }
    ),
    "PAYAL_KHANDWALA": BrandProfileSizing(
        brand_id="PAYAL_KHANDWALA",
        brand_name="Payal Khandwala Minimalist",
        origin_country="India",
        cut_archetype="INDIAN_CONTEMPORARY",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=35.0,
                waist_in=29.0,
                hips_in=36.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=37.0,
                waist_in=31.0,
                hips_in=38.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=39.0,
                waist_in=33.0,
                hips_in=40.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=41.0,
                waist_in=35.0,
                hips_in=42.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=43.0,
                waist_in=37.0,
                hips_in=44.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=45.0,
                waist_in=39.0,
                hips_in=46.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=47.0,
                waist_in=41.0,
                hips_in=48.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=49.0,
                waist_in=43.0,
                hips_in=50.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=1.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=27.0,
                hips_in=35.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=29.0,
                hips_in=37.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=31.0,
                hips_in=39.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=33.0,
                hips_in=41.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=35.0,
                hips_in=43.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=37.0,
                hips_in=45.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=39.0,
                hips_in=47.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=41.0,
                hips_in=49.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
        }
    ),
    "BODICE_STUDIO": BrandProfileSizing(
        brand_id="BODICE_STUDIO",
        brand_name="Bodice Studio Architectural",
        origin_country="India",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "KALLOL_DATTA": BrandProfileSizing(
        brand_id="KALLOL_DATTA",
        brand_name="Kallol Datta 1955",
        origin_country="India",
        cut_archetype="ASIAN_COMPACT",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "EKA_LIFESTYLE": BrandProfileSizing(
        brand_id="EKA_LIFESTYLE",
        brand_name="Eka Handcrafted Linens",
        origin_country="India",
        cut_archetype="INDIAN_CONTEMPORARY",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=35.5,
                waist_in=29.5,
                hips_in=36.5,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=1.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=37.5,
                waist_in=31.5,
                hips_in=38.5,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=1.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=39.5,
                waist_in=33.5,
                hips_in=40.5,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=1.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=41.5,
                waist_in=35.5,
                hips_in=42.5,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=1.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=43.5,
                waist_in=37.5,
                hips_in=44.5,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=1.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=45.5,
                waist_in=39.5,
                hips_in=46.5,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=1.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=47.5,
                waist_in=41.5,
                hips_in=48.5,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=1.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=49.5,
                waist_in=43.5,
                hips_in=50.5,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=1.5
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=27.5,
                hips_in=35.5,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=29.5,
                hips_in=37.5,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=31.5,
                hips_in=39.5,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=33.5,
                hips_in=41.5,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=35.5,
                hips_in=43.5,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=37.5,
                hips_in=45.5,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=39.5,
                hips_in=47.5,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=41.5,
                hips_in=49.5,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
        }
    ),
    "PERO_ANEETH_ARORA": BrandProfileSizing(
        brand_id="PERO_ANEETH_ARORA",
        brand_name="péro by Aneeth Arora",
        origin_country="India",
        cut_archetype="INDIAN_CONTEMPORARY",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=35.0,
                waist_in=29.0,
                hips_in=36.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=37.0,
                waist_in=31.0,
                hips_in=38.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=39.0,
                waist_in=33.0,
                hips_in=40.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=41.0,
                waist_in=35.0,
                hips_in=42.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=43.0,
                waist_in=37.0,
                hips_in=44.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=45.0,
                waist_in=39.0,
                hips_in=46.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=47.0,
                waist_in=41.0,
                hips_in=48.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=49.0,
                waist_in=43.0,
                hips_in=50.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=1.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=27.0,
                hips_in=35.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=29.0,
                hips_in=37.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=31.0,
                hips_in=39.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=33.0,
                hips_in=41.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=35.0,
                hips_in=43.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=37.0,
                hips_in=45.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=39.0,
                hips_in=47.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=41.0,
                hips_in=49.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
        }
    ),
    "HUEMN_STREETWEAR": BrandProfileSizing(
        brand_id="HUEMN_STREETWEAR",
        brand_name="Huemn Urban Culture",
        origin_country="India",
        cut_archetype="AMERICAN_RELAXED",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=35.0,
                waist_in=29.0,
                hips_in=36.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=37.0,
                waist_in=31.0,
                hips_in=38.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=39.0,
                waist_in=33.0,
                hips_in=40.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=41.0,
                waist_in=35.0,
                hips_in=42.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=43.0,
                waist_in=37.0,
                hips_in=44.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=45.0,
                waist_in=39.0,
                hips_in=46.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=47.0,
                waist_in=41.0,
                hips_in=48.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=49.0,
                waist_in=43.0,
                hips_in=50.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=1.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=27.0,
                hips_in=35.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=29.0,
                hips_in=37.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=31.0,
                hips_in=39.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=33.0,
                hips_in=41.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=35.0,
                hips_in=43.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=37.0,
                hips_in=45.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=39.0,
                hips_in=47.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=41.0,
                hips_in=49.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
        }
    ),
    "ALMOST_GODS": BrandProfileSizing(
        brand_id="ALMOST_GODS",
        brand_name="Almost Gods Luxury Streetwear",
        origin_country="India",
        cut_archetype="AMERICAN_RELAXED",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=35.5,
                waist_in=29.5,
                hips_in=36.5,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=1.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=37.5,
                waist_in=31.5,
                hips_in=38.5,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=1.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=39.5,
                waist_in=33.5,
                hips_in=40.5,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=1.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=41.5,
                waist_in=35.5,
                hips_in=42.5,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=1.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=43.5,
                waist_in=37.5,
                hips_in=44.5,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=1.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=45.5,
                waist_in=39.5,
                hips_in=46.5,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=1.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=47.5,
                waist_in=41.5,
                hips_in=48.5,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=1.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=49.5,
                waist_in=43.5,
                hips_in=50.5,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=1.5
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=27.5,
                hips_in=35.5,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=29.5,
                hips_in=37.5,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=31.5,
                hips_in=39.5,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=33.5,
                hips_in=41.5,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=35.5,
                hips_in=43.5,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=37.5,
                hips_in=45.5,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=39.5,
                hips_in=47.5,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=41.5,
                hips_in=49.5,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
        }
    ),
    "NOR_BLACK_NOR_WHITE": BrandProfileSizing(
        brand_id="NOR_BLACK_NOR_WHITE",
        brand_name="Nor Black Nor White",
        origin_country="India",
        cut_archetype="AMERICAN_RELAXED",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=35.0,
                waist_in=29.0,
                hips_in=36.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=37.0,
                waist_in=31.0,
                hips_in=38.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=39.0,
                waist_in=33.0,
                hips_in=40.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=41.0,
                waist_in=35.0,
                hips_in=42.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=43.0,
                waist_in=37.0,
                hips_in=44.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=45.0,
                waist_in=39.0,
                hips_in=46.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=47.0,
                waist_in=41.0,
                hips_in=48.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=49.0,
                waist_in=43.0,
                hips_in=50.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=1.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=27.0,
                hips_in=35.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=29.0,
                hips_in=37.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=31.0,
                hips_in=39.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=33.0,
                hips_in=41.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=35.0,
                hips_in=43.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=37.0,
                hips_in=45.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=39.0,
                hips_in=47.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=41.0,
                hips_in=49.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
        }
    ),
    "COS_MINIMAL": BrandProfileSizing(
        brand_id="COS_MINIMAL",
        brand_name="COS Minimalist Tailoring",
        origin_country="United Kingdom",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "TOTEME_STOCKHOLM": BrandProfileSizing(
        brand_id="TOTEME_STOCKHOLM",
        brand_name="Totême Stockholm",
        origin_country="Sweden",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "LEMAIRE_PARIS": BrandProfileSizing(
        brand_id="LEMAIRE_PARIS",
        brand_name="Lemaire Paris",
        origin_country="France",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "THE_ROW_NYC": BrandProfileSizing(
        brand_id="THE_ROW_NYC",
        brand_name="The Row Luxury Essentials",
        origin_country="United States",
        cut_archetype="AMERICAN_RELAXED",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=35.0,
                waist_in=29.0,
                hips_in=36.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=37.0,
                waist_in=31.0,
                hips_in=38.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=39.0,
                waist_in=33.0,
                hips_in=40.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=41.0,
                waist_in=35.0,
                hips_in=42.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=43.0,
                waist_in=37.0,
                hips_in=44.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=45.0,
                waist_in=39.0,
                hips_in=46.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=47.0,
                waist_in=41.0,
                hips_in=48.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=49.0,
                waist_in=43.0,
                hips_in=50.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=1.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=27.0,
                hips_in=35.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=29.0,
                hips_in=37.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=31.0,
                hips_in=39.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=33.0,
                hips_in=41.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=35.0,
                hips_in=43.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=37.0,
                hips_in=45.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=39.0,
                hips_in=47.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=41.0,
                hips_in=49.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
        }
    ),
    "KHAITE_NY": BrandProfileSizing(
        brand_id="KHAITE_NY",
        brand_name="Khaite New York",
        origin_country="United States",
        cut_archetype="AMERICAN_RELAXED",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.5,
                waist_in=28.5,
                hips_in=35.5,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.5,
                waist_in=30.5,
                hips_in=37.5,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.5,
                waist_in=32.5,
                hips_in=39.5,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.5,
                waist_in=34.5,
                hips_in=41.5,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.5,
                waist_in=36.5,
                hips_in=43.5,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.5,
                waist_in=38.5,
                hips_in=45.5,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.5,
                waist_in=40.5,
                hips_in=47.5,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.5,
                waist_in=42.5,
                hips_in=49.5,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.5
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.5,
                hips_in=34.5,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.5,
                hips_in=36.5,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.5,
                hips_in=38.5,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.5,
                hips_in=40.5,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.5,
                hips_in=42.5,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.5,
                hips_in=44.5,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.5,
                hips_in=46.5,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.5,
                hips_in=48.5,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.5
            ),
        }
    ),
    "JIL_SANDER": BrandProfileSizing(
        brand_id="JIL_SANDER",
        brand_name="Jil Sander Pure",
        origin_country="Germany",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "DRIES_VAN_NOTEN": BrandProfileSizing(
        brand_id="DRIES_VAN_NOTEN",
        brand_name="Dries Van Noten",
        origin_country="Belgium",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "MAISON_MARGIELA": BrandProfileSizing(
        brand_id="MAISON_MARGIELA",
        brand_name="Maison Margiela Artisanal",
        origin_country="France",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=33.5,
                waist_in=27.5,
                hips_in=34.5,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=35.5,
                waist_in=29.5,
                hips_in=36.5,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=-0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=37.5,
                waist_in=31.5,
                hips_in=38.5,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=-0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=39.5,
                waist_in=33.5,
                hips_in=40.5,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=-0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=41.5,
                waist_in=35.5,
                hips_in=42.5,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=43.5,
                waist_in=37.5,
                hips_in=44.5,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=-0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=45.5,
                waist_in=39.5,
                hips_in=46.5,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=-0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=47.5,
                waist_in=41.5,
                hips_in=48.5,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=-0.5
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=25.5,
                hips_in=33.5,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=27.5,
                hips_in=35.5,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=29.5,
                hips_in=37.5,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=31.5,
                hips_in=39.5,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=33.5,
                hips_in=41.5,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=35.5,
                hips_in=43.5,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=37.5,
                hips_in=45.5,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=39.5,
                hips_in=47.5,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
        }
    ),
    "ACNE_STUDIOS": BrandProfileSizing(
        brand_id="ACNE_STUDIOS",
        brand_name="Acne Studios Stockholm",
        origin_country="Sweden",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "FEAR_OF_GOD": BrandProfileSizing(
        brand_id="FEAR_OF_GOD",
        brand_name="Fear of God Luxury Street",
        origin_country="United States",
        cut_archetype="AMERICAN_RELAXED",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=2.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=2.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=2.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=2.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=2.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=2.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=2.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=50.0,
                waist_in=44.0,
                hips_in=51.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=2.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=42.0,
                hips_in=50.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
        }
    ),
    "RHUDE_LA": BrandProfileSizing(
        brand_id="RHUDE_LA",
        brand_name="Rhude Los Angeles",
        origin_country="United States",
        cut_archetype="AMERICAN_RELAXED",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=35.5,
                waist_in=29.5,
                hips_in=36.5,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=1.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=37.5,
                waist_in=31.5,
                hips_in=38.5,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=1.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=39.5,
                waist_in=33.5,
                hips_in=40.5,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=1.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=41.5,
                waist_in=35.5,
                hips_in=42.5,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=1.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=43.5,
                waist_in=37.5,
                hips_in=44.5,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=1.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=45.5,
                waist_in=39.5,
                hips_in=46.5,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=1.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=47.5,
                waist_in=41.5,
                hips_in=48.5,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=1.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=49.5,
                waist_in=43.5,
                hips_in=50.5,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=1.5
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=27.5,
                hips_in=35.5,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=29.5,
                hips_in=37.5,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=31.5,
                hips_in=39.5,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=33.5,
                hips_in=41.5,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=35.5,
                hips_in=43.5,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=37.5,
                hips_in=45.5,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=39.5,
                hips_in=47.5,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=41.5,
                hips_in=49.5,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
        }
    ),
    "STUSSY_WORLDWIDE": BrandProfileSizing(
        brand_id="STUSSY_WORLDWIDE",
        brand_name="Stüssy Worldwide",
        origin_country="United States",
        cut_archetype="AMERICAN_RELAXED",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=35.5,
                waist_in=29.5,
                hips_in=36.5,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=1.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=37.5,
                waist_in=31.5,
                hips_in=38.5,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=1.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=39.5,
                waist_in=33.5,
                hips_in=40.5,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=1.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=41.5,
                waist_in=35.5,
                hips_in=42.5,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=1.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=43.5,
                waist_in=37.5,
                hips_in=44.5,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=1.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=45.5,
                waist_in=39.5,
                hips_in=46.5,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=1.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=47.5,
                waist_in=41.5,
                hips_in=48.5,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=1.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=49.5,
                waist_in=43.5,
                hips_in=50.5,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=1.5
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=27.5,
                hips_in=35.5,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=29.5,
                hips_in=37.5,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=31.5,
                hips_in=39.5,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=33.5,
                hips_in=41.5,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=35.5,
                hips_in=43.5,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=37.5,
                hips_in=45.5,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=39.5,
                hips_in=47.5,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=41.5,
                hips_in=49.5,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.5
            ),
        }
    ),
    "KITH_NYC": BrandProfileSizing(
        brand_id="KITH_NYC",
        brand_name="Kith New York",
        origin_country="United States",
        cut_archetype="AMERICAN_RELAXED",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=35.0,
                waist_in=29.0,
                hips_in=36.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=37.0,
                waist_in=31.0,
                hips_in=38.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=39.0,
                waist_in=33.0,
                hips_in=40.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=41.0,
                waist_in=35.0,
                hips_in=42.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=43.0,
                waist_in=37.0,
                hips_in=44.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=45.0,
                waist_in=39.0,
                hips_in=46.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=47.0,
                waist_in=41.0,
                hips_in=48.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=49.0,
                waist_in=43.0,
                hips_in=50.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=1.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=27.0,
                hips_in=35.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=29.0,
                hips_in=37.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=31.0,
                hips_in=39.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=33.0,
                hips_in=41.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=35.0,
                hips_in=43.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=37.0,
                hips_in=45.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=39.0,
                hips_in=47.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=41.0,
                hips_in=49.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=1.0
            ),
        }
    ),
    "UNDERCOVER_JUN_TAKAHASHI": BrandProfileSizing(
        brand_id="UNDERCOVER_JUN_TAKAHASHI",
        brand_name="Undercover Jun Takahashi",
        origin_country="Japan",
        cut_archetype="ASIAN_COMPACT",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=33.0,
                waist_in=27.0,
                hips_in=34.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=35.0,
                waist_in=29.0,
                hips_in=36.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=-1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=37.0,
                waist_in=31.0,
                hips_in=38.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=-1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=39.0,
                waist_in=33.0,
                hips_in=40.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=-1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=41.0,
                waist_in=35.0,
                hips_in=42.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=43.0,
                waist_in=37.0,
                hips_in=44.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=-1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=45.0,
                waist_in=39.0,
                hips_in=46.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=-1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=47.0,
                waist_in=41.0,
                hips_in=48.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=-1.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=25.0,
                hips_in=33.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=27.0,
                hips_in=35.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=29.0,
                hips_in=37.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=31.0,
                hips_in=39.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=33.0,
                hips_in=41.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=35.0,
                hips_in=43.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=37.0,
                hips_in=45.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=39.0,
                hips_in=47.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
        }
    ),
    "COMME_DES_GARCONS": BrandProfileSizing(
        brand_id="COMME_DES_GARCONS",
        brand_name="Comme des Garçons",
        origin_country="Japan",
        cut_archetype="ASIAN_COMPACT",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=33.0,
                waist_in=27.0,
                hips_in=34.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=35.0,
                waist_in=29.0,
                hips_in=36.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=-1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=37.0,
                waist_in=31.0,
                hips_in=38.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=-1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=39.0,
                waist_in=33.0,
                hips_in=40.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=-1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=41.0,
                waist_in=35.0,
                hips_in=42.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=43.0,
                waist_in=37.0,
                hips_in=44.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=-1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=45.0,
                waist_in=39.0,
                hips_in=46.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=-1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=47.0,
                waist_in=41.0,
                hips_in=48.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=-1.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=25.0,
                hips_in=33.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=27.0,
                hips_in=35.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=29.0,
                hips_in=37.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=31.0,
                hips_in=39.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=33.0,
                hips_in=41.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=35.0,
                hips_in=43.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=37.0,
                hips_in=45.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=39.0,
                hips_in=47.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-1.0
            ),
        }
    ),
    "YOHJI_YAMAMOTO": BrandProfileSizing(
        brand_id="YOHJI_YAMAMOTO",
        brand_name="Yohji Yamamoto Pour Homme",
        origin_country="Japan",
        cut_archetype="ASIAN_COMPACT",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=2.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=2.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=2.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=2.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=2.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=2.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=2.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=50.0,
                waist_in=44.0,
                hips_in=51.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=2.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=42.0,
                hips_in=50.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=2.0
            ),
        }
    ),
    "ISSEY_MIYAKE_PLEATS": BrandProfileSizing(
        brand_id="ISSEY_MIYAKE_PLEATS",
        brand_name="Issey Miyake Pleats Please",
        origin_country="Japan",
        cut_archetype="ASIAN_COMPACT",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "VISVIM_INDIGO": BrandProfileSizing(
        brand_id="VISVIM_INDIGO",
        brand_name="Visvim Okayama Handcraft",
        origin_country="Japan",
        cut_archetype="ASIAN_COMPACT",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=33.5,
                waist_in=27.5,
                hips_in=34.5,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=35.5,
                waist_in=29.5,
                hips_in=36.5,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=-0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=37.5,
                waist_in=31.5,
                hips_in=38.5,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=-0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=39.5,
                waist_in=33.5,
                hips_in=40.5,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=-0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=41.5,
                waist_in=35.5,
                hips_in=42.5,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=43.5,
                waist_in=37.5,
                hips_in=44.5,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=-0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=45.5,
                waist_in=39.5,
                hips_in=46.5,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=-0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=47.5,
                waist_in=41.5,
                hips_in=48.5,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=-0.5
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=25.5,
                hips_in=33.5,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=27.5,
                hips_in=35.5,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=29.5,
                hips_in=37.5,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=31.5,
                hips_in=39.5,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=33.5,
                hips_in=41.5,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=35.5,
                hips_in=43.5,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=37.5,
                hips_in=45.5,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=39.5,
                hips_in=47.5,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
        }
    ),
    "KAPITAL_DENIM": BrandProfileSizing(
        brand_id="KAPITAL_DENIM",
        brand_name="Kapital Kountry",
        origin_country="Japan",
        cut_archetype="ASIAN_COMPACT",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "A_COLD_WALL": BrandProfileSizing(
        brand_id="A_COLD_WALL",
        brand_name="A-Cold-Wall* Industrial",
        origin_country="United Kingdom",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "CRAIG_GREEN": BrandProfileSizing(
        brand_id="CRAIG_GREEN",
        brand_name="Craig Green Monastic",
        origin_country="United Kingdom",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "JACQUEMUS_PROVENCE": BrandProfileSizing(
        brand_id="JACQUEMUS_PROVENCE",
        brand_name="Jacquemus Le Sud",
        origin_country="France",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=33.5,
                waist_in=27.5,
                hips_in=34.5,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=35.5,
                waist_in=29.5,
                hips_in=36.5,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=-0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=37.5,
                waist_in=31.5,
                hips_in=38.5,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=-0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=39.5,
                waist_in=33.5,
                hips_in=40.5,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=-0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=41.5,
                waist_in=35.5,
                hips_in=42.5,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=43.5,
                waist_in=37.5,
                hips_in=44.5,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=-0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=45.5,
                waist_in=39.5,
                hips_in=46.5,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=-0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=47.5,
                waist_in=41.5,
                hips_in=48.5,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=-0.5
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=25.5,
                hips_in=33.5,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=27.5,
                hips_in=35.5,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=29.5,
                hips_in=37.5,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=31.5,
                hips_in=39.5,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=33.5,
                hips_in=41.5,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=35.5,
                hips_in=43.5,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=37.5,
                hips_in=45.5,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=39.5,
                hips_in=47.5,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=-0.5
            ),
        }
    ),
    "LOEWE_MADRID": BrandProfileSizing(
        brand_id="LOEWE_MADRID",
        brand_name="Loewe Madrid 1846",
        origin_country="Spain",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "BOTTEGA_VENETA": BrandProfileSizing(
        brand_id="BOTTEGA_VENETA",
        brand_name="Bottega Veneta Intrecciato",
        origin_country="Italy",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "BRUNELLO_CUCINELLI": BrandProfileSizing(
        brand_id="BRUNELLO_CUCINELLI",
        brand_name="Brunello Cucinelli Solomeo",
        origin_country="Italy",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "LORO_PIANA_CASHMERE": BrandProfileSizing(
        brand_id="LORO_PIANA_CASHMERE",
        brand_name="Loro Piana Cashmere",
        origin_country="Italy",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "CANALI_SARTORIA": BrandProfileSizing(
        brand_id="CANALI_SARTORIA",
        brand_name="Canali 1934 Sartoria",
        origin_country="Italy",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "ZEGNA_OASI": BrandProfileSizing(
        brand_id="ZEGNA_OASI",
        brand_name="Zegna Oasi Cashmere",
        origin_country="Italy",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
    "BOGLIOLI_MILANO": BrandProfileSizing(
        brand_id="BOGLIOLI_MILANO",
        brand_name="Boglioli Milano",
        origin_country="Italy",
        cut_archetype="EUROPEAN_SLIM",
        tops_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=34.0,
                waist_in=28.0,
                hips_in=35.0,
                shoulder_in=16.7,
                length_in=28.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=36.0,
                waist_in=30.0,
                hips_in=37.0,
                shoulder_in=17.1,
                length_in=28.5,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=38.0,
                waist_in=32.0,
                hips_in=39.0,
                shoulder_in=17.5,
                length_in=29.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=40.0,
                waist_in=34.0,
                hips_in=41.0,
                shoulder_in=17.9,
                length_in=29.5,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=42.0,
                waist_in=36.0,
                hips_in=43.0,
                shoulder_in=18.3,
                length_in=30.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=44.0,
                waist_in=38.0,
                hips_in=45.0,
                shoulder_in=18.7,
                length_in=30.5,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=46.0,
                waist_in=40.0,
                hips_in=47.0,
                shoulder_in=19.1,
                length_in=31.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=48.0,
                waist_in=42.0,
                hips_in=49.0,
                shoulder_in=19.5,
                length_in=31.5,
                vanity_sizing_offset_in=0.0
            ),
        },
        bottoms_size_chart={
            "XXS": BrandSizeMeasurement(
                size_label="XXS",
                chest_in=0.0,
                waist_in=26.0,
                hips_in=34.0,
                inseam_in=31.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XS": BrandSizeMeasurement(
                size_label="XS",
                chest_in=0.0,
                waist_in=28.0,
                hips_in=36.0,
                inseam_in=31.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "S": BrandSizeMeasurement(
                size_label="S",
                chest_in=0.0,
                waist_in=30.0,
                hips_in=38.0,
                inseam_in=32.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "M": BrandSizeMeasurement(
                size_label="M",
                chest_in=0.0,
                waist_in=32.0,
                hips_in=40.0,
                inseam_in=32.2,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "L": BrandSizeMeasurement(
                size_label="L",
                chest_in=0.0,
                waist_in=34.0,
                hips_in=42.0,
                inseam_in=32.4,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XL": BrandSizeMeasurement(
                size_label="XL",
                chest_in=0.0,
                waist_in=36.0,
                hips_in=44.0,
                inseam_in=32.6,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "XXL": BrandSizeMeasurement(
                size_label="XXL",
                chest_in=0.0,
                waist_in=38.0,
                hips_in=46.0,
                inseam_in=32.8,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
            "3XL": BrandSizeMeasurement(
                size_label="3XL",
                chest_in=0.0,
                waist_in=40.0,
                hips_in=48.0,
                inseam_in=33.0,
                shoulder_in=0.0,
                length_in=41.0,
                vanity_sizing_offset_in=0.0
            ),
        }
    ),
}
