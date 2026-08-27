from typing import List, Dict, Any, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.products.schemas import ProductListOut


class ExtractedFashionTokens(BaseModel):
    query: str
    detected_gender: Optional[str] = None
    detected_category: Optional[str] = None
    detected_color: Optional[str] = None
    detected_fit: Optional[str] = None
    detected_occasion: Optional[str] = None
    detected_fabric: Optional[str] = None
    detected_season: Optional[str] = None
    remaining_keywords: List[str] = []


class FacetBucket(BaseModel):
    key: str
    count: int


class FacetsResponse(BaseModel):
    categories: List[FacetBucket] = []
    brands: List[FacetBucket] = []
    colors: List[FacetBucket] = []
    sizes: List[FacetBucket] = []
    occasions: List[FacetBucket] = []
    fits: List[FacetBucket] = []
    fabrics: List[FacetBucket] = []
    price_ranges: List[FacetBucket] = []


class SearchResponse(BaseModel):
    query: str
    extracted_tokens: ExtractedFashionTokens
    items: List[Dict[str, Any]]
    total: int
    page: int
    limit: int
    facets: Optional[FacetsResponse] = None


class AutocompleteItem(BaseModel):
    title: str
    type: str # "PRODUCT", "CATEGORY", "BRAND", "OCCASION", "COLLECTION"
    slug: str
    image_url: Optional[str] = None


class AutocompleteResponse(BaseModel):
    suggestions: List[AutocompleteItem]
    trending_searches: List[str]


class CollectionItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    product_id: str
    display_order: int


class FashionCollectionBase(BaseModel):
    title: str
    slug: str
    tagline: Optional[str] = None
    description: Optional[str] = None
    banner_image_url: Optional[str] = None
    season: Optional[str] = None
    occasion: Optional[str] = None
    is_active: bool = True
    is_featured: bool = False
    display_order: int = 0
    style_tags: List[str] = []


class FashionCollectionCreate(FashionCollectionBase):
    pass


class FashionCollectionUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    tagline: Optional[str] = None
    description: Optional[str] = None
    banner_image_url: Optional[str] = None
    season: Optional[str] = None
    occasion: Optional[str] = None
    is_active: Optional[bool] = None
    is_featured: Optional[bool] = None
    display_order: Optional[int] = None
    style_tags: Optional[List[str]] = None


class FashionCollectionOut(FashionCollectionBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    created_at: datetime
    products: List[Dict[str, Any]] = []


class AddProductsToCollection(BaseModel):
    product_ids: List[str]
