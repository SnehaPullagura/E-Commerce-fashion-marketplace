"""
Omni-Channel Fulfillment & Automated Vendor Settlements REST Router.
"""

from fastapi import APIRouter, HTTPException, Query, status
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime, timezone

from app.shipping.omnichannel import (
    OmniChannelLogisticsEngine, RoutingOptimizationRequest, DarkStoreLocation
)
from app.vendors.automated_payouts import (
    escrow_engine, VendorPayoutAccount, OrderSettlementItem
)

router = APIRouter(prefix="/logistics", tags=["Omni-Channel Logistics & Vendor Payouts"])


class BatchSettlementRequest(BaseModel):
    account: VendorPayoutAccount
    orders: List[OrderSettlementItem]


@router.post("/route-optimize")
def optimize_order_routing(payload: RoutingOptimizationRequest):
    """Calculates hyper-local routing, dark store proximity, and courier package splits."""
    return OmniChannelLogisticsEngine.optimize_order_routing(payload)


@router.get("/dark-stores/all")
def list_dark_store_hubs():
    """Lists all active regional dark store fulfillment hubs."""
    return {"dark_stores": OmniChannelLogisticsEngine.DARK_STORES}


@router.post("/payouts/batch-settle")
def settle_vendor_orders(payload: BatchSettlementRequest):
    """Executes automated escrow distribution, commission deduction, and reserve hold allocation."""
    return escrow_engine.process_order_settlement(payload.account, payload.orders)


@router.get("/payouts/ledger/{vendor_id}")
def get_vendor_financial_ledger(vendor_id: str):
    """Inspects live financial ledger, escrow pending, and rolling reserve balances for a vendor."""
    ledger = escrow_engine.get_or_create_ledger(vendor_id)
    return {"ledger": ledger}
