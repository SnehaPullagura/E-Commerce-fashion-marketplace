import enum
from typing import List, Optional
from datetime import datetime
from sqlalchemy import (
    String, Boolean, Float, Integer, JSON, ForeignKey, Enum as SQLEnum, Text, DateTime
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import BaseModel, get_utc_now


class VendorStatus(str, enum.Enum):
    PENDING = "PENDING"
    UNDER_REVIEW = "UNDER_REVIEW"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    SUSPENDED = "SUSPENDED"


class VendorProfile(BaseModel):
    __tablename__ = "vendor_profiles"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    business_name: Mapped[str] = mapped_column(String(150), unique=True, index=True, nullable=False)
    legal_name: Mapped[str] = mapped_column(String(150), nullable=False)
    slug: Mapped[str] = mapped_column(String(160), unique=True, index=True, nullable=False)

    # KYC & Business Tax Identification
    gst_number: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    pan_number: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)

    # Banking details for payouts
    bank_account_name: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    bank_account_number: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    bank_ifsc: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    bank_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    status: Mapped[VendorStatus] = mapped_column(SQLEnum(VendorStatus), default=VendorStatus.PENDING, nullable=False, index=True)
    commission_rate: Mapped[float] = mapped_column(Float, default=15.0, nullable=False) # Marketplace commission %

    # Storefront Customization
    logo_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    banner_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    support_email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    support_phone: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)

    city: Mapped[str] = mapped_column(String(100), default="Mumbai", nullable=False)
    state: Mapped[str] = mapped_column(String(100), default="Maharashtra", nullable=False)
    postal_code: Mapped[str] = mapped_column(String(20), default="400001", nullable=False)

    rating: Mapped[float] = mapped_column(Float, default=5.0, nullable=False)
    total_sales_amount: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    total_earnings_paid: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)

    # Relationships
    documents: Mapped[List["VendorDocument"]] = relationship("VendorDocument", back_populates="vendor", cascade="all, delete-orphan")
    payouts: Mapped[List["VendorPayout"]] = relationship("VendorPayout", back_populates="vendor", cascade="all, delete-orphan")


class VendorDocument(BaseModel):
    __tablename__ = "vendor_documents"

    vendor_id: Mapped[str] = mapped_column(String(36), ForeignKey("vendor_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    document_type: Mapped[str] = mapped_column(String(50), nullable=False) # GST_CERTIFICATE, PAN_CARD, CANCELLED_CHEQUE
    document_url: Mapped[str] = mapped_column(String(500), nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    vendor: Mapped["VendorProfile"] = relationship("VendorProfile", back_populates="documents")


class VendorPayout(BaseModel):
    __tablename__ = "vendor_payouts"

    vendor_id: Mapped[str] = mapped_column(String(36), ForeignKey("vendor_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    payout_reference: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="PAID", nullable=False) # PENDING, PROCESSING, PAID, FAILED
    period_start: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    period_end: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    bank_reference_id: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    processed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=get_utc_now, nullable=False)

    vendor: Mapped["VendorProfile"] = relationship("VendorProfile", back_populates="payouts")
