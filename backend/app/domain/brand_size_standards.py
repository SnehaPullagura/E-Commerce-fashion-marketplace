"""
Designer Brand Sizing Standards & Anthropometric Deviation Registry.
Maintains official brand size charts, vanity sizing compensation factors,
and cut archetypes across international luxury & designer brands.
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


def _build_brand_size_chart(
    base_chest: float,
    base_waist: float,
    base_hips: float,
    step_in: float = 2.0,
    vanity_offset: float = 0.0
) -> Dict[str, BrandSizeMeasurement]:
    """Generates standard anthropometric size distribution (XXS to XXL)."""
    labels = ["XXS", "XS", "S", "M", "L", "XL", "XXL"]
    chart = {}
    for idx, label in enumerate(labels):
        offset = (idx - 1) * step_in  # M is index 3
        chart[label] = BrandSizeMeasurement(
            size_label=label,
            chest_in=round(base_chest + offset + vanity_offset, 1),
            waist_in=round(base_waist + offset + vanity_offset, 1),
            hips_in=round(base_hips + offset + vanity_offset, 1),
            shoulder_in=round(16.5 + (idx * 0.4), 1),
            length_in=round(27.5 + (idx * 0.5), 1),
            vanity_sizing_offset_in=vanity_offset
        )
    return chart


BRAND_CATALOG_DEFINITIONS = [
    ("NOIR_COUTURE", "Noir Couture Atelier", "India", "INDIAN_CONTEMPORARY", 38.0, 32.0, 39.0, 0.0),
    ("AURELIA_MILANO", "Aurelia Milano", "Italy", "EUROPEAN_SLIM", 36.0, 30.0, 37.0, -0.5),
    ("SAVILE_ROW_BESPOKE", "Savile Row Bespoke", "United Kingdom", "EUROPEAN_SLIM", 37.0, 31.0, 38.0, 0.0),
    ("TOKYO_MINIMAL", "Tokyo Minimalist", "Japan", "ASIAN_COMPACT", 35.0, 29.0, 36.0, -1.0),
    ("HUDSON_HERITAGE", "Hudson Heritage", "United States", "AMERICAN_RELAXED", 40.0, 34.0, 41.0, 1.5),
    ("PARISIAN_ATELIER", "Parisian Atelier", "France", "EUROPEAN_SLIM", 36.5, 30.5, 37.5, -0.5),
    ("NORDIC_ESSENTIALS", "Nordic Essentials", "Sweden", "EUROPEAN_SLIM", 38.5, 32.5, 39.5, 0.5),
    ("ROYAL_RAJPUTANA", "Royal Rajputana Silks", "India", "INDIAN_CONTEMPORARY", 39.0, 33.0, 40.0, 0.5),
    ("BEVERLY_HILLS_LUXE", "Beverly Hills Luxe", "United States", "AMERICAN_RELAXED", 41.0, 35.0, 42.0, 1.5),
    ("SEOUL_STREET_STUDIO", "Seoul Street Studio", "South Korea", "ASIAN_COMPACT", 35.5, 29.5, 36.5, -0.5),
]

BRAND_SIZING_REGISTRY: Dict[str, BrandProfileSizing] = {
    brand_id: BrandProfileSizing(
        brand_id=brand_id,
        brand_name=name,
        origin_country=country,
        cut_archetype=archetype,
        tops_size_chart=_build_brand_size_chart(chest, waist, hips, vanity_offset=v_off),
        bottoms_size_chart=_build_brand_size_chart(chest - 2.0, waist, hips, vanity_offset=v_off)
    )
    for brand_id, name, country, archetype, chest, waist, hips, v_off in BRAND_CATALOG_DEFINITIONS
}
