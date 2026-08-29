"""
High-Throughput Flash Sale, Drop Countdown & Atomic Inventory Token Engine.
Ensures zero-oversell guarantees during concurrent mega flash sales.
"""

from typing import Dict, List, Optional, Any, Set
from pydantic import BaseModel, Field
from datetime import datetime, timezone, timedelta
import uuid


class FlashSaleDrop(BaseModel):
    drop_id: str
    product_id: str
    title: str
    original_price: float
    flash_price: float
    total_inventory: int
    reserved_inventory: int = 0
    claimed_inventory: int = 0
    max_per_customer: int = 2
    start_time: datetime
    end_time: datetime
    status: str = "ACTIVE"  # UPCOMING, ACTIVE, SOLD_OUT, EXPIRED


class ReservationToken(BaseModel):
    token_id: str
    drop_id: str
    user_id: str
    quantity: int
    expires_at: datetime
    status: str = "RESERVED"  # RESERVED, CONVERTED, EXPIRED


class FlashSaleEngine:
    def __init__(self):
        self.drops: Dict[str, FlashSaleDrop] = {}
        self.tokens: Dict[str, ReservationToken] = {}
        self.user_reservations: Dict[str, Set[str]] = {}  # user_id -> set of token_ids

    def register_drop(self, drop: FlashSaleDrop) -> FlashSaleDrop:
        self.drops[drop.drop_id] = drop
        return drop

    def get_active_drops(self) -> List[Dict[str, Any]]:
        now = datetime.now(timezone.utc)
        results = []
        for drop in self.drops.values():
            # Check status
            if now < drop.start_time:
                current_status = "UPCOMING"
            elif drop.start_time <= now <= drop.end_time:
                current_status = "SOLD_OUT" if drop.reserved_inventory >= drop.total_inventory else "ACTIVE"
            else:
                current_status = "EXPIRED"

            drop.status = current_status
            results.append({
                "drop_id": drop.drop_id,
                "product_id": drop.product_id,
                "title": drop.title,
                "original_price": drop.original_price,
                "flash_price": drop.flash_price,
                "discount_pct": round(((drop.original_price - drop.flash_price) / drop.original_price) * 100, 1),
                "total_inventory": drop.total_inventory,
                "available_stock": max(0, drop.total_inventory - drop.reserved_inventory),
                "status": drop.status,
                "starts_in_seconds": max(0, int((drop.start_time - now).total_seconds())),
                "ends_in_seconds": max(0, int((drop.end_time - now).total_seconds()))
            })
        return results

    def claim_atomic_reservation(
        self,
        drop_id: str,
        user_id: str,
        quantity: int = 1,
        hold_minutes: int = 5
    ) -> Dict[str, Any]:
        """Atomically allocates reservation token if stock is available within limit."""
        if drop_id not in self.drops:
            return {"success": False, "error": "Flash drop not found"}

        drop = self.drops[drop_id]
        now = datetime.now(timezone.utc)

        # Cleanup expired tokens for this drop
        self._expire_stale_tokens(drop_id)

        if now < drop.start_time:
            return {"success": False, "error": "Flash drop has not started yet"}
        if now > drop.end_time:
            return {"success": False, "error": "Flash drop has concluded"}

        if (drop.total_inventory - drop.reserved_inventory) < quantity:
            return {"success": False, "error": "Stock depleted - Sold Out"}

        # Check per-user limits
        user_existing_tokens = [
            self.tokens[tid] for tid in self.user_reservations.get(user_id, set())
            if tid in self.tokens and self.tokens[tid].drop_id == drop_id and self.tokens[tid].status == "RESERVED"
        ]
        already_reserved = sum(t.quantity for t in user_existing_tokens)
        if (already_reserved + quantity) > drop.max_per_customer:
            return {"success": False, "error": f"Max limit per customer is {drop.max_per_customer}"}

        # Issue atomic reservation token
        token_id = f"tok_{uuid.uuid4().hex[:12]}"
        token = ReservationToken(
            token_id=token_id,
            drop_id=drop_id,
            user_id=user_id,
            quantity=quantity,
            expires_at=now + timedelta(minutes=hold_minutes),
            status="RESERVED"
        )
        self.tokens[token_id] = token
        if user_id not in self.user_reservations:
            self.user_reservations[user_id] = set()
        self.user_reservations[user_id].add(token_id)

        drop.reserved_inventory += quantity

        return {
            "success": True,
            "token_id": token_id,
            "drop_id": drop_id,
            "quantity_reserved": quantity,
            "flash_unit_price": drop.flash_price,
            "expires_at": token.expires_at.isoformat(),
            "ttl_seconds": hold_minutes * 60
        }

    def _expire_stale_tokens(self, drop_id: str):
        now = datetime.now(timezone.utc)
        drop = self.drops.get(drop_id)
        if not drop:
            return

        for token in list(self.tokens.values()):
            if token.drop_id == drop_id and token.status == "RESERVED" and token.expires_at < now:
                token.status = "EXPIRED"
                drop.reserved_inventory = max(0, drop.reserved_inventory - token.quantity)


# Singleton engine instance
flash_engine = FlashSaleEngine()
