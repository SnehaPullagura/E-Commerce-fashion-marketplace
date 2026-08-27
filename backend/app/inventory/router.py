from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.core.exceptions import NotFoundException
from app.users.models import UserRole
from app.authentication.dependencies import require_roles
from app.inventory.models import InventoryItem
from app.inventory.schemas import InventoryItemOut, InventoryStockAdjust
from app.inventory.service import InventoryService

router = APIRouter(prefix="/inventory", tags=["Inventory & Stock Management"])


@router.get(
    "/{variant_id}",
    response_model=InventoryItemOut,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.VENDOR_OWNER, UserRole.VENDOR_MANAGER]))]
)
async def get_variant_inventory(
    variant_id: str,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(InventoryItem).where(InventoryItem.variant_id == variant_id)
    res = await db.execute(stmt)
    item = res.scalar_one_or_none()
    if not item:
        raise NotFoundException("Inventory record not found")
    return item


@router.post(
    "/{variant_id}/adjust",
    response_model=InventoryItemOut,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.VENDOR_OWNER]))]
)
async def adjust_stock(
    variant_id: str,
    adjust_in: InventoryStockAdjust,
    db: AsyncSession = Depends(get_db)
):
    return await InventoryService.adjust_stock(
        db, variant_id, adjust_in.quantity_delta, adjust_in.reason
    )
