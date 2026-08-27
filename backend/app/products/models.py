import enum
from typing import List, Optional
from sqlalchemy import (
    String, Boolean, Float, Integer, JSON, ForeignKey, Enum as SQLEnum, Text
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import BaseModel


class ProductStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    PUBLISHED = "PUBLISHED"
    REJECTED = "REJECTED"
    ARCHIVED = "ARCHIVED"


class ProductGender(str, enum.Enum):
    MEN = "MEN"
    WOMEN = "WOMEN"
    UNISEX = "UNISEX"
    KIDS = "KIDS"


class FitType(str, enum.Enum):
    SLIM = "SLIM"
    REGULAR = "REGULAR"
    OVERSIZED = "OVERSIZED"
    TAILORED = "TAILORED"
    RELAXED = "RELAXED"
    SKINNY = "SKINNY"


class OccasionType(str, enum.Enum):
    CASUAL = "CASUAL"
    FORMAL = "FORMAL"
    OFFICE = "OFFICE"
    PARTY = "PARTY"
    WEDDING = "WEDDING"
    FESTIVAL = "FESTIVAL"
    STREETWEAR = "STREETWEAR"
    TRAVEL = "TRAVEL"
    SPORTS = "SPORTS"
    LOUNGEWEAR = "LOUNGEWEAR"


class SeasonType(str, enum.Enum):
    SUMMER = "SUMMER"
    WINTER = "WINTER"
    MONSOON = "MONSOON"
    SPRING = "SPRING"
    AUTUMN = "AUTUMN"
    ALL_SEASON = "ALL_SEASON"


class Brand(BaseModel):
    __tablename__ = "brands"

    name: Mapped[str] = mapped_column(String(150), unique=True, index=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(160), unique=True, index=True, nullable=False)
    logo_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    banner_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    country_of_origin: Mapped[str] = mapped_column(String(100), default="India", nullable=False)
    website: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    # Relationships
    products: Mapped[List["Product"]] = relationship("Product", back_populates="brand")
    size_charts: Mapped[List["BrandSizeChart"]] = relationship("BrandSizeChart", back_populates="brand")


class BrandSizeChart(BaseModel):
    """Brand-Specific Size Guide for Smart Size Recommendations"""
    __tablename__ = "brand_size_charts"

    brand_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("brands.id", ondelete="CASCADE"), nullable=True, index=True)
    category_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("categories.id", ondelete="CASCADE"), nullable=True, index=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False) # e.g. "Zara Men's Shirts Size Chart"
    chart_type: Mapped[str] = mapped_column(String(50), default="TOPWEAR", nullable=False) # TOPWEAR, BOTTOMWEAR, FOOTWEAR, ACCESSORY
    unit: Mapped[str] = mapped_column(String(10), default="INCHES", nullable=False) # INCHES, CM

    brand: Mapped[Optional["Brand"]] = relationship("Brand", back_populates="size_charts")
    measurements: Mapped[List["SizeChartMeasurement"]] = relationship("SizeChartMeasurement", back_populates="size_chart", cascade="all, delete-orphan")


class SizeChartMeasurement(BaseModel):
    __tablename__ = "size_chart_measurements"

    size_chart_id: Mapped[str] = mapped_column(String(36), ForeignKey("brand_size_charts.id", ondelete="CASCADE"), nullable=False, index=True)
    size_label: Mapped[str] = mapped_column(String(20), nullable=False) # XS, S, M, L, XL, XXL or 28, 30, 32, 34
    chest_min: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    chest_max: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    waist_min: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    waist_max: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    hips_min: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    hips_max: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    shoulder: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    length: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    inseam: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    foot_length_cm: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    size_chart: Mapped["BrandSizeChart"] = relationship("BrandSizeChart", back_populates="measurements")


class Product(BaseModel):
    __tablename__ = "products"

    vendor_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False) # Links to vendor profile / user
    brand_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("brands.id", ondelete="SET NULL"), nullable=True, index=True)
    category_id: Mapped[str] = mapped_column(String(36), ForeignKey("categories.id", ondelete="RESTRICT"), nullable=False, index=True)
    size_chart_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("brand_size_charts.id", ondelete="SET NULL"), nullable=True)

    title: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(280), unique=True, index=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    base_mrp: Mapped[float] = mapped_column(Float, nullable=False) # Maximum Retail Price
    base_price: Mapped[float] = mapped_column(Float, nullable=False) # Selling Price
    discount_percentage: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    gender: Mapped[ProductGender] = mapped_column(SQLEnum(ProductGender), default=ProductGender.UNISEX, nullable=False, index=True)

    # Fashion Specific Attributes
    fabric: Mapped[Optional[str]] = mapped_column(String(100), nullable=True, index=True) # 100% Pure Cotton, Raw Denim, Silk Georgette
    material: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    fit_type: Mapped[FitType] = mapped_column(SQLEnum(FitType), default=FitType.REGULAR, nullable=False, index=True)
    pattern: Mapped[Optional[str]] = mapped_column(String(100), nullable=True, index=True) # Solid, Striped, Checkered, Floral, Printed
    occasion: Mapped[OccasionType] = mapped_column(SQLEnum(OccasionType), default=OccasionType.CASUAL, nullable=False, index=True)
    season: Mapped[SeasonType] = mapped_column(SQLEnum(SeasonType), default=SeasonType.ALL_SEASON, nullable=False, index=True)
    care_instructions: Mapped[Optional[str]] = mapped_column(Text, nullable=True) # Machine wash cold, do not bleach
    style_tags: Mapped[List[str]] = mapped_column(JSON, default=list, nullable=False) # ["streetwear", "oversized", "graphic-tee", "aesthetic"]
    color_palette: Mapped[List[str]] = mapped_column(JSON, default=list, nullable=False) # Primary colors represented

    status: Mapped[ProductStatus] = mapped_column(SQLEnum(ProductStatus), default=ProductStatus.PUBLISHED, nullable=False, index=True)
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, index=True)
    is_trending: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, index=True)
    average_rating: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    review_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    return_window_days: Mapped[int] = mapped_column(Integer, default=7, nullable=False)

    # Relationships
    brand: Mapped[Optional["Brand"]] = relationship("Brand", back_populates="products")
    variants: Mapped[List["ProductVariant"]] = relationship("ProductVariant", back_populates="product", cascade="all, delete-orphan")
    images: Mapped[List["ProductImage"]] = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")


class ProductVariant(BaseModel):
    __tablename__ = "product_variants"

    product_id: Mapped[str] = mapped_column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    sku: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    size: Mapped[str] = mapped_column(String(30), nullable=False, index=True) # S, M, L, XL, 30, 32, UK 9
    color_name: Mapped[str] = mapped_column(String(50), nullable=False, index=True) # Midnight Black, Olive Green, Rust Orange
    color_hex: Mapped[Optional[str]] = mapped_column(String(10), nullable=True) # #000000, #556B2F
    mrp: Mapped[float] = mapped_column(Float, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    barcode: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    weight_grams: Mapped[Optional[float]] = mapped_column(Float, default=300.0, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    product: Mapped["Product"] = relationship("Product", back_populates="variants")


class ProductImage(BaseModel):
    __tablename__ = "product_images"

    product_id: Mapped[str] = mapped_column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    variant_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("product_variants.id", ondelete="SET NULL"), nullable=True)
    image_url: Mapped[str] = mapped_column(String(500), nullable=False)
    alt_text: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    color_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_primary: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    product: Mapped["Product"] = relationship("Product", back_populates="images")
