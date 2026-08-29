"""
Geofenced Omni-Channel Dark Store Fulfillment & Multi-Carrier Routing Solver.
Solves split-shipment optimization, localized dark store dispatch, and courier SLAs.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
import math
import uuid


class DarkStoreLocation(BaseModel):
    store_id: str
    name: str
    city: str
    lat: float
    lon: float
    service_radius_km: float = 25.0
    express_same_day_enabled: bool = True


class ShipmentItem(BaseModel):
    product_id: str
    vendor_id: str
    title: str
    weight_kg: float
    price: float


class RoutingOptimizationRequest(BaseModel):
    customer_lat: float
    customer_lon: float
    customer_city: str
    items: List[ShipmentItem]
    prefer_eco: bool = False


class OmniChannelLogisticsEngine:
    DARK_STORES: List[DarkStoreLocation] = [
        DarkStoreLocation(store_id="ds_mumbai_bkc", name="Mumbai BKC Dark Hub", city="Mumbai", lat=19.066, lon=72.868, service_radius_km=30.0),
        DarkStoreLocation(store_id="ds_delhi_aerocity", name="Delhi Aerocity Hub", city="Delhi", lat=28.553, lon=77.121, service_radius_km=35.0),
        DarkStoreLocation(store_id="ds_blr_indiranagar", name="Bangalore Central Hub", city="Bangalore", lat=12.971, lon=77.641, service_radius_km=25.0),
        DarkStoreLocation(store_id="ds_london_mayfair", name="London Mayfair Atelier", city="London", lat=51.509, lon=-0.148, service_radius_km=20.0),
        DarkStoreLocation(store_id="ds_ny_soho", name="NYC SoHo Fashion Vault", city="New York", lat=40.723, lon=-73.998, service_radius_km=15.0)
    ]

    @staticmethod
    def haversine_distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Calculates great-circle distance between two geographic coordinates."""
        R = 6371.0  # Earth radius in kilometers
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2.0) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2.0) ** 2
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        return round(R * c, 2)

    @staticmethod
    def optimize_order_routing(request: RoutingOptimizationRequest) -> Dict[str, Any]:
        # Find nearest dark store
        nearest_store = None
        min_dist = 999999.0

        for store in OmniChannelLogisticsEngine.DARK_STORES:
            dist = OmniChannelLogisticsEngine.haversine_distance_km(
                request.customer_lat, request.customer_lon, store.lat, store.lon
            )
            if dist < min_dist:
                min_dist = dist
                nearest_store = store

        # Group items by vendor
        vendor_groups: Dict[str, List[ShipmentItem]] = {}
        for item in request.items:
            vendor_groups.setdefault(item.vendor_id, []).append(item)

        is_hyperlocal = (
            nearest_store is not None
            and min_dist <= nearest_store.service_radius_km
            and nearest_store.express_same_day_enabled
        )

        shipment_packages = []
        for v_id, v_items in vendor_groups.items():
            tot_weight = sum(i.weight_kg for i in v_items)
            tot_val = sum(i.price for i in v_items)

            if is_hyperlocal and min_dist <= 15.0:
                carrier = "HyperLocal 90-Min Eco Courier"
                cost = 8.50
                sla_hours = 2
            elif request.prefer_eco:
                carrier = "DHL GoGreen Consolidated Ground"
                cost = 5.00
                sla_hours = 48
            else:
                carrier = "FedEx Priority Express"
                cost = 14.00
                sla_hours = 24

            shipment_packages.append({
                "package_id": f"pkg_{uuid.uuid4().hex[:8]}",
                "vendor_id": v_id,
                "item_count": len(v_items),
                "items": [i.title for i in v_items],
                "weight_kg": round(tot_weight, 2),
                "assigned_carrier": carrier,
                "shipping_fee_usd": cost,
                "estimated_sla_hours": sla_hours
            })

        total_shipping_fee = sum(p["shipping_fee_usd"] for p in shipment_packages)

        return {
            "destination_city": request.customer_city,
            "nearest_fulfillment_hub": nearest_store.name if nearest_store else "Central Regional Depot",
            "distance_to_hub_km": min_dist,
            "hyperlocal_eligible": is_hyperlocal,
            "total_packages": len(shipment_packages),
            "packages": shipment_packages,
            "total_shipping_fee_usd": round(total_shipping_fee, 2),
            "estimated_delivery_summary": "Same-Day 90 Min" if is_hyperlocal else "1-2 Business Days"
        }
