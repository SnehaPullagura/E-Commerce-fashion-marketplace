from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.orm import selectinload

from app.core.exceptions import NotFoundException, ForbiddenException
from app.users.models import User, UserProfile, UserAddress, UserSizeProfile, UserStylePreference
from app.users.schemas import (
    UserUpdate,
    UserProfileUpdate,
    UserAddressCreate,
    UserAddressUpdate,
    UserSizeProfileUpdate,
    FashionDNAUpdate,
)


class UserService:
    @staticmethod
    async def get_by_id(db: AsyncSession, user_id: str) -> User:
        stmt = (
            select(User)
            .options(
                selectinload(User.profile),
                selectinload(User.size_profile),
                selectinload(User.style_preference),
                selectinload(User.addresses)
            )
            .where(User.id == user_id, User.is_deleted == False)
        )
        res = await db.execute(stmt)
        user = res.scalar_one_or_none()
        if not user:
            raise NotFoundException("User not found")
        return user

    @staticmethod
    async def update_user(db: AsyncSession, user_id: str, user_in: UserUpdate) -> User:
        user = await UserService.get_by_id(db, user_id)
        update_data = user_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(user, key, value)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def update_profile(db: AsyncSession, user_id: str, profile_in: UserProfileUpdate) -> UserProfile:
        stmt = select(UserProfile).where(UserProfile.user_id == user_id)
        res = await db.execute(stmt)
        profile = res.scalar_one_or_none()
        if not profile:
            profile = UserProfile(user_id=user_id)
            db.add(profile)

        update_data = profile_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(profile, key, value)

        await db.commit()
        await db.refresh(profile)
        return profile

    @staticmethod
    async def get_addresses(db: AsyncSession, user_id: str) -> List[UserAddress]:
        stmt = (
            select(UserAddress)
            .where(UserAddress.user_id == user_id, UserAddress.is_deleted == False)
            .order_by(UserAddress.is_default.desc(), UserAddress.created_at.desc())
        )
        res = await db.execute(stmt)
        return list(res.scalars().all())

    @staticmethod
    async def create_address(db: AsyncSession, user_id: str, address_in: UserAddressCreate) -> UserAddress:
        if address_in.is_default:
            # Set other addresses as not default
            await db.execute(
                update(UserAddress)
                .where(UserAddress.user_id == user_id)
                .values(is_default=False)
            )

        address = UserAddress(user_id=user_id, **address_in.model_dump())
        db.add(address)
        await db.commit()
        await db.refresh(address)
        return address

    @staticmethod
    async def update_address(
        db: AsyncSession, user_id: str, address_id: str, address_in: UserAddressUpdate
    ) -> UserAddress:
        stmt = select(UserAddress).where(
            UserAddress.id == address_id,
            UserAddress.user_id == user_id,
            UserAddress.is_deleted == False
        )
        res = await db.execute(stmt)
        address = res.scalar_one_or_none()
        if not address:
            raise NotFoundException("Address not found")

        update_data = address_in.model_dump(exclude_unset=True)
        if update_data.get("is_default"):
            await db.execute(
                update(UserAddress)
                .where(UserAddress.user_id == user_id)
                .values(is_default=False)
            )

        for key, value in update_data.items():
            setattr(address, key, value)

        await db.commit()
        await db.refresh(address)
        return address

    @staticmethod
    async def delete_address(db: AsyncSession, user_id: str, address_id: str) -> bool:
        stmt = select(UserAddress).where(
            UserAddress.id == address_id,
            UserAddress.user_id == user_id,
            UserAddress.is_deleted == False
        )
        res = await db.execute(stmt)
        address = res.scalar_one_or_none()
        if not address:
            raise NotFoundException("Address not found")

        address.is_deleted = True
        await db.commit()
        return True

    @staticmethod
    async def update_size_profile(
        db: AsyncSession, user_id: str, size_in: UserSizeProfileUpdate
    ) -> UserSizeProfile:
        stmt = select(UserSizeProfile).where(UserSizeProfile.user_id == user_id)
        res = await db.execute(stmt)
        profile = res.scalar_one_or_none()
        if not profile:
            profile = UserSizeProfile(user_id=user_id)
            db.add(profile)

        update_data = size_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(profile, key, value)

        await db.commit()
        await db.refresh(profile)
        return profile

    @staticmethod
    async def update_fashion_dna(
        db: AsyncSession, user_id: str, style_in: FashionDNAUpdate
    ) -> UserStylePreference:
        stmt = select(UserStylePreference).where(UserStylePreference.user_id == user_id)
        res = await db.execute(stmt)
        dna = res.scalar_one_or_none()
        if not dna:
            dna = UserStylePreference(user_id=user_id)
            db.add(dna)

        update_data = style_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(dna, key, value)

        await db.commit()
        await db.refresh(dna)
        return dna
