from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import User
from app.users.schemas import UserCreate, UserOut
from app.authentication.schemas import (
    LoginRequest,
    TokenResponse,
    RefreshTokenRequest,
    OTPRequestCreate,
    OTPVerifyRequest,
)
from app.authentication.service import AuthService
from app.authentication.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate, request: Request, db: AsyncSession = Depends(get_db)):
    user = await AuthService.register(db, user_in)
    await AuthService.log_audit(
        db,
        action="USER_REGISTERED",
        resource_type="USER",
        actor_id=user.id,
        actor_role=user.role.value,
        resource_id=user.id,
        ip_address=request.client.host if request.client else None
    )
    return user


@router.post("/login", response_model=TokenResponse)
async def login(login_data: LoginRequest, request: Request, db: AsyncSession = Depends(get_db)):
    user = await AuthService.authenticate(db, login_data.email, login_data.password)
    user_agent = request.headers.get("User-Agent")
    ip_addr = request.client.host if request.client else None
    tokens = await AuthService.create_tokens(db, user, device_info=user_agent, ip_address=ip_addr)

    await AuthService.log_audit(
        db,
        action="USER_LOGIN",
        resource_type="USER",
        actor_id=user.id,
        actor_role=user.role.value,
        resource_id=user.id,
        ip_address=ip_addr
    )
    return tokens


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(
    refresh_in: RefreshTokenRequest,
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    user_agent = request.headers.get("User-Agent")
    ip_addr = request.client.host if request.client else None
    return await AuthService.refresh_tokens(
        db,
        refresh_in.refresh_token,
        device_info=user_agent,
        ip_address=ip_addr
    )


@router.post("/otp/request")
async def request_otp(otp_in: OTPRequestCreate, db: AsyncSession = Depends(get_db)):
    code = await AuthService.send_otp(db, otp_in.identifier, otp_in.purpose)
    return {
        "success": True,
        "message": f"OTP sent successfully to {otp_in.identifier}",
        "mock_code": code # In production environment, sent via SMS/Email provider
    }


@router.post("/otp/verify")
async def verify_otp(verify_in: OTPVerifyRequest, db: AsyncSession = Depends(get_db)):
    is_valid = await AuthService.verify_otp(
        db, verify_in.identifier, verify_in.otp_code, verify_in.purpose
    )
    return {"success": is_valid, "message": "OTP verified successfully"}


@router.get("/me", response_model=UserOut)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user
