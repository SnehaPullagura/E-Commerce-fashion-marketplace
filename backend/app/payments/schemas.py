from typing import Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.payments.models import PaymentGatewayType, PaymentTxStatus


class InitiatePaymentRequest(BaseModel):
    order_id: str
    gateway: PaymentGatewayType = PaymentGatewayType.MOCK
    payment_method: str = "UPI"


class PaymentInitiateResponse(BaseModel):
    transaction_reference: str
    order_id: str
    amount: float
    currency: str
    gateway: PaymentGatewayType
    gateway_order_id: Optional[str] = None
    razorpay_key_id: Optional[str] = None


class VerifyPaymentWebhook(BaseModel):
    transaction_reference: str
    gateway_payment_id: Optional[str] = None
    gateway_signature: Optional[str] = None
    status: PaymentTxStatus = PaymentTxStatus.SUCCESS
    gateway_payload: Dict[str, Any] = {}


class PaymentTransactionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    order_id: str
    transaction_reference: str
    payment_gateway: PaymentGatewayType
    amount: float
    currency: str
    status: PaymentTxStatus
    payment_method: str
    created_at: datetime


class RefundRequest(BaseModel):
    order_id: str
    sub_order_id: Optional[str] = None
    amount: float
    reason: str
