from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class WishlistItemAdd(BaseModel):
    product_id: str
    desired_size: Optional[str] = None
    desired_color: Optional[str] = None


class WishlistItemOut(BaseModel):
    id: str
    product_id: str
    product_title: str
    product_slug: str
    brand_name: Optional[str] = None
    image_url: Optional[str] = None
    current_price: float
    original_price_added: float
    has_price_dropped: bool
    price_difference: float
    desired_size: Optional[str] = None
    desired_color: Optional[str] = None
    created_at: datetime


class WishlistOut(BaseModel):
    id: str
    user_id: str
    name: str
    is_public: bool
    share_token: Optional[str] = None
    items_count: int
    items: List[WishlistItemOut]
