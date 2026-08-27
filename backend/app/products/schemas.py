from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from app.products.models import (
    ProductStatus,
    ProductGender,
    FitType,
    OccasionType,
    SeasonType,
)


# --- Brand Schemas ---
class BrandBase(BaseModel):
    name: str
    slug: str
    logo_url: Optional[str] = None
    banner_url: Optional[str] = None
    description: Optional[str] = None
    country_of_origin: str = "India"
    website: Optional[str] = None
    is_verified: bool = True
    is_featured: bool = False


class BrandCreate(BrandBase):
    pass


class BrandUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    logo_url: Optional[str] = None
    banner_url: Optional[str] = None
    description: Optional[str] = None
    website: Optional[str] = None
    is_verified: Optional[bool] = None
    is_featured: Optional[bool] = None


class BrandOut(BrandBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    created_at: datetime


# --- Size Chart & Intelligence Schemas ---
class SizeMeasurementBase(BaseModel):
    size_label: str # S, M, L, XL or 28, 30, 32
    chest_min: Optional[float] = None
    chest_max: Optional[float] = None
    waist_min: Optional[float] = None
    waist_max: Optional[float] = None
    hips_min: Optional[float] = None
    hips_max: Optional[float] = None
    shoulder: Optional[float] = None
    length: Optional[float] = None
    inseam: Optional[float] = None
    foot_length_cm: Optional[float] = None


class SizeMeasurementCreate(SizeMeasurementBase):
    pass


class SizeMeasurementOut(SizeMeasurementBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    size_chart_id: str


class BrandSizeChartBase(BaseModel):
    title: str
    brand_id: Optional[str] = None
    category_id: Optional[str] = None
    chart_type: str = "TOPWEAR" # TOPWEAR, BOTTOMWEAR, FOOTWEAR
    unit: str = "INCHES"


class BrandSizeChartCreate(BrandSizeChartBase):
    measurements: List[SizeMeasurementCreate] = []


class BrandSizeChartOut(BrandSizeChartBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    created_at: datetime
    measurements: List[SizeMeasurementOut] = []


# --- Product Variant & Image Schemas ---
class ProductImageBase(BaseModel):
    image_url: str
    variant_id: Optional[str] = None
    alt_text: Optional[str] = None
    color_name: Optional[str] = None
    display_order: int = 0
    is_primary: bool = False


class ProductImageCreate(ProductImageBase):
    pass


class ProductImageOut(ProductImageBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    product_id: str


class ProductVariantBase(BaseModel):
    sku: str
    size: str
    color_name: str
    color_hex: Optional[str] = None
    mrp: float
    price: float
    barcode: Optional[str] = None
    weight_grams: float = 300.0
    is_active: bool = True


class ProductVariantCreate(ProductVariantBase):
    pass


class ProductVariantUpdate(BaseModel):
    size: Optional[str] = None
    color_name: Optional[str] = None
    color_hex: Optional[str] = None
    mrp: Optional[float] = None
    price: Optional[float] = None
    barcode: Optional[str] = None
    weight_grams: Optional[float] = None
    is_active: Optional[bool] = None


class ProductVariantOut(ProductVariantBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    product_id: str
    created_at: datetime


# --- Product Main Schemas ---
class ProductBase(BaseModel):
    title: str
    slug: str
    description: str
    brand_id: Optional[str] = None
    category_id: str
    size_chart_id: Optional[str] = None
    base_mrp: float
    base_price: float
    discount_percentage: float = 0.0
    gender: ProductGender = ProductGender.UNISEX

    # Fashion Attributes
    fabric: Optional[str] = None
    material: Optional[str] = None
    fit_type: FitType = FitType.REGULAR
    pattern: Optional[str] = None
    occasion: OccasionType = OccasionType.CASUAL
    season: SeasonType = SeasonType.ALL_SEASON
    care_instructions: Optional[str] = None
    style_tags: List[str] = []
    color_palette: List[str] = []
    return_window_days: int = 7


class ProductCreate(ProductBase):
    vendor_id: Optional[str] = None # Filled from current vendor session if omitted
    variants: List[ProductVariantCreate] = []
    images: List[ProductImageCreate] = []


class ProductUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    brand_id: Optional[str] = None
    category_id: Optional[str] = None
    size_chart_id: Optional[str] = None
    base_mrp: Optional[float] = None
    base_price: Optional[float] = None
    discount_percentage: Optional[float] = None
    gender: Optional[ProductGender] = None
    fabric: Optional[str] = None
    material: Optional[str] = None
    fit_type: Optional[FitType] = None
    pattern: Optional[str] = None
    occasion: Optional[OccasionType] = None
    season: Optional[SeasonType] = None
    care_instructions: Optional[str] = None
    style_tags: Optional[List[str]] = None
    color_palette: Optional[List[str]] = None
    status: Optional[ProductStatus] = None
    is_featured: Optional[bool] = None
    is_trending: Optional[bool] = None
    return_window_days: Optional[int] = None


class ProductListOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    vendor_id: str
    brand_id: Optional[str] = None
    category_id: str
    title: str
    slug: str
    base_mrp: float
    base_price: float
    discount_percentage: float
    gender: ProductGender
    fabric: Optional[str] = None
    fit_type: FitType
    pattern: Optional[str] = None
    occasion: OccasionType
    season: SeasonType
    status: ProductStatus
    is_featured: bool
    is_trending: bool
    average_rating: float
    review_count: int
    primary_image: Optional[str] = None
    colors: List[str] = []
    sizes: List[str] = []
    created_at: datetime


class ProductOut(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    vendor_id: str
    status: ProductStatus
    is_featured: bool
    is_trending: bool
    average_rating: float
    review_count: int
    created_at: datetime
    updated_at: datetime

    brand: Optional[BrandOut] = None
    variants: List[ProductVariantOut] = []
    images: List[ProductImageOut] = []


# --- Size Intelligence Schema ---
class SizeAdvisorRequest(BaseModel):
    chest_in: Optional[float] = None
    waist_in: Optional[float] = None
    hips_in: Optional[float] = None
    height_cm: Optional[float] = None
    fit_preference: Optional[FitType] = FitType.REGULAR


class SizeAdvisorResponse(BaseModel):
    recommended_size: str
    confidence_score: float # e.g. 0.95 (95%)
    fit_analysis: str # e.g. "Size M will provide a standard regular fit across chest (38-40 in)"
    size_measurements: Optional[SizeMeasurementOut] = None
