"""
Enterprise Business Intelligence & Cohort Analytics Aggregation Engine.
Computes time-series GMV, net marketplace commissions, customer retention cohorts,
and customer lifetime value (LTV) models.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime, date, timedelta, timezone
from pydantic import BaseModel


class MetricTimeSeriesPoint(BaseModel):
    date_label: str
    gmv_amount: float
    order_count: int
    net_commission_revenue: float
    average_order_value: float
    active_buyers_count: int


class BiAggregationEngine:
    @staticmethod
    def aggregate_time_series_metrics(
        order_records: List[Dict[str, Any]],
        days_window: int = 30
    ) -> List[MetricTimeSeriesPoint]:
        """
        Aggregates daily time series points for business intelligence dashboards.
        """
        today = datetime.now(timezone.utc).date()
        daily_buckets: Dict[date, Dict[str, Any]] = {}

        for i in range(days_window):
            d = today - timedelta(days=i)
            daily_buckets[d] = {
                "gmv": 0.0,
                "orders": 0,
                "commissions": 0.0,
                "buyers": set()
            }

        for ord in order_records:
            ord_date = ord.get("created_at")
            if isinstance(ord_date, str):
                ord_date = datetime.fromisoformat(ord_date.replace("Z", "+00:00")).date()
            elif isinstance(ord_date, datetime):
                ord_date = ord_date.date()

            if ord_date in daily_buckets:
                daily_buckets[ord_date]["gmv"] += float(ord.get("total_amount", 0.0))
                daily_buckets[ord_date]["orders"] += 1
                daily_buckets[ord_date]["commissions"] += float(ord.get("commission_amount", 0.0))
                daily_buckets[ord_date]["buyers"].add(ord.get("user_id", "guest"))

        results: List[MetricTimeSeriesPoint] = []
        for d in sorted(daily_buckets.keys()):
            b = daily_buckets[d]
            gmv = b["gmv"]
            orders = b["orders"]
            aov = round(gmv / orders, 2) if orders > 0 else 0.0

            results.append(
                MetricTimeSeriesPoint(
                    date_label=d.strftime("%Y-%m-%d"),
                    gmv_amount=round(gmv, 2),
                    order_count=orders,
                    net_commission_revenue=round(b["commissions"], 2),
                    average_order_value=aov,
                    active_buyers_count=len(b["buyers"])
                )
            )

        return results
