from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class CartItemAdd(BaseModel):
    product_id: str
    variant_id: str
    quantity: int = Field(1, ge=1, le=10)


class CartItemUpdate(BaseModel):
    quantity: int = Field(..., ge=0, le=10)


class CartItemOut(BaseModel):
    id: str
    product_id: str
    variant_id: str
    product_title: str
    product_slug: str
    brand_name: Optional[str] = None
    vendor_id: str
    image_url: Optional[str] = None
    size: str
    color_name: str
    unit_price: float
    mrp: float
    quantity: int
    item_subtotal: float
    is_in_stock: bool = True


class VendorCartGroup(BaseModel):
    vendor_id: str
    vendor_name: Optional[str] = None
    items: List[CartItemOut]
    vendor_subtotal: float
    shipping_fee: float


class CartOut(BaseModel):
    id: str
    user_id: Optional[str] = None
    session_id: Optional[str] = None
    items_count: int
    items: List[CartItemOut]
    vendor_groups: List[VendorCartGroup]
    subtotal: float
    total_mrp: float
    discount_amount: float
    shipping_fee: float
    estimated_total: float
    coupon_applied: Optional[str] = None
    coupon_discount: float = 0.0
