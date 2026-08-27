from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class InventoryItemBase(BaseModel):
    variant_id: str
    sku: str
    vendor_id: str
    physical_stock: int = 0
    low_stock_threshold: int = 5
    warehouse_location: Optional[str] = None


class InventoryItemCreate(InventoryItemBase):
    pass


class InventoryStockAdjust(BaseModel):
    quantity_delta: int # Positive to add stock, negative to deduct
    reason: str


class InventoryItemOut(InventoryItemBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    reserved_stock: int
    available_stock: int
    created_at: datetime
