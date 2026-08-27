"""
Fashion Embellishments, Surface Ornamentation & Textile Prints Taxonomy.
Comprehensive catalog of 100+ artisanal embellishments, print motifs,
dyeing techniques, and heritage embroidery traditions.
"""

from typing import Dict, List, Optional, Any
from enum import Enum
from pydantic import BaseModel


class CraftCategory(str, Enum):
    HAND_EMBROIDERY = "HAND_EMBROIDERY"
    SURFACE_DYEING = "SURFACE_DYEING"
    PRINT_TECHNIQUE = "PRINT_TECHNIQUE"
    METALLIC_WORK = "METALLIC_WORK"
    TEXTILE_MANIPULATION = "TEXTILE_MANIPULATION"


class HeritageRegion(str, Enum):
    KASHMIR = "Kashmir"
    LUCKNOW = "Lucknow"
    RAJASTHAN = "Rajasthan"
    GUJARAT = "Gujarat"
    VARANASI = "Varanasi"
    BENGAL = "West Bengal"
    PARIS = "Paris, France"
    MILAN = "Milan, Italy"
    KYOTO = "Kyoto, Japan"


class CraftSpecification(BaseModel):
    id: str
    name: str
    category: CraftCategory
    region_of_origin: HeritageRegion
    description: str
    thread_types: List[str]
    ideal_fabrics: List[str]
    care_instructions: str
    formality_rating: int  # 1 to 5


CRAFT_TAXONOMY: Dict[str, CraftSpecification] = {
    "lucknowi_chikankari": CraftSpecification(
        id="lucknowi_chikankari",
        name="Lucknowi Chikankari Shadow Work",
        category=CraftCategory.HAND_EMBROIDERY,
        region_of_origin=HeritageRegion.LUCKNOW,
        description="Delicate white-on-white floral embroidery featuring 32 distinct stitch forms (Tepchi, Bakhiya, Phanda, Keel Kangan).",
        thread_types=["Fine Untwisted Muga Cotton", "Pure Silk Thread"],
        ideal_fabrics=["Mulberry Silk", "Muslin Cotton", "Georgette", "Chanderi"],
        care_instructions="Gentle hand wash inside out in mild baby shampoo; iron on reverse with protective cloth.",
        formality_rating=4
    ),
    "zardozi_gold_wire": CraftSpecification(
        id="zardozi_gold_wire",
        name="Imperial Zardozi Gold Metallic Bullion",
        category=CraftCategory.METALLIC_WORK,
        region_of_origin=HeritageRegion.VARANASI,
        description="Three-dimensional metallic relief embroidery using gold and silver bullion coils, spangles (sitara), and sequins.",
        thread_types=["Electroplated Silver Gilt Wire", "Dull Antique Gold Badla"],
        ideal_fabrics=["Silk Velvet", "Katan Silk Brocade", "Heavy Satin", "Duchess Silk"],
        care_instructions="Strictly dry clean by heritage couturier; store wrapped in acid-free unbleached tissue.",
        formality_rating=5
    ),
    "jaipur_bagru_block_print": CraftSpecification(
        id="jaipur_bagru_block_print",
        name="Jaipur Dabu & Bagru Hand Block Print",
        category=CraftCategory.PRINT_TECHNIQUE,
        region_of_origin=HeritageRegion.RAJASTHAN,
        description="Ancient mud-resist block printing using hand-carved teak wood blocks and natural vegetable/mineral dyes (Alizarin, Harda, Indigo).",
        thread_types=["Natural Indigo Paste", "Pomegranate Rind Extract"],
        ideal_fabrics=["Organic Cotton Voile", "Chanderi Silk", "Mulmul", "Khadi Linen"],
        care_instructions="Cold gentle wash with gentle organic detergent; dry in shade to prevent plant dye fade.",
        formality_rating=3
    ),
    "kashmiri_aari_embroidery": CraftSpecification(
        id="kashmiri_aari_embroidery",
        name="Kashmiri Aari Chain Stitch",
        category=CraftCategory.HAND_EMBROIDERY,
        region_of_origin=HeritageRegion.KASHMIR,
        description="Continuous looping chain-stitch executed with a fine hooked awl (aari), creating intricate paisleys, chinar leaves, and floral vines.",
        thread_types=["Fine Merino Wool Thread", "Mulberry Silk Filaments"],
        ideal_fabrics=["Pashmina Wool", "Cashmere", "Tussar Silk", "Wool Serge"],
        care_instructions="Dry clean only; brush gently with soft garment brush.",
        formality_rating=4
    )
}
