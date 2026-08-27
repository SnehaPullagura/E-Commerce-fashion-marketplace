from typing import List, Optional
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import User, UserRole
from app.authentication.dependencies import get_current_user, require_roles
from app.orders.schemas import (
    OrderOut,
    SubOrderOut,
    CheckoutRequest,
    UpdateOrderStatusRequest,
)
from app.orders.service import OrderService

router = APIRouter(prefix="/orders", tags=["Multi-Vendor Orders"])


@router.post("/checkout", response_model=OrderOut, status_code=status.HTTP_201_CREATED)
async def checkout_cart(
    req: CheckoutRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await OrderService.create_order_from_cart(db, current_user, req)


@router.get("", response_model=List[OrderOut])
async def list_my_orders(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await OrderService.list_user_orders(db, current_user.id)


@router.get("/{order_id}", response_model=OrderOut)
async def get_order_details(
    order_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    user_id = None if current_user.role in (UserRole.SUPER_ADMIN, UserRole.ADMIN) else current_user.id
    return await OrderService.get_by_id(db, order_id, user_id=user_id)


@router.get("/vendor/sub-orders", response_model=List[SubOrderOut])
async def list_vendor_sub_orders(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await OrderService.list_vendor_sub_orders(db, current_user.id)


@router.put("/sub-orders/{sub_order_id}/status", response_model=SubOrderOut)
async def update_sub_order_status(
    sub_order_id: str,
    req: UpdateOrderStatusRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    vendor_id = None if current_user.role in (UserRole.SUPER_ADMIN, UserRole.ADMIN) else current_user.id
    return await OrderService.update_sub_order_status(db, sub_order_id, req, vendor_id=vendor_id)
