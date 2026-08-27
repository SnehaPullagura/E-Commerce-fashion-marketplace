from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr
from app.vendors.models import VendorStatus


class VendorOnboardRequest(BaseModel):
    business_name: str
    legal_name: str
    slug: str
    gst_number: Optional[str] = None
    pan_number: Optional[str] = None
    bank_account_name: Optional[str] = None
    bank_account_number: Optional[str] = None
    bank_ifsc: Optional[str] = None
    bank_name: Optional[str] = None
    city: str
    state: str
    postal_code: str
    description: Optional[str] = None
    support_email: Optional[EmailStr] = None
    support_phone: Optional[str] = None


class VendorUpdateProfile(BaseModel):
    business_name: Optional[str] = None
    logo_url: Optional[str] = None
    banner_url: Optional[str] = None
    description: Optional[str] = None
    support_email: Optional[EmailStr] = None
    support_phone: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None


class VendorDocumentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    document_type: str
    document_url: str
    is_verified: bool


class VendorPayoutOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    payout_reference: str
    amount: float
    status: str
    period_start: datetime
    period_end: datetime
    processed_at: datetime


class VendorProfileOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    user_id: str
    business_name: str
    legal_name: str
    slug: str
    status: VendorStatus
    commission_rate: float
    logo_url: Optional[str] = None
    banner_url: Optional[str] = None
    description: Optional[str] = None
    support_email: Optional[str] = None
    support_phone: Optional[str] = None
    city: str
    state: str
    postal_code: str
    rating: float
    total_sales_amount: float
    total_earnings_paid: float
    created_at: datetime


class StorefrontOut(BaseModel):
    id: str
    business_name: str
    slug: str
    logo_url: Optional[str] = None
    banner_url: Optional[str] = None
    description: Optional[str] = None
    rating: float
    city: str
    state: str
    products_count: int
    products: List[dict] = []
