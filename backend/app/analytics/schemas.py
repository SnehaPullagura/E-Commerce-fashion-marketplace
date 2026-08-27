from typing import List, Dict, Any, Optional
from datetime import date
from pydantic import BaseModel, ConfigDict


class MetricPoint(BaseModel):
    date: str
    value: float


class MarketplaceOverviewAnalytics(BaseModel):
    period_days: int
    total_gmv: float
    total_revenue: float
    total_orders: int
    average_order_value: float
    conversion_rate: float
    gmv_trend: List[Dict[str, Any]]
    orders_trend: List[Dict[str, Any]]
    top_categories: List[Dict[str, Any]]
    top_vendors: List[Dict[str, Any]]


class VendorAnalyticsSummary(BaseModel):
    vendor_id: str
    total_sales: float
    net_earnings: float
    commission_paid: float
    total_orders: int
    fulfillment_rate: float
    average_order_value: float
    sales_trend: List[Dict[str, Any]]
    top_products: List[Dict[str, Any]]


class FashionTrendRadar(BaseModel):
    top_occasions: List[Dict[str, Any]]
    top_fabrics: List[Dict[str, Any]]
    top_color_palettes: List[Dict[str, Any]]
    top_fit_types: List[Dict[str, Any]]


class ConversionFunnelStep(BaseModel):
    step: str
    count: int
    dropoff_rate: float


class ConversionFunnelResponse(BaseModel):
    steps: List[ConversionFunnelStep]
    overall_conversion_rate: float
