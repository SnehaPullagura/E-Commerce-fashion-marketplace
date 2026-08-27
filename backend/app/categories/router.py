from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import UserRole
from app.authentication.dependencies import require_roles
from app.categories.schemas import (
    CategoryOut,
    CategoryTreeOut,
    CategoryCreate,
    CategoryUpdate,
    CategoryAttributeCreate,
    CategoryAttributeOut,
)
from app.categories.service import CategoryService

router = APIRouter(prefix="/categories", tags=["Fashion Categories"])


@router.get("", response_model=List[CategoryOut])
async def list_categories(db: AsyncSession = Depends(get_db)):
    return await CategoryService.get_all(db)


@router.get("/tree", response_model=List[CategoryTreeOut])
async def get_category_tree(db: AsyncSession = Depends(get_db)):
    return await CategoryService.get_tree(db)


@router.get("/{identifier}", response_model=CategoryOut)
async def get_category(identifier: str, db: AsyncSession = Depends(get_db)):
    # Check if UUID or slug
    if len(identifier) == 36 and "-" in identifier:
        return await CategoryService.get_by_id(db, identifier)
    return await CategoryService.get_by_slug(db, identifier)


@router.post(
    "",
    response_model=CategoryOut,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN]))]
)
async def create_category(cat_in: CategoryCreate, db: AsyncSession = Depends(get_db)):
    return await CategoryService.create(db, cat_in)


@router.put(
    "/{category_id}",
    response_model=CategoryOut,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN]))]
)
async def update_category(category_id: str, cat_in: CategoryUpdate, db: AsyncSession = Depends(get_db)):
    return await CategoryService.update(db, category_id, cat_in)


@router.post(
    "/{category_id}/attributes",
    response_model=CategoryAttributeOut,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN]))]
)
async def add_category_attribute(category_id: str, attr_in: CategoryAttributeCreate, db: AsyncSession = Depends(get_db)):
    return await CategoryService.add_attribute(db, category_id, attr_in)
