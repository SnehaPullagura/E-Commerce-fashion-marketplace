from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import User
from app.users.schemas import (
    UserOut,
    UserUpdate,
    UserProfileOut,
    UserProfileUpdate,
    UserAddressOut,
    UserAddressCreate,
    UserAddressUpdate,
    UserSizeProfileOut,
    UserSizeProfileUpdate,
    FashionDNAOut,
    FashionDNAUpdate,
)
from app.users.service import UserService
from app.authentication.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["Users & Fashion Profile"])


@router.get("/me", response_model=UserOut)
async def get_my_profile(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await UserService.get_by_id(db, current_user.id)


@router.put("/me", response_model=UserOut)
async def update_my_profile(
    user_in: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    await UserService.update_user(db, current_user.id, user_in)
    return await UserService.get_by_id(db, current_user.id)


@router.put("/me/profile", response_model=UserProfileOut)
async def update_profile_settings(
    profile_in: UserProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await UserService.update_profile(db, current_user.id, profile_in)


@router.get("/me/addresses", response_model=List[UserAddressOut])
async def get_my_addresses(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await UserService.get_addresses(db, current_user.id)


@router.post("/me/addresses", response_model=UserAddressOut, status_code=status.HTTP_201_CREATED)
async def add_address(
    address_in: UserAddressCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await UserService.create_address(db, current_user.id, address_in)


@router.put("/me/addresses/{address_id}", response_model=UserAddressOut)
async def update_address(
    address_id: str,
    address_in: UserAddressUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await UserService.update_address(db, current_user.id, address_id, address_in)


@router.delete("/me/addresses/{address_id}")
async def delete_address(
    address_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    await UserService.delete_address(db, current_user.id, address_id)
    return {"success": True, "message": "Address deleted successfully"}


@router.get("/me/size-profile", response_model=UserSizeProfileOut)
async def get_my_size_profile(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    user = await UserService.get_by_id(db, current_user.id)
    return user.size_profile


@router.put("/me/size-profile", response_model=UserSizeProfileOut)
async def update_my_size_profile(
    size_in: UserSizeProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await UserService.update_size_profile(db, current_user.id, size_in)


@router.get("/me/fashion-dna", response_model=FashionDNAOut)
async def get_my_fashion_dna(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    user = await UserService.get_by_id(db, current_user.id)
    return user.style_preference


@router.put("/me/fashion-dna", response_model=FashionDNAOut)
async def update_my_fashion_dna(
    dna_in: FashionDNAUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await UserService.update_fashion_dna(db, current_user.id, dna_in)
