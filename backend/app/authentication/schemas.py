from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from app.users.models import UserRole
from app.authentication.models import OTPPurpose


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int
    user_id: str
    role: UserRole
    first_name: str
    email: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class OTPRequestCreate(BaseModel):
    identifier: str # Email or mobile
    purpose: OTPPurpose = OTPPurpose.LOGIN


class OTPVerifyRequest(BaseModel):
    identifier: str
    otp_code: str
    purpose: OTPPurpose = OTPPurpose.LOGIN


class PasswordChangeRequest(BaseModel):
    current_password: str
    new_password: str = Field(..., min_length=6)


class PasswordResetRequest(BaseModel):
    email: EmailStr


class PasswordResetConfirm(BaseModel):
    token: str
    new_password: str = Field(..., min_length=6)
