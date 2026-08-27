from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.users.models import UserRole
from app.vendors.models import VendorStatus
from app.products.models import ProductStatus


class PlatformSettingCreate(BaseModel):
    key: str
    value: str
    description: Optional[str] = None
    is_public: bool = False


class PlatformSettingOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    key: str
    value: str
    description: Optional[str] = None
    is_public: bool


class ModerateVendorRequest(BaseModel):
    status: VendorStatus # APPROVED, REJECTED, SUSPENDED
    commission_rate: Optional[float] = None
    reason: Optional[str] = None


class ModerateProductRequest(BaseModel):
    status: ProductStatus # PUBLISHED, REJECTED, ARCHIVED
    reason: Optional[str] = None


class AdminOverviewStats(BaseModel):
    total_users: int
    total_vendors: int
    pending_vendors: int
    total_products: int
    total_orders: int
    total_gmv: float
    total_revenue_commission: float
