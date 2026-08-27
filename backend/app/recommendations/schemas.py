from typing import List, Optional, Dict, Any
from pydantic import BaseModel, ConfigDict


class OutfitItem(BaseModel):
    id: str
    title: str
    slug: str
    category_role: str # "MAIN_PIECE", "TOPWEAR", "BOTTOMWEAR", "FOOTWEAR", "ACCESSORY"
    brand_name: Optional[str] = None
    price: float
    mrp: float
    discount_percentage: float
    image_url: Optional[str] = None
    color_name: Optional[str] = None
    fit_type: str
    match_reason: str


class CompleteTheLookResponse(BaseModel):
    main_product_id: str
    main_product_title: str
    outfit_style_theme: str # e.g., "Smart Casual Office Look" or "Weekend Summer Streetwear"
    occasion: str
    outfit_items: List[OutfitItem]
    bundle_total_mrp: float
    bundle_discount_price: float
    bundle_savings: float
    bundle_discount_percentage: float = 10.0 # Extra 10% off for bundle


class PersonalizedFeedItem(BaseModel):
    product_id: str
    title: str
    slug: str
    brand_name: Optional[str] = None
    base_price: float
    base_mrp: float
    discount_percentage: float
    primary_image: Optional[str] = None
    fit_type: str
    occasion: str
    fabric: Optional[str] = None
    fashion_dna_match_score: float # e.g. 96.5%
    match_tags: List[str] = [] # ["Matches your Minimalist persona", "Favorite Color: Black", "Top Size: M in stock"]


class PersonalizedFeedResponse(BaseModel):
    fashion_persona: List[str]
    preferred_occasions: List[str]
    items: List[PersonalizedFeedItem]
    total: int
