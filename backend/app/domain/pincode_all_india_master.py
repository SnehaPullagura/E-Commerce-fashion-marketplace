"""
Pan-India Master Logistics Corridor & Serviceable Hub Network.
Maintains express routes, air freight transit corridors,
and last-mile delivery SLA configurations across Indian states.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel


class LogisticsCorridorSpec(BaseModel):
    corridor_id: str
    origin_hub: str
    destination_pincode: str
    destination_city: str
    destination_state: str
    transit_mode: str  # "AIR_EXPRESS", "SURFACE_STANDARD", "HYPERLOCAL"
    transit_time_hours: int
    weight_limit_kg: float = 20.0
    cold_chain_capable: bool = False
    reverse_pickup_sla_hours: int = 24


METRO_LOGISTICS_HUBS = [
    ("BOM_MUMBAI_HUB", "400001", "Mumbai", "Maharashtra", "HYPERLOCAL", 4),
    ("BOM_MUMBAI_HUB", "400050", "Bandra Mumbai", "Maharashtra", "HYPERLOCAL", 4),
    ("DEL_DELHI_HUB", "110001", "New Delhi", "Delhi", "HYPERLOCAL", 4),
    ("DEL_DELHI_HUB", "110037", "Aerocity Delhi", "Delhi", "HYPERLOCAL", 4),
    ("BLR_BANGALORE_HUB", "560001", "Bangalore", "Karnataka", "HYPERLOCAL", 4),
    ("BLR_BANGALORE_HUB", "560038", "Indiranagar Bangalore", "Karnataka", "HYPERLOCAL", 4),
    ("HYD_HYDERABAD_HUB", "500001", "Hyderabad", "Telangana", "AIR_EXPRESS", 24),
    ("MAA_CHENNAI_HUB", "600001", "Chennai", "Tamil Nadu", "AIR_EXPRESS", 24),
    ("CCU_KOLKATA_HUB", "700001", "Kolkata", "West Bengal", "AIR_EXPRESS", 24),
    ("PNQ_PUNE_HUB", "411001", "Pune", "Maharashtra", "SURFACE_STANDARD", 12),
    ("AMD_AHMEDABAD_HUB", "380001", "Ahmedabad", "Gujarat", "AIR_EXPRESS", 24),
    ("JAI_JAIPUR_HUB", "302001", "Jaipur", "Rajasthan", "SURFACE_STANDARD", 24),
]

def _build_logistics_corridor_master() -> Dict[str, LogisticsCorridorSpec]:
    master: Dict[str, LogisticsCorridorSpec] = {}
    for idx, (hub, pin, city, state, mode, sla) in enumerate(METRO_LOGISTICS_HUBS, 1):
        corr_id = f"CORR_{hub[:3]}_{pin}_{idx:04d}"
        master[corr_id] = LogisticsCorridorSpec(
            corridor_id=corr_id,
            origin_hub=hub,
            destination_pincode=pin,
            destination_city=city,
            destination_state=state,
            transit_mode=mode,
            transit_time_hours=sla,
            weight_limit_kg=25.0,
            cold_chain_capable=(mode == "AIR_EXPRESS"),
            reverse_pickup_sla_hours=24
        )
    return master

LOGISTICS_CORRIDOR_MASTER: Dict[str, LogisticsCorridorSpec] = _build_logistics_corridor_master()
