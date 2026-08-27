from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class CategoryAttributeBase(BaseModel):
    name: str
    attribute_type: str = "MULTI_SELECT"
    is_required: bool = False
    is_filterable: bool = True
    allowed_values: List[str] = []


class CategoryAttributeCreate(CategoryAttributeBase):
    pass


class CategoryAttributeOut(CategoryAttributeBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    category_id: str


class CategoryBase(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None
    parent_id: Optional[str] = None
    level: int = 0
    image_url: Optional[str] = None
    banner_url: Optional[str] = None
    icon_name: Optional[str] = None
    is_active: bool = True
    display_order: int = 0
    commission_rate: float = 15.0


class CategoryCreate(CategoryBase):
    attributes: Optional[List[CategoryAttributeCreate]] = None


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    parent_id: Optional[str] = None
    level: Optional[int] = None
    image_url: Optional[str] = None
    banner_url: Optional[str] = None
    icon_name: Optional[str] = None
    is_active: Optional[bool] = None
    display_order: Optional[int] = None
    commission_rate: Optional[float] = None


class CategoryOut(CategoryBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    created_at: datetime
    attributes: List[CategoryAttributeOut] = []


class CategoryTreeOut(CategoryOut):
    subcategories: List["CategoryTreeOut"] = []
