import enum
from typing import List, Optional
from datetime import date
from sqlalchemy import (
    String, Boolean, Float, Date, JSON, ForeignKey, Enum as SQLEnum, Text
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import BaseModel


class UserRole(str, enum.Enum):
    SUPER_ADMIN = "SUPER_ADMIN"
    ADMIN = "ADMIN"
    MODERATOR = "MODERATOR"
    VENDOR_OWNER = "VENDOR_OWNER"
    VENDOR_MANAGER = "VENDOR_MANAGER"
    CUSTOMER = "CUSTOMER"


class GenderPreference(str, enum.Enum):
    MEN = "MEN"
    WOMEN = "WOMEN"
    ALL = "ALL"
    KIDS = "KIDS"


class FitPreference(str, enum.Enum):
    SLIM = "SLIM"
    REGULAR = "REGULAR"
    OVERSIZED = "OVERSIZED"
    TAILORED = "TAILORED"
    RELAXED = "RELAXED"


class AddressType(str, enum.Enum):
    HOME = "HOME"
    WORK = "WORK"
    OTHER = "OTHER"


class User(BaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    phone: Mapped[Optional[str]] = mapped_column(String(20), unique=True, index=True, nullable=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    role: Mapped[UserRole] = mapped_column(SQLEnum(UserRole), default=UserRole.CUSTOMER, nullable=False, index=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    avatar_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    gender_preference: Mapped[GenderPreference] = mapped_column(SQLEnum(GenderPreference), default=GenderPreference.ALL, nullable=False)
    date_of_birth: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    # Relationships
    profile: Mapped[Optional["UserProfile"]] = relationship("UserProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    addresses: Mapped[List["UserAddress"]] = relationship("UserAddress", back_populates="user", cascade="all, delete-orphan")
    size_profile: Mapped[Optional["UserSizeProfile"]] = relationship("UserSizeProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    style_preference: Mapped[Optional["UserStylePreference"]] = relationship("UserStylePreference", back_populates="user", uselist=False, cascade="all, delete-orphan")


class UserProfile(BaseModel):
    __tablename__ = "user_profiles"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    bio: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    language_preference: Mapped[str] = mapped_column(String(10), default="en", nullable=False)
    currency_preference: Mapped[str] = mapped_column(String(10), default="INR", nullable=False)
    notification_settings: Mapped[dict] = mapped_column(JSON, default=lambda: {
        "email_orders": True,
        "email_promotions": True,
        "sms_orders": True,
        "push_recommendations": True,
        "price_drop_alerts": True
    }, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="profile")


class UserAddress(BaseModel):
    __tablename__ = "user_addresses"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    address_type: Mapped[AddressType] = mapped_column(SQLEnum(AddressType), default=AddressType.HOME, nullable=False)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)
    street_address: Mapped[str] = mapped_column(String(255), nullable=False)
    landmark: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    state: Mapped[str] = mapped_column(String(100), nullable=False)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    country: Mapped[str] = mapped_column(String(100), default="India", nullable=False)
    is_default: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    delivery_instructions: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="addresses")


class UserSizeProfile(BaseModel):
    """Fashion Intelligence: Body Measurements & Size Preferences"""
    __tablename__ = "user_size_profiles"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    height_cm: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    weight_kg: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    chest_in: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    waist_in: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    hips_in: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    inseam_in: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    shoulder_in: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    shoe_size_uk: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    preferred_top_size: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)   # S, M, L, XL
    preferred_bottom_size: Mapped[Optional[str]] = mapped_column(String(10), nullable=True) # 30, 32, 34
    fit_preference: Mapped[FitPreference] = mapped_column(SQLEnum(FitPreference), default=FitPreference.REGULAR, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="size_profile")


class UserStylePreference(BaseModel):
    """Fashion DNA Profile: Styles, Colors, Occasions and Brand affinities"""
    __tablename__ = "user_style_preferences"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    style_personas: Mapped[List[str]] = mapped_column(JSON, default=list, nullable=False)  # ["Minimalist", "Streetwear", "Ethnic", "Casual"]
    favorite_colors: Mapped[List[str]] = mapped_column(JSON, default=list, nullable=False)  # ["Black", "Navy Blue", "Olive", "White"]
    preferred_brands: Mapped[List[str]] = mapped_column(JSON, default=list, nullable=False)
    preferred_categories: Mapped[List[str]] = mapped_column(JSON, default=list, nullable=False)
    occasion_interests: Mapped[List[str]] = mapped_column(JSON, default=list, nullable=False) # ["Office", "Party", "Wedding", "Travel"]
    price_sensitivity: Mapped[str] = mapped_column(String(20), default="MID_RANGE", nullable=False) # BUDGET, MID_RANGE, PREMIUM, LUXURY

    user: Mapped["User"] = relationship("User", back_populates="style_preference")
