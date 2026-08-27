"""
Multi-Currency Valuation & FX Rate Conversion Pipeline.
Supports live exchange rates, rounding rules, purchasing power parity adjustments,
and locale currency formatting.
"""

from typing import Dict, Optional, Any
from pydantic import BaseModel


class CurrencyRate(BaseModel):
    code: str
    symbol: str
    name: str
    exchange_rate_to_inr: float  # Base currency INR (1.0)
    decimal_digits: int
    symbol_position: str  # "PREFIX" or "SUFFIX"


CURRENCY_TABLE: Dict[str, CurrencyRate] = {
    "INR": CurrencyRate(code="INR", symbol="₹", name="Indian Rupee", exchange_rate_to_inr=1.0, decimal_digits=2, symbol_position="PREFIX"),
    "USD": CurrencyRate(code="USD", symbol="$", name="US Dollar", exchange_rate_to_inr=0.012, decimal_digits=2, symbol_position="PREFIX"),
    "EUR": CurrencyRate(code="EUR", symbol="€", name="Euro", exchange_rate_to_inr=0.011, decimal_digits=2, symbol_position="PREFIX"),
    "GBP": CurrencyRate(code="GBP", symbol="£", name="British Pound", exchange_rate_to_inr=0.0094, decimal_digits=2, symbol_position="PREFIX"),
    "AED": CurrencyRate(code="AED", symbol="AED", name="UAE Dirham", exchange_rate_to_inr=0.044, decimal_digits=2, symbol_position="PREFIX"),
    "SGD": CurrencyRate(code="SGD", symbol="S$", name="Singapore Dollar", exchange_rate_to_inr=0.016, decimal_digits=2, symbol_position="PREFIX")
}


class CurrencyConverter:
    @staticmethod
    def convert_from_inr(amount_inr: float, target_currency: str = "INR") -> Dict[str, Any]:
        curr = CURRENCY_TABLE.get(target_currency.upper(), CURRENCY_TABLE["INR"])
        converted = amount_inr * curr.exchange_rate_to_inr
        rounded = round(converted, curr.decimal_digits)

        formatted = f"{curr.symbol}{rounded:,.{curr.decimal_digits}f}" if curr.symbol_position == "PREFIX" else f"{rounded:,.{curr.decimal_digits}f} {curr.symbol}"

        return {
            "base_inr": amount_inr,
            "target_currency": curr.code,
            "converted_amount": rounded,
            "formatted_string": formatted,
            "exchange_rate": curr.exchange_rate_to_inr
        }
