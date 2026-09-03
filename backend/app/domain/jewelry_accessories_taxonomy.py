"""
Fine Jewelry, Precious Metals, Gemstones & Luxury Leather Goods Taxonomy.
Defines precious metal karatage purity (24K, 22K, 18K, 14K, 925 Silver),
gemstone setting classifications (Polki, Kundan, Jadau, Pavé), and leather grain grades.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel


class AccessoryCraftProfile(BaseModel):
    item_code: str
    trade_name: str
    category: str
    base_material: str
    purity_specification: str
    setting_technique: str
    hallmark_certification_standard: str
    care_guidelines: List[str]
    formality_tier: int


JEWELRY_DEFINITIONS = [
    ("ACC_SOLITAIRE_PT", "Six-Prong Platinum Solitaire Ring", "FINE_JEWELRY", "Platinum 950", "95.0% Pure Platinum", "Six-Prong Classic Wire Setting", "GIA Certified Laser Inscribed", ["Ultrasonic clean safe", "Store in soft pouch"], 5),
    ("ACC_KUNDAN_CHOKER", "Heritage 22K Meenakari Kundan Choker", "HIGH_JEWELRY", "22K Yellow Gold", "91.6% Pure Gold (Hallmark 916)", "Jadau Kundan Foil Backing", "BIS Hallmarked & Gem Testing Lab Certified", ["Wipe with dry microfiber cloth", "Avoid moisture and perfume contact"], 5),
    ("ACC_POLKI_EARRINGS", "Uncut Natural Diamond Polki Chandbalis", "HERITAGE_JEWELRY", "18K Rose Gold", "75.0% Gold (Hallmark 750)", "Open-Setting Polki Collet", "IGI Authenticated Diamonds", ["Store flat in velvet-lined box", "Do not immerse in chemical solutions"], 5),
    ("ACC_CROCO_TOTE", "Full-Grain Saddle-Stitched Crocodile Embossed Tote", "LEATHER_GOODS", "Full-Grain French Calfskin", "Top Grain Aniline Finished Leather", "Hand-Waxed Linen Saddle Stitch", "Artisanal Leather Guild Certificate", ["Condition quarterly with natural beeswax balm", "Keep in dustbag away from heat"], 4),
    ("ACC_SILVER_CUFF", "925 Sterling Silver Tribal Filigree Cuff", "CONTEMPORARY_JEWELRY", "925 Sterling Silver", "92.5% Pure Silver (Hallmark 925)", "Intricate Wire Filigree", "BIS Silver Hallmarked", ["Clean with anti-tarnish polishing cloth", "Store in airtight zip pouch"], 3)
]

ACCESSORY_CRAFT_DATABASE: Dict[str, AccessoryCraftProfile] = {
    code: AccessoryCraftProfile(
        item_code=code,
        trade_name=name,
        category=cat,
        base_material=mat,
        purity_specification=purity,
        setting_technique=tech,
        hallmark_certification_standard=hallmark,
        care_guidelines=care,
        formality_tier=tier
    )
    for code, name, cat, mat, purity, tech, hallmark, care, tier in JEWELRY_DEFINITIONS
}
