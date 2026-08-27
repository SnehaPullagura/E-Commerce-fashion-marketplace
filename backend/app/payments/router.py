from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.users.models import User, UserRole
from app.authentication.dependencies import get_current_user, require_roles
from app.payments.schemas import (
    InitiatePaymentRequest,
    PaymentInitiateResponse,
    VerifyPaymentWebhook,
    RefundRequest,
)
from app.payments.service import PaymentService

router = APIRouter(prefix="/payments", tags=["Payments & Gateway"])


@router.post("/initiate", response_model=PaymentInitiateResponse)
async def initiate_payment(
    req: InitiatePaymentRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await PaymentService.initiate_payment(db, current_user, req)


@router.post("/webhook")
async def payment_webhook(
    req: VerifyPaymentWebhook,
    db: AsyncSession = Depends(get_db)
):
    """Payment Gateway Webhook Endpoint"""
    return await PaymentService.process_payment_callback(db, req)


@router.post(
    "/refund",
    dependencies=[Depends(require_roles([UserRole.SUPER_ADMIN, UserRole.ADMIN]))]
)
async def process_refund(
    req: RefundRequest,
    db: AsyncSession = Depends(get_db)
):
    refund = await PaymentService.process_refund(db, req)
    return {
        "success": True,
        "refund_reference": refund.refund_reference,
        "amount": refund.amount,
        "status": refund.status
    }
