from fastapi import APIRouter, Depends, Body, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import User, UserRole
from app.authentication.dependencies import get_current_user, require_roles
from app.shipping.models import ShipmentStatus
from app.shipping.schemas import (
    ShipmentOut,
    CreateShipmentRequest,
    TrackingEventOut,
)
from app.shipping.service import ShippingService

router = APIRouter(prefix="/shipping", tags=["Shipping & Logistics"])


@router.post(
    "/shipments",
    response_model=ShipmentOut,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.VENDOR_OWNER, UserRole.VENDOR_MANAGER]))]
)
async def create_shipment(
    req: CreateShipmentRequest,
    db: AsyncSession = Depends(get_db)
):
    return await ShippingService.create_shipment(db, req)


@router.get("/shipments/{sub_order_id}", response_model=ShipmentOut)
async def get_shipment_tracking(
    sub_order_id: str,
    db: AsyncSession = Depends(get_db)
):
    return await ShippingService.get_by_sub_order(db, sub_order_id)


@router.post(
    "/shipments/{shipment_id}/events",
    response_model=TrackingEventOut,
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.VENDOR_OWNER]))]
)
async def add_tracking_event(
    shipment_id: str,
    status_val: ShipmentStatus = Body(..., embed=True),
    location: str = Body(..., embed=True),
    description: str = Body(..., embed=True),
    db: AsyncSession = Depends(get_db)
):
    return await ShippingService.add_tracking_milestone(
        db, shipment_id, status_val, location, description
    )
