from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload

from app.core.exceptions import NotFoundException, ConflictException
from app.categories.models import Category, CategoryAttribute
from app.categories.schemas import CategoryCreate, CategoryUpdate, CategoryAttributeCreate


class CategoryService:
    @staticmethod
    async def get_all(db: AsyncSession, only_active: bool = True) -> List[Category]:
        stmt = (
            select(Category)
            .options(selectinload(Category.attributes), selectinload(Category.subcategories))
            .where(Category.is_deleted == False)
        )
        if only_active:
            stmt = stmt.where(Category.is_active == True)
        stmt = stmt.order_by(Category.display_order.asc(), Category.name.asc())
        res = await db.execute(stmt)
        return list(res.scalars().all())

    @staticmethod
    async def get_tree(db: AsyncSession) -> List[Category]:
        stmt = (
            select(Category)
            .options(
                selectinload(Category.attributes),
                selectinload(Category.subcategories).selectinload(Category.subcategories)
            )
            .where(Category.parent_id == None, Category.is_deleted == False, Category.is_active == True)
            .order_by(Category.display_order.asc())
        )
        res = await db.execute(stmt)
        return list(res.scalars().all())

    @staticmethod
    async def get_by_id(db: AsyncSession, category_id: str) -> Category:
        stmt = (
            select(Category)
            .options(selectinload(Category.attributes), selectinload(Category.subcategories))
            .where(Category.id == category_id, Category.is_deleted == False)
        )
        res = await db.execute(stmt)
        category = res.scalar_one_or_none()
        if not category:
            raise NotFoundException(f"Category {category_id} not found")
        return category

    @staticmethod
    async def get_by_slug(db: AsyncSession, slug: str) -> Category:
        stmt = (
            select(Category)
            .options(selectinload(Category.attributes), selectinload(Category.subcategories))
            .where(Category.slug == slug.lower(), Category.is_deleted == False)
        )
        res = await db.execute(stmt)
        category = res.scalar_one_or_none()
        if not category:
            raise NotFoundException(f"Category with slug '{slug}' not found")
        return category

    @staticmethod
    async def create(db: AsyncSession, cat_in: CategoryCreate) -> Category:
        stmt = select(Category).where(Category.slug == cat_in.slug.lower())
        res = await db.execute(stmt)
        if res.scalar_one_or_none():
            raise ConflictException(f"Category with slug '{cat_in.slug}' already exists")

        level = 0
        if cat_in.parent_id:
            parent = await CategoryService.get_by_id(db, cat_in.parent_id)
            level = parent.level + 1

        cat_dict = cat_in.model_dump(exclude={"attributes", "level"})
        category = Category(**cat_dict, level=level)
        db.add(category)
        await db.flush()

        if cat_in.attributes:
            for attr in cat_in.attributes:
                category_attr = CategoryAttribute(category_id=category.id, **attr.model_dump())
                db.add(category_attr)

        await db.commit()
        return await CategoryService.get_by_id(db, category.id)

    @staticmethod
    async def update(db: AsyncSession, category_id: str, cat_in: CategoryUpdate) -> Category:
        category = await CategoryService.get_by_id(db, category_id)
        update_data = cat_in.model_dump(exclude_unset=True)
        for key, val in update_data.items():
            setattr(category, key, val)
        await db.commit()
        return await CategoryService.get_by_id(db, category.id)

    @staticmethod
    async def add_attribute(db: AsyncSession, category_id: str, attr_in: CategoryAttributeCreate) -> CategoryAttribute:
        await CategoryService.get_by_id(db, category_id)
        attr = CategoryAttribute(category_id=category_id, **attr_in.model_dump())
        db.add(attr)
        await db.commit()
        await db.refresh(attr)
        return attr
