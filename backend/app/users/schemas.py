from typing import List, Optional
from datetime import datetime, date
from pydantic import BaseModel, EmailStr, ConfigDict, Field
from app.users.models import UserRole, GenderPreference, FitPreference, AddressType


class UserAddressBase(BaseModel):
    address_type: AddressType = AddressType.HOME
    full_name: str
    phone_number: str
    street_address: str
    landmark: Optional[str] = None
    city: str
    state: str
    postal_code: str
    country: str = "India"
    is_default: bool = False
    delivery_instructions: Optional[str] = None


class UserAddressCreate(UserAddressBase):
    pass


class UserAddressUpdate(BaseModel):
    address_type: Optional[AddressType] = None
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    street_address: Optional[str] = None
    landmark: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    is_default: Optional[bool] = None
    delivery_instructions: Optional[str] = None


class UserAddressOut(UserAddressBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime


class UserSizeProfileBase(BaseModel):
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    chest_in: Optional[float] = None
    waist_in: Optional[float] = None
    hips_in: Optional[float] = None
    inseam_in: Optional[float] = None
    shoulder_in: Optional[float] = None
    shoe_size_uk: Optional[float] = None
    preferred_top_size: Optional[str] = None
    preferred_bottom_size: Optional[str] = None
    fit_preference: FitPreference = FitPreference.REGULAR


class UserSizeProfileCreate(UserSizeProfileBase):
    pass


class UserSizeProfileUpdate(UserSizeProfileBase):
    pass


class UserSizeProfileOut(UserSizeProfileBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime


class FashionDNABase(BaseModel):
    style_personas: List[str] = Field(default_factory=list)
    favorite_colors: List[str] = Field(default_factory=list)
    preferred_brands: List[str] = Field(default_factory=list)
    preferred_categories: List[str] = Field(default_factory=list)
    occasion_interests: List[str] = Field(default_factory=list)
    price_sensitivity: str = "MID_RANGE"


class FashionDNACreate(FashionDNABase):
    pass


class FashionDNAUpdate(FashionDNABase):
    pass


class FashionDNAOut(FashionDNABase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime


class UserProfileBase(BaseModel):
    bio: Optional[str] = None
    language_preference: str = "en"
    currency_preference: str = "INR"
    notification_settings: Optional[dict] = None


class UserProfileUpdate(UserProfileBase):
    pass


class UserProfileOut(UserProfileBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    user_id: str
    created_at: datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
    first_name: str
    last_name: Optional[str] = None
    phone: Optional[str] = None
    role: UserRole = UserRole.CUSTOMER
    gender_preference: GenderPreference = GenderPreference.ALL
    date_of_birth: Optional[date] = None


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    avatar_url: Optional[str] = None
    gender_preference: Optional[GenderPreference] = None
    date_of_birth: Optional[date] = None


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    email: EmailStr
    first_name: str
    last_name: Optional[str] = None
    phone: Optional[str] = None
    role: UserRole
    is_active: bool
    is_verified: bool
    avatar_url: Optional[str] = None
    gender_preference: GenderPreference
    date_of_birth: Optional[date] = None
    created_at: datetime
    profile: Optional[UserProfileOut] = None
    size_profile: Optional[UserSizeProfileOut] = None
    style_preference: Optional[FashionDNAOut] = None
