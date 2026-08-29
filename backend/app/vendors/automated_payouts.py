"""
Automated Multi-Vendor Escrow Payouts, Rolling Reserve Holds & Commission Settlement Engine.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime, timezone, timedelta
import uuid


class VendorPayoutAccount(BaseModel):
    vendor_id: str
    vendor_name: str
    payout_currency: str = "USD"
    bank_iban_masked: str = "**** **** **** 8821"
    platform_commission_rate: float = 0.12  # 12% standard fashion marketplace take-rate
    rolling_reserve_pct: float = 0.05       # 5% held for dispute/returns protection


class OrderSettlementItem(BaseModel):
    order_id: str
    vendor_id: str
    gross_order_amount: float
    delivered_at: datetime
    return_window_expired: bool = True


class VendorEscrowSettlementEngine:
    def __init__(self):
        self.vendor_ledgers: Dict[str, Dict[str, Any]] = {}

    def get_or_create_ledger(self, vendor_id: str, vendor_name: str = "Atelier") -> Dict[str, Any]:
        if vendor_id not in self.vendor_ledgers:
            self.vendor_ledgers[vendor_id] = {
                "vendor_id": vendor_id,
                "vendor_name": vendor_name,
                "available_balance": 0.0,
                "escrow_pending_balance": 0.0,
                "rolling_reserve_held": 0.0,
                "total_lifetime_payouts": 0.0,
                "total_commission_paid": 0.0,
                "settlement_currency": "USD",
                "payout_history": []
            }
        return self.vendor_ledgers[vendor_id]

    def process_order_settlement(
        self,
        account: VendorPayoutAccount,
        orders: List[OrderSettlementItem]
    ) -> Dict[str, Any]:
        """Calculates net revenue distribution after marketplace commission and rolling reserve."""
        ledger = self.get_or_create_ledger(account.vendor_id, account.vendor_name)

        total_gross = sum(o.gross_order_amount for o in orders)
        total_commission = round(total_gross * account.platform_commission_rate, 2)
        total_reserve = round(total_gross * account.rolling_reserve_pct, 2)
        net_payable = round(total_gross - total_commission - total_reserve, 2)

        # Update ledger
        ledger["available_balance"] += net_payable
        ledger["rolling_reserve_held"] += total_reserve
        ledger["total_commission_paid"] += total_commission

        settlement_id = f"stl_{uuid.uuid4().hex[:10]}"
        record = {
            "settlement_id": settlement_id,
            "processed_at": datetime.now(timezone.utc).isoformat(),
            "orders_settled_count": len(orders),
            "gross_amount": total_gross,
            "marketplace_commission_deducted": total_commission,
            "rolling_reserve_allocated": total_reserve,
            "net_disbursed_to_available": net_payable,
            "status": "SETTLED"
        }
        ledger["payout_history"].append(record)

        return {
            "settlement_id": settlement_id,
            "vendor_id": account.vendor_id,
            "gross_revenue": total_gross,
            "commission_rate_pct": round(account.platform_commission_rate * 100, 1),
            "commission_amount": total_commission,
            "reserve_held_amount": total_reserve,
            "net_payable": net_payable,
            "currency": account.payout_currency,
            "ledger_current_balance": ledger["available_balance"]
        }


# Singleton settlement engine
escrow_engine = VendorEscrowSettlementEngine()
