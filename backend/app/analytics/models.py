from datetime import date
from typing import Optional
from sqlalchemy import String, Float, Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base_model import BaseModel


class DailyMarketplaceMetric(BaseModel):
    __tablename__ = "daily_marketplace_metrics"

    metric_date: Mapped[date] = mapped_column(Date, unique=True, index=True, nullable=False)
    gmv: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    revenue_commission: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    total_orders: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    average_order_value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    active_users: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    new_users: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    cart_abandonment_rate: Mapped[float] = mapped_column(Float, default=0.0, nullable=False) # %
    return_rate: Mapped[float] = mapped_column(Float, default=0.0, nullable=False) # %


class VendorDailyMetric(BaseModel):
    __tablename__ = "vendor_daily_metrics"

    vendor_id: Mapped[str] = mapped_column(String(36), ForeignKey("vendor_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    metric_date: Mapped[date] = mapped_column(Date, index=True, nullable=False)
    sales_amount: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    orders_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    net_earnings: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    cancellation_rate: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    return_rate: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)


class ProductEngagementMetric(BaseModel):
    __tablename__ = "product_engagement_metrics"

    product_id: Mapped[str] = mapped_column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    metric_date: Mapped[date] = mapped_column(Date, index=True, nullable=False)
    views_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    cart_adds_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    wishlist_adds_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    orders_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    conversion_rate: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
