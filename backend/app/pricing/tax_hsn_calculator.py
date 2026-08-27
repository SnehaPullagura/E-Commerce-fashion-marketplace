"""
Apparel Goods and Services Tax (GST) & HSN Code Calculation Engine.
Compliant with Indian Indirect Tax rules for textile & garment classifications.
HSN 6101-6117 (Knitted/Crocheted Garments), HSN 6201-6217 (Woven Garments),
HSN 6401-6405 (Footwear), with dual-tier price slab calculation (< ₹1000 @ 5% vs > ₹1000 @ 12%).
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel
from enum import Enum


class HSNApparelCode(str, Enum):
    KNITTED_MEN_OUTERWEAR = "6101"
    KNITTED_WOMEN_SUITS = "6104"
    KNITTED_SHIRTS = "6105"
    KNITTED_T_SHIRTS = "6109"
    WOVEN_MEN_SUITS_BLAZERS = "6203"
    WOVEN_WOMEN_DRESSES = "6204"
    WOVEN_MEN_SHIRTS = "6205"
    WOVEN_WOMEN_BLOUSES = "6206"
    FOOTWEAR_LEATHER_RUBBER = "6403"
    ACCESSORIES_TIES_SCARVES = "6214"


class TaxBreakdown(BaseModel):
    item_mrp: float
    taxable_base_value: float
    hsn_code: str
    gst_rate_pct: float
    cgst_pct: float
    cgst_amount: float
    sgst_pct: float
    sgst_amount: float
    igst_pct: float
    igst_amount: float
    total_tax_amount: float
    is_interstate: bool


class TaxCalculationEngine:
    @staticmethod
    def calculate_apparel_gst(
        selling_price: float,
        hsn_code: str = "6205",
        vendor_state: str = "Maharashtra",
        customer_state: str = "Karnataka"
    ) -> TaxBreakdown:
        """
        Calculates GST slab:
        - Apparel Selling Price <= ₹1,000: 5% GST (2.5% CGST + 2.5% SGST or 5% IGST)
        - Apparel Selling Price > ₹1,000: 12% GST (6.0% CGST + 6.0% SGST or 12% IGST)
        - Footwear > ₹1,000: 18% GST
        """
        # Determine rate slab
        if hsn_code.startswith("64") and selling_price > 1000.0:
            rate = 18.0
        elif selling_price <= 1000.0:
            rate = 5.0
        else:
            rate = 12.0

        # Back-calculate taxable value from inclusive price
        # Price = Taxable * (1 + Rate/100) -> Taxable = Price / (1 + Rate/100)
        taxable_value = round(selling_price / (1.0 + (rate / 100.0)), 2)
        tax_total = round(selling_price - taxable_value, 2)

        is_interstate = vendor_state.strip().lower() != customer_state.strip().lower()

        if is_interstate:
            cgst_pct = 0.0
            cgst_amt = 0.0
            sgst_pct = 0.0
            sgst_amt = 0.0
            igst_pct = rate
            igst_amt = tax_total
        else:
            cgst_pct = rate / 2.0
            cgst_amt = round(tax_total / 2.0, 2)
            sgst_pct = rate / 2.0
            sgst_amt = round(tax_total - cgst_amt, 2)
            igst_pct = 0.0
            igst_amt = 0.0

        return TaxBreakdown(
            item_mrp=selling_price,
            taxable_base_value=taxable_value,
            hsn_code=hsn_code,
            gst_rate_pct=rate,
            cgst_pct=cgst_pct,
            cgst_amount=cgst_amt,
            sgst_pct=sgst_pct,
            sgst_amount=sgst_amt,
            igst_pct=igst_pct,
            igst_amount=igst_amt,
            total_tax_amount=tax_total,
            is_interstate=is_interstate
        )
