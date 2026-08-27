import enum
from datetime import datetime
from typing import Optional
from sqlalchemy import (
    String, Boolean, DateTime, JSON, ForeignKey, Enum as SQLEnum, Text
)
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base_model import BaseModel, get_utc_now


class OTPPurpose(str, enum.Enum):
    REGISTRATION = "REGISTRATION"
    LOGIN = "LOGIN"
    PASSWORD_RESET = "PASSWORD_RESET"
    PHONE_VERIFICATION = "PHONE_VERIFICATION"


class RefreshToken(BaseModel):
    __tablename__ = "refresh_tokens"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    token: Mapped[str] = mapped_column(String(500), unique=True, index=True, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    is_revoked: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    device_info: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    ip_address: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)


class OTPRequest(BaseModel):
    __tablename__ = "otp_requests"

    identifier: Mapped[str] = mapped_column(String(255), index=True, nullable=False) # Email or Phone
    otp_code: Mapped[str] = mapped_column(String(10), nullable=False)
    purpose: Mapped[OTPPurpose] = mapped_column(SQLEnum(OTPPurpose), default=OTPPurpose.LOGIN, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    attempts: Mapped[int] = mapped_column(default=0, nullable=False)


class AuditLog(BaseModel):
    __tablename__ = "audit_logs"

    actor_id: Mapped[Optional[str]] = mapped_column(String(36), index=True, nullable=True)
    actor_role: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    action: Mapped[str] = mapped_column(String(100), index=True, nullable=False) # e.g., USER_LOGIN, VENDOR_APPROVED
    resource_type: Mapped[str] = mapped_column(String(100), index=True, nullable=False) # e.g., USER, PRODUCT, ORDER
    resource_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    ip_address: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    details: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
