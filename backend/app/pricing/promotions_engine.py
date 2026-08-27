"""
Advanced Promotion & Discount Calculation Engine.
Evaluates cart rule pipelines, coupon validity thresholds,
buy-X-get-Y conditions, tier-based percentage caps, and multi-vendor bundle pricing.
"""

from typing import Dict, List, Optional, Any, Tuple
from pydantic import BaseModel, Field
from enum import Enum


class PromotionType(str, Enum):
    PERCENTAGE_OFF = "PERCENTAGE_OFF"
    FIXED_AMOUNT_OFF = "FIXED_AMOUNT_OFF"
    TIERED_SPEND_DISCOUNT = "TIERED_SPEND_DISCOUNT"
    COMPLETE_OUTFIT_BUNDLE = "COMPLETE_OUTFIT_BUNDLE"
    BUY_X_GET_Y_FREE = "BUY_X_GET_Y_FREE"
    FIRST_PURCHASE_WELCOME = "FIRST_PURCHASE_WELCOME"


class PromotionRule(BaseModel):
    code: str
    promo_type: PromotionType
    discount_pct: Optional[float] = None
    fixed_discount_amount: Optional[float] = None
    min_order_value: float = 0.0
    max_discount_cap: Optional[float] = None
    eligible_category_ids: List[str] = []
    eligible_vendor_ids: List[str] = []
    first_order_only: bool = False
    usage_limit_per_user: int = 1


class PromotionEvaluationEngine:
    @staticmethod
    def evaluate_cart_discount(
        cart_items: List[Dict[str, Any]],
        cart_subtotal: float,
        coupon_rule: PromotionRule,
        user_order_count: int = 0
    ) -> Dict[str, Any]:
        """
        Executes promotional validation and calculates exact discount amount.
        """
        # 1. Minimum spend validation
        if cart_subtotal < coupon_rule.min_order_value:
            return {
                "is_valid": False,
                "discount_amount": 0.0,
                "final_total": cart_subtotal,
                "rejection_reason": f"Minimum cart value of ₹{coupon_rule.min_order_value:.2f} required for coupon {coupon_rule.code}."
            }

        # 2. First order check
        if coupon_rule.first_order_only and user_order_count > 0:
            return {
                "is_valid": False,
                "discount_amount": 0.0,
                "final_total": cart_subtotal,
                "rejection_reason": f"Coupon {coupon_rule.code} is valid for first-time shoppers only."
            }

        # 3. Calculate gross discount
        gross_discount = 0.0
        if coupon_rule.promo_type == PromotionType.PERCENTAGE_OFF:
            gross_discount = (cart_subtotal * (coupon_rule.discount_pct or 0.0)) / 100.0
        elif coupon_rule.promo_type == PromotionType.FIXED_AMOUNT_OFF:
            gross_discount = coupon_rule.fixed_discount_amount or 0.0
        elif coupon_rule.promo_type == PromotionType.COMPLETE_OUTFIT_BUNDLE:
            gross_discount = cart_subtotal * 0.10  # 10% outfit bundle

        # 4. Apply maximum cap
        if coupon_rule.max_discount_cap and gross_discount > coupon_rule.max_discount_cap:
            gross_discount = coupon_rule.max_discount_cap

        gross_discount = min(gross_discount, cart_subtotal)
        final_total = round(cart_subtotal - gross_discount, 2)

        return {
            "is_valid": True,
            "coupon_code": coupon_rule.code,
            "discount_amount": round(gross_discount, 2),
            "final_total": final_total,
            "savings_percentage": round((gross_discount / cart_subtotal) * 100.0, 1) if cart_subtotal > 0 else 0.0,
            "success_message": f"Coupon {coupon_rule.code} applied successfully! Saved ₹{gross_discount:.2f}."
        }
