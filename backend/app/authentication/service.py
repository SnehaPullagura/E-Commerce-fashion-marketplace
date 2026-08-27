import random
from datetime import datetime, timedelta, timezone
from typing import Optional, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload

from app.core.config import settings
from app.core.security import (
    verify_password,
    get_password_hash,
    create_access_token,
    create_refresh_token,
    decode_token,
)
from app.core.exceptions import (
    BadRequestException,
    UnauthorizedException,
    ConflictException,
    NotFoundException,
)
from app.core.events import event_bus, EventType
from app.users.models import User, UserProfile, UserSizeProfile, UserStylePreference, UserRole
from app.users.schemas import UserCreate
from app.authentication.models import RefreshToken, OTPRequest, OTPPurpose, AuditLog
from app.authentication.schemas import TokenResponse


class AuthService:
    @staticmethod
    async def register(db: AsyncSession, user_in: UserCreate) -> User:
        # Check existing email
        stmt = select(User).where(User.email == user_in.email.lower())
        res = await db.execute(stmt)
        if res.scalar_one_or_none():
            raise ConflictException(f"User with email '{user_in.email}' already exists")

        # Check phone if provided
        if user_in.phone:
            stmt_phone = select(User).where(User.phone == user_in.phone)
            res_phone = await db.execute(stmt_phone)
            if res_phone.scalar_one_or_none():
                raise ConflictException("Phone number already in use")

        # Create user
        user = User(
            email=user_in.email.lower(),
            phone=user_in.phone,
            hashed_password=get_password_hash(user_in.password),
            first_name=user_in.first_name,
            last_name=user_in.last_name,
            role=user_in.role,
            gender_preference=user_in.gender_preference,
            date_of_birth=user_in.date_of_birth,
            is_verified=False
        )
        db.add(user)
        await db.flush()

        # Initialize profile, size profile and style preference (Fashion DNA)
        profile = UserProfile(user_id=user.id)
        size_profile = UserSizeProfile(user_id=user.id)
        style_preference = UserStylePreference(user_id=user.id)
        db.add_all([profile, size_profile, style_preference])
        await db.commit()

        # Reload with relationships
        stmt_reload = (
            select(User)
            .options(
                selectinload(User.profile),
                selectinload(User.size_profile),
                selectinload(User.style_preference),
                selectinload(User.addresses)
            )
            .where(User.id == user.id)
        )
        result = await db.execute(stmt_reload)
        created_user = result.scalar_one()

        # Dispatch event
        await event_bus.publish(
            EventType.USER_REGISTERED,
            {"user_id": created_user.id, "email": created_user.email, "role": created_user.role.value}
        )

        return created_user

    @staticmethod
    async def authenticate(db: AsyncSession, email: str, password: str) -> User:
        stmt = (
            select(User)
            .options(
                selectinload(User.profile),
                selectinload(User.size_profile),
                selectinload(User.style_preference),
                selectinload(User.addresses)
            )
            .where(User.email == email.lower(), User.is_deleted == False)
        )
        res = await db.execute(stmt)
        user = res.scalar_one_or_none()

        if not user or not verify_password(password, user.hashed_password):
            raise UnauthorizedException("Invalid email or password")
        if not user.is_active:
            raise UnauthorizedException("Your account has been deactivated")

        return user

    @staticmethod
    async def create_tokens(
        db: AsyncSession,
        user: User,
        device_info: Optional[str] = None,
        ip_address: Optional[str] = None
    ) -> TokenResponse:
        access_token = create_access_token(
            subject=user.id,
            role=user.role.value,
            extra_claims={"email": user.email, "first_name": user.first_name}
        )
        refresh_token = create_refresh_token(subject=user.id, role=user.role.value)

        # Store refresh token record
        expires_at = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        token_record = RefreshToken(
            user_id=user.id,
            token=refresh_token,
            expires_at=expires_at,
            device_info=device_info,
            ip_address=ip_address
        )
        db.add(token_record)
        await db.commit()

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer",
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            user_id=user.id,
            role=user.role,
            first_name=user.first_name,
            email=user.email
        )

    @staticmethod
    async def refresh_tokens(
        db: AsyncSession,
        refresh_token_str: str,
        device_info: Optional[str] = None,
        ip_address: Optional[str] = None
    ) -> TokenResponse:
        payload = decode_token(refresh_token_str)
        if not payload or payload.get("type") != "refresh":
            raise UnauthorizedException("Invalid refresh token")

        stmt = select(RefreshToken).where(
            RefreshToken.token == refresh_token_str,
            RefreshToken.is_revoked == False
        )
        res = await db.execute(stmt)
        token_record = res.scalar_one_or_none()

        if not token_record or token_record.expires_at < datetime.now(timezone.utc):
            raise UnauthorizedException("Refresh token is expired or revoked")

        # Invalidate old refresh token (Rotation)
        token_record.is_revoked = True

        # Fetch user
        stmt_user = (
            select(User)
            .options(
                selectinload(User.profile),
                selectinload(User.size_profile),
                selectinload(User.style_preference),
                selectinload(User.addresses)
            )
            .where(User.id == token_record.user_id, User.is_active == True)
        )
        user_res = await db.execute(stmt_user)
        user = user_res.scalar_one_or_none()
        if not user:
            raise UnauthorizedException("User not found or inactive")

        # Generate new pair
        return await AuthService.create_tokens(db, user, device_info, ip_address)

    @staticmethod
    async def send_otp(db: AsyncSession, identifier: str, purpose: OTPPurpose) -> str:
        # Generate 6 digit code
        code = f"{random.randint(100000, 999999)}"
        expires_at = datetime.now(timezone.utc) + timedelta(minutes=10)

        otp = OTPRequest(
            identifier=identifier.lower().strip(),
            otp_code=code,
            purpose=purpose,
            expires_at=expires_at,
            is_verified=False
        )
        db.add(otp)
        await db.commit()
        return code

    @staticmethod
    async def verify_otp(db: AsyncSession, identifier: str, code: str, purpose: OTPPurpose) -> bool:
        stmt = select(OTPRequest).where(
            OTPRequest.identifier == identifier.lower().strip(),
            OTPRequest.purpose == purpose,
            OTPRequest.is_verified == False
        ).order_by(OTPRequest.created_at.desc())
        res = await db.execute(stmt)
        otp = res.scalar_one_or_none()

        if not otp:
            raise BadRequestException("Invalid or expired OTP")

        if otp.expires_at < datetime.now(timezone.utc):
            raise BadRequestException("OTP has expired")

        if otp.otp_code != code:
            otp.attempts += 1
            await db.commit()
            raise BadRequestException("Incorrect OTP code")

        otp.is_verified = True
        await db.commit()
        return True

    @staticmethod
    async def log_audit(
        db: AsyncSession,
        action: str,
        resource_type: str,
        actor_id: Optional[str] = None,
        actor_role: Optional[str] = None,
        resource_id: Optional[str] = None,
        details: Optional[dict] = None,
        ip_address: Optional[str] = None
    ) -> None:
        log = AuditLog(
            actor_id=actor_id,
            actor_role=actor_role,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            details=details or {},
            ip_address=ip_address
        )
        db.add(log)
        await db.commit()
