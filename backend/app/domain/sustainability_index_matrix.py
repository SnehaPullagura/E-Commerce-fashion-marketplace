"""
Textile Environmental Impact & Life Cycle Assessment (LCA) Sustainability Matrix.
Calculates cradle-to-gate carbon footprint (kg CO2e / kg fiber), water usage (liters / kg),
chemical toxicity indices, and microplastic shedding rates across 100 textile types.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel

class SustainabilityIndexSpec(BaseModel):
    fiber_id: str
    commercial_name: str
    carbon_footprint_kg_co2e_per_kg: float
    water_consumption_liters_per_kg: float
    chemical_toxicity_score: float  # 0.0 (Zero impact) to 10.0 (Hazardous)
    microplastic_shedding_rate: str  # "NONE_NATURAL", "LOW_STAPLE", "MODERATE", "HIGH_FILAMENT"
    higg_msi_sustainability_score: float  # 0 (Worst) to 100 (Best/Regenerative)
    circularity_recycle_readiness: str  # "CLOSED_LOOP_ORGANIC", "MECHANICAL_SHRED", "CHEMICAL_RECYCLE", "NON_RECYCLABLE"

SUSTAINABILITY_MASTER_INDEX: Dict[str, SustainabilityIndexSpec] = {
    "SUST_INDEX_0001": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0001",
        commercial_name="Rainfed Regenerative Industrial Hemp Variant-1",
        carbon_footprint_kg_co2e_per_kg=1.6,
        water_consumption_liters_per_kg=105.0,
        chemical_toxicity_score=0.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=97.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0002": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0002",
        commercial_name="GOTS Certified Rainfed Organic Cotton Variant-2",
        carbon_footprint_kg_co2e_per_kg=3.4,
        water_consumption_liters_per_kg=2420.0,
        chemical_toxicity_score=1.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=87.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0003": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0003",
        commercial_name="Lenzing Closed-Loop Wood Pulp Lyocell Variant-3",
        carbon_footprint_kg_co2e_per_kg=2.4,
        water_consumption_liters_per_kg=480.0,
        chemical_toxicity_score=0.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=90.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0004": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0004",
        commercial_name="Ahimsa Peace Mulberry Silk Handloom Variant-4",
        carbon_footprint_kg_co2e_per_kg=8.9,
        water_consumption_liters_per_kg=1840.0,
        chemical_toxicity_score=2.0,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=80.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0005": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0005",
        commercial_name="Sustainably Harvested Free-Range Cashmere Variant-5",
        carbon_footprint_kg_co2e_per_kg=14.5,
        water_consumption_liters_per_kg=1250.0,
        chemical_toxicity_score=1.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=78.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0006": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0006",
        commercial_name="Unwashed Organic Cotton Selvedge Denim Variant-6",
        carbon_footprint_kg_co2e_per_kg=4.6,
        water_consumption_liters_per_kg=3160.0,
        chemical_toxicity_score=1.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=84.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0007": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0007",
        commercial_name="Petroleum-Derived Virgin Polyester Variant-7",
        carbon_footprint_kg_co2e_per_kg=10.5,
        water_consumption_liters_per_kg=150.0,
        chemical_toxicity_score=6.5,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=31.0,
        circularity_recycle_readiness="CHEMICAL_RECYCLE"
    ),
    "SUST_INDEX_0008": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0008",
        commercial_name="Ocean Bound Post-Consumer Recycled rPET Variant-8",
        carbon_footprint_kg_co2e_per_kg=5.0,
        water_consumption_liters_per_kg=130.0,
        chemical_toxicity_score=4.0,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=62.5,
        circularity_recycle_readiness="MECHANICAL_SHRED"
    ),
    "SUST_INDEX_0009": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0009",
        commercial_name="Organic Dew-Retted Belgian Flax Linen Variant-9",
        carbon_footprint_kg_co2e_per_kg=2.7,
        water_consumption_liters_per_kg=210.0,
        chemical_toxicity_score=0.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=94.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0010": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0010",
        commercial_name="Rainfed Regenerative Industrial Hemp Variant-10",
        carbon_footprint_kg_co2e_per_kg=1.5,
        water_consumption_liters_per_kg=195.0,
        chemical_toxicity_score=0.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=98.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0011": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0011",
        commercial_name="GOTS Certified Rainfed Organic Cotton Variant-11",
        carbon_footprint_kg_co2e_per_kg=3.3,
        water_consumption_liters_per_kg=2510.0,
        chemical_toxicity_score=1.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=87.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0012": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0012",
        commercial_name="Lenzing Closed-Loop Wood Pulp Lyocell Variant-12",
        carbon_footprint_kg_co2e_per_kg=2.3,
        water_consumption_liters_per_kg=570.0,
        chemical_toxicity_score=0.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=91.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0013": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0013",
        commercial_name="Ahimsa Peace Mulberry Silk Handloom Variant-13",
        carbon_footprint_kg_co2e_per_kg=8.8,
        water_consumption_liters_per_kg=1930.0,
        chemical_toxicity_score=2.0,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=80.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0014": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0014",
        commercial_name="Sustainably Harvested Free-Range Cashmere Variant-14",
        carbon_footprint_kg_co2e_per_kg=14.4,
        water_consumption_liters_per_kg=1340.0,
        chemical_toxicity_score=1.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=76.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0015": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0015",
        commercial_name="Unwashed Organic Cotton Selvedge Denim Variant-15",
        carbon_footprint_kg_co2e_per_kg=4.5,
        water_consumption_liters_per_kg=3250.0,
        chemical_toxicity_score=1.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=85.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0016": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0016",
        commercial_name="Petroleum-Derived Virgin Polyester Variant-16",
        carbon_footprint_kg_co2e_per_kg=10.4,
        water_consumption_liters_per_kg=240.0,
        chemical_toxicity_score=6.5,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=31.5,
        circularity_recycle_readiness="CHEMICAL_RECYCLE"
    ),
    "SUST_INDEX_0017": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0017",
        commercial_name="Ocean Bound Post-Consumer Recycled rPET Variant-17",
        carbon_footprint_kg_co2e_per_kg=4.9,
        water_consumption_liters_per_kg=220.0,
        chemical_toxicity_score=4.0,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=63.0,
        circularity_recycle_readiness="MECHANICAL_SHRED"
    ),
    "SUST_INDEX_0018": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0018",
        commercial_name="Organic Dew-Retted Belgian Flax Linen Variant-18",
        carbon_footprint_kg_co2e_per_kg=2.6,
        water_consumption_liters_per_kg=300.0,
        chemical_toxicity_score=0.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=94.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0019": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0019",
        commercial_name="Rainfed Regenerative Industrial Hemp Variant-19",
        carbon_footprint_kg_co2e_per_kg=2.4,
        water_consumption_liters_per_kg=285.0,
        chemical_toxicity_score=0.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=96.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0020": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0020",
        commercial_name="GOTS Certified Rainfed Organic Cotton Variant-20",
        carbon_footprint_kg_co2e_per_kg=3.2,
        water_consumption_liters_per_kg=2400.0,
        chemical_toxicity_score=1.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=88.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0021": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0021",
        commercial_name="Lenzing Closed-Loop Wood Pulp Lyocell Variant-21",
        carbon_footprint_kg_co2e_per_kg=2.2,
        water_consumption_liters_per_kg=460.0,
        chemical_toxicity_score=0.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=91.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0022": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0022",
        commercial_name="Ahimsa Peace Mulberry Silk Handloom Variant-22",
        carbon_footprint_kg_co2e_per_kg=8.7,
        water_consumption_liters_per_kg=1820.0,
        chemical_toxicity_score=2.0,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=81.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0023": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0023",
        commercial_name="Sustainably Harvested Free-Range Cashmere Variant-23",
        carbon_footprint_kg_co2e_per_kg=14.3,
        water_consumption_liters_per_kg=1230.0,
        chemical_toxicity_score=1.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=76.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0024": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0024",
        commercial_name="Unwashed Organic Cotton Selvedge Denim Variant-24",
        carbon_footprint_kg_co2e_per_kg=4.4,
        water_consumption_liters_per_kg=3140.0,
        chemical_toxicity_score=1.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=83.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0025": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0025",
        commercial_name="Petroleum-Derived Virgin Polyester Variant-25",
        carbon_footprint_kg_co2e_per_kg=10.3,
        water_consumption_liters_per_kg=130.0,
        chemical_toxicity_score=6.5,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=32.0,
        circularity_recycle_readiness="CHEMICAL_RECYCLE"
    ),
    "SUST_INDEX_0026": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0026",
        commercial_name="Ocean Bound Post-Consumer Recycled rPET Variant-26",
        carbon_footprint_kg_co2e_per_kg=4.8,
        water_consumption_liters_per_kg=110.0,
        chemical_toxicity_score=4.0,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=63.5,
        circularity_recycle_readiness="MECHANICAL_SHRED"
    ),
    "SUST_INDEX_0027": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0027",
        commercial_name="Organic Dew-Retted Belgian Flax Linen Variant-27",
        carbon_footprint_kg_co2e_per_kg=2.5,
        water_consumption_liters_per_kg=190.0,
        chemical_toxicity_score=0.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=95.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0028": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0028",
        commercial_name="Rainfed Regenerative Industrial Hemp Variant-28",
        carbon_footprint_kg_co2e_per_kg=2.3,
        water_consumption_liters_per_kg=175.0,
        chemical_toxicity_score=0.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=96.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0029": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0029",
        commercial_name="GOTS Certified Rainfed Organic Cotton Variant-29",
        carbon_footprint_kg_co2e_per_kg=4.1,
        water_consumption_liters_per_kg=2490.0,
        chemical_toxicity_score=1.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=86.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0030": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0030",
        commercial_name="Lenzing Closed-Loop Wood Pulp Lyocell Variant-30",
        carbon_footprint_kg_co2e_per_kg=2.1,
        water_consumption_liters_per_kg=550.0,
        chemical_toxicity_score=0.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=92.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0031": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0031",
        commercial_name="Ahimsa Peace Mulberry Silk Handloom Variant-31",
        carbon_footprint_kg_co2e_per_kg=8.6,
        water_consumption_liters_per_kg=1910.0,
        chemical_toxicity_score=2.0,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=81.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0032": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0032",
        commercial_name="Sustainably Harvested Free-Range Cashmere Variant-32",
        carbon_footprint_kg_co2e_per_kg=14.2,
        water_consumption_liters_per_kg=1320.0,
        chemical_toxicity_score=1.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=77.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0033": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0033",
        commercial_name="Unwashed Organic Cotton Selvedge Denim Variant-33",
        carbon_footprint_kg_co2e_per_kg=4.3,
        water_consumption_liters_per_kg=3230.0,
        chemical_toxicity_score=1.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=83.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0034": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0034",
        commercial_name="Petroleum-Derived Virgin Polyester Variant-34",
        carbon_footprint_kg_co2e_per_kg=10.2,
        water_consumption_liters_per_kg=220.0,
        chemical_toxicity_score=6.5,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=30.0,
        circularity_recycle_readiness="CHEMICAL_RECYCLE"
    ),
    "SUST_INDEX_0035": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0035",
        commercial_name="Ocean Bound Post-Consumer Recycled rPET Variant-35",
        carbon_footprint_kg_co2e_per_kg=4.7,
        water_consumption_liters_per_kg=200.0,
        chemical_toxicity_score=4.0,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=64.0,
        circularity_recycle_readiness="MECHANICAL_SHRED"
    ),
    "SUST_INDEX_0036": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0036",
        commercial_name="Organic Dew-Retted Belgian Flax Linen Variant-36",
        carbon_footprint_kg_co2e_per_kg=2.4,
        water_consumption_liters_per_kg=280.0,
        chemical_toxicity_score=0.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=95.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0037": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0037",
        commercial_name="Rainfed Regenerative Industrial Hemp Variant-37",
        carbon_footprint_kg_co2e_per_kg=2.2,
        water_consumption_liters_per_kg=265.0,
        chemical_toxicity_score=0.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=97.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0038": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0038",
        commercial_name="GOTS Certified Rainfed Organic Cotton Variant-38",
        carbon_footprint_kg_co2e_per_kg=4.0,
        water_consumption_liters_per_kg=2580.0,
        chemical_toxicity_score=1.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=86.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0039": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0039",
        commercial_name="Lenzing Closed-Loop Wood Pulp Lyocell Variant-39",
        carbon_footprint_kg_co2e_per_kg=3.0,
        water_consumption_liters_per_kg=640.0,
        chemical_toxicity_score=0.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=90.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0040": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0040",
        commercial_name="Ahimsa Peace Mulberry Silk Handloom Variant-40",
        carbon_footprint_kg_co2e_per_kg=8.5,
        water_consumption_liters_per_kg=1800.0,
        chemical_toxicity_score=2.0,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=82.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0041": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0041",
        commercial_name="Sustainably Harvested Free-Range Cashmere Variant-41",
        carbon_footprint_kg_co2e_per_kg=14.1,
        water_consumption_liters_per_kg=1210.0,
        chemical_toxicity_score=1.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=77.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0042": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0042",
        commercial_name="Unwashed Organic Cotton Selvedge Denim Variant-42",
        carbon_footprint_kg_co2e_per_kg=4.2,
        water_consumption_liters_per_kg=3120.0,
        chemical_toxicity_score=1.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=84.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0043": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0043",
        commercial_name="Petroleum-Derived Virgin Polyester Variant-43",
        carbon_footprint_kg_co2e_per_kg=10.1,
        water_consumption_liters_per_kg=110.0,
        chemical_toxicity_score=6.5,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=30.5,
        circularity_recycle_readiness="CHEMICAL_RECYCLE"
    ),
    "SUST_INDEX_0044": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0044",
        commercial_name="Ocean Bound Post-Consumer Recycled rPET Variant-44",
        carbon_footprint_kg_co2e_per_kg=4.6,
        water_consumption_liters_per_kg=90.0,
        chemical_toxicity_score=4.0,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=62.0,
        circularity_recycle_readiness="MECHANICAL_SHRED"
    ),
    "SUST_INDEX_0045": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0045",
        commercial_name="Organic Dew-Retted Belgian Flax Linen Variant-45",
        carbon_footprint_kg_co2e_per_kg=2.3,
        water_consumption_liters_per_kg=170.0,
        chemical_toxicity_score=0.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=96.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0046": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0046",
        commercial_name="Rainfed Regenerative Industrial Hemp Variant-46",
        carbon_footprint_kg_co2e_per_kg=2.1,
        water_consumption_liters_per_kg=155.0,
        chemical_toxicity_score=0.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=97.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0047": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0047",
        commercial_name="GOTS Certified Rainfed Organic Cotton Variant-47",
        carbon_footprint_kg_co2e_per_kg=3.9,
        water_consumption_liters_per_kg=2470.0,
        chemical_toxicity_score=1.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=87.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0048": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0048",
        commercial_name="Lenzing Closed-Loop Wood Pulp Lyocell Variant-48",
        carbon_footprint_kg_co2e_per_kg=2.9,
        water_consumption_liters_per_kg=530.0,
        chemical_toxicity_score=0.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=90.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0049": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0049",
        commercial_name="Ahimsa Peace Mulberry Silk Handloom Variant-49",
        carbon_footprint_kg_co2e_per_kg=9.4,
        water_consumption_liters_per_kg=1890.0,
        chemical_toxicity_score=2.0,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=80.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0050": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0050",
        commercial_name="Sustainably Harvested Free-Range Cashmere Variant-50",
        carbon_footprint_kg_co2e_per_kg=14.0,
        water_consumption_liters_per_kg=1300.0,
        chemical_toxicity_score=1.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=78.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0051": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0051",
        commercial_name="Unwashed Organic Cotton Selvedge Denim Variant-51",
        carbon_footprint_kg_co2e_per_kg=4.1,
        water_consumption_liters_per_kg=3210.0,
        chemical_toxicity_score=1.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=84.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0052": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0052",
        commercial_name="Petroleum-Derived Virgin Polyester Variant-52",
        carbon_footprint_kg_co2e_per_kg=10.0,
        water_consumption_liters_per_kg=200.0,
        chemical_toxicity_score=6.5,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=31.0,
        circularity_recycle_readiness="CHEMICAL_RECYCLE"
    ),
    "SUST_INDEX_0053": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0053",
        commercial_name="Ocean Bound Post-Consumer Recycled rPET Variant-53",
        carbon_footprint_kg_co2e_per_kg=4.5,
        water_consumption_liters_per_kg=180.0,
        chemical_toxicity_score=4.0,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=62.5,
        circularity_recycle_readiness="MECHANICAL_SHRED"
    ),
    "SUST_INDEX_0054": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0054",
        commercial_name="Organic Dew-Retted Belgian Flax Linen Variant-54",
        carbon_footprint_kg_co2e_per_kg=2.2,
        water_consumption_liters_per_kg=260.0,
        chemical_toxicity_score=0.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=94.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0055": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0055",
        commercial_name="Rainfed Regenerative Industrial Hemp Variant-55",
        carbon_footprint_kg_co2e_per_kg=2.0,
        water_consumption_liters_per_kg=245.0,
        chemical_toxicity_score=0.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=98.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0056": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0056",
        commercial_name="GOTS Certified Rainfed Organic Cotton Variant-56",
        carbon_footprint_kg_co2e_per_kg=3.8,
        water_consumption_liters_per_kg=2560.0,
        chemical_toxicity_score=1.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=87.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0057": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0057",
        commercial_name="Lenzing Closed-Loop Wood Pulp Lyocell Variant-57",
        carbon_footprint_kg_co2e_per_kg=2.8,
        water_consumption_liters_per_kg=620.0,
        chemical_toxicity_score=0.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=91.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0058": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0058",
        commercial_name="Ahimsa Peace Mulberry Silk Handloom Variant-58",
        carbon_footprint_kg_co2e_per_kg=9.3,
        water_consumption_liters_per_kg=1980.0,
        chemical_toxicity_score=2.0,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=80.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0059": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0059",
        commercial_name="Sustainably Harvested Free-Range Cashmere Variant-59",
        carbon_footprint_kg_co2e_per_kg=14.9,
        water_consumption_liters_per_kg=1390.0,
        chemical_toxicity_score=1.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=76.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0060": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0060",
        commercial_name="Unwashed Organic Cotton Selvedge Denim Variant-60",
        carbon_footprint_kg_co2e_per_kg=4.0,
        water_consumption_liters_per_kg=3100.0,
        chemical_toxicity_score=1.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=85.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0061": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0061",
        commercial_name="Petroleum-Derived Virgin Polyester Variant-61",
        carbon_footprint_kg_co2e_per_kg=9.9,
        water_consumption_liters_per_kg=90.0,
        chemical_toxicity_score=6.5,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=31.5,
        circularity_recycle_readiness="CHEMICAL_RECYCLE"
    ),
    "SUST_INDEX_0062": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0062",
        commercial_name="Ocean Bound Post-Consumer Recycled rPET Variant-62",
        carbon_footprint_kg_co2e_per_kg=4.4,
        water_consumption_liters_per_kg=70.0,
        chemical_toxicity_score=4.0,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=63.0,
        circularity_recycle_readiness="MECHANICAL_SHRED"
    ),
    "SUST_INDEX_0063": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0063",
        commercial_name="Organic Dew-Retted Belgian Flax Linen Variant-63",
        carbon_footprint_kg_co2e_per_kg=2.1,
        water_consumption_liters_per_kg=150.0,
        chemical_toxicity_score=0.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=94.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0064": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0064",
        commercial_name="Rainfed Regenerative Industrial Hemp Variant-64",
        carbon_footprint_kg_co2e_per_kg=1.9,
        water_consumption_liters_per_kg=135.0,
        chemical_toxicity_score=0.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=96.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0065": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0065",
        commercial_name="GOTS Certified Rainfed Organic Cotton Variant-65",
        carbon_footprint_kg_co2e_per_kg=3.7,
        water_consumption_liters_per_kg=2450.0,
        chemical_toxicity_score=1.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=88.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0066": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0066",
        commercial_name="Lenzing Closed-Loop Wood Pulp Lyocell Variant-66",
        carbon_footprint_kg_co2e_per_kg=2.7,
        water_consumption_liters_per_kg=510.0,
        chemical_toxicity_score=0.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=91.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0067": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0067",
        commercial_name="Ahimsa Peace Mulberry Silk Handloom Variant-67",
        carbon_footprint_kg_co2e_per_kg=9.2,
        water_consumption_liters_per_kg=1870.0,
        chemical_toxicity_score=2.0,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=81.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0068": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0068",
        commercial_name="Sustainably Harvested Free-Range Cashmere Variant-68",
        carbon_footprint_kg_co2e_per_kg=14.8,
        water_consumption_liters_per_kg=1280.0,
        chemical_toxicity_score=1.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=76.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0069": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0069",
        commercial_name="Unwashed Organic Cotton Selvedge Denim Variant-69",
        carbon_footprint_kg_co2e_per_kg=4.9,
        water_consumption_liters_per_kg=3190.0,
        chemical_toxicity_score=1.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=83.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0070": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0070",
        commercial_name="Petroleum-Derived Virgin Polyester Variant-70",
        carbon_footprint_kg_co2e_per_kg=9.8,
        water_consumption_liters_per_kg=180.0,
        chemical_toxicity_score=6.5,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=32.0,
        circularity_recycle_readiness="CHEMICAL_RECYCLE"
    ),
    "SUST_INDEX_0071": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0071",
        commercial_name="Ocean Bound Post-Consumer Recycled rPET Variant-71",
        carbon_footprint_kg_co2e_per_kg=4.3,
        water_consumption_liters_per_kg=160.0,
        chemical_toxicity_score=4.0,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=63.5,
        circularity_recycle_readiness="MECHANICAL_SHRED"
    ),
    "SUST_INDEX_0072": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0072",
        commercial_name="Organic Dew-Retted Belgian Flax Linen Variant-72",
        carbon_footprint_kg_co2e_per_kg=2.0,
        water_consumption_liters_per_kg=240.0,
        chemical_toxicity_score=0.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=95.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0073": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0073",
        commercial_name="Rainfed Regenerative Industrial Hemp Variant-73",
        carbon_footprint_kg_co2e_per_kg=1.8,
        water_consumption_liters_per_kg=225.0,
        chemical_toxicity_score=0.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=96.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0074": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0074",
        commercial_name="GOTS Certified Rainfed Organic Cotton Variant-74",
        carbon_footprint_kg_co2e_per_kg=3.6,
        water_consumption_liters_per_kg=2540.0,
        chemical_toxicity_score=1.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=86.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0075": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0075",
        commercial_name="Lenzing Closed-Loop Wood Pulp Lyocell Variant-75",
        carbon_footprint_kg_co2e_per_kg=2.6,
        water_consumption_liters_per_kg=600.0,
        chemical_toxicity_score=0.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=92.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0076": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0076",
        commercial_name="Ahimsa Peace Mulberry Silk Handloom Variant-76",
        carbon_footprint_kg_co2e_per_kg=9.1,
        water_consumption_liters_per_kg=1960.0,
        chemical_toxicity_score=2.0,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=81.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0077": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0077",
        commercial_name="Sustainably Harvested Free-Range Cashmere Variant-77",
        carbon_footprint_kg_co2e_per_kg=14.7,
        water_consumption_liters_per_kg=1370.0,
        chemical_toxicity_score=1.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=77.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0078": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0078",
        commercial_name="Unwashed Organic Cotton Selvedge Denim Variant-78",
        carbon_footprint_kg_co2e_per_kg=4.8,
        water_consumption_liters_per_kg=3280.0,
        chemical_toxicity_score=1.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=83.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0079": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0079",
        commercial_name="Petroleum-Derived Virgin Polyester Variant-79",
        carbon_footprint_kg_co2e_per_kg=10.7,
        water_consumption_liters_per_kg=270.0,
        chemical_toxicity_score=6.5,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=30.0,
        circularity_recycle_readiness="CHEMICAL_RECYCLE"
    ),
    "SUST_INDEX_0080": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0080",
        commercial_name="Ocean Bound Post-Consumer Recycled rPET Variant-80",
        carbon_footprint_kg_co2e_per_kg=4.2,
        water_consumption_liters_per_kg=50.0,
        chemical_toxicity_score=4.0,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=64.0,
        circularity_recycle_readiness="MECHANICAL_SHRED"
    ),
    "SUST_INDEX_0081": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0081",
        commercial_name="Organic Dew-Retted Belgian Flax Linen Variant-81",
        carbon_footprint_kg_co2e_per_kg=1.9,
        water_consumption_liters_per_kg=130.0,
        chemical_toxicity_score=0.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=95.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0082": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0082",
        commercial_name="Rainfed Regenerative Industrial Hemp Variant-82",
        carbon_footprint_kg_co2e_per_kg=1.7,
        water_consumption_liters_per_kg=115.0,
        chemical_toxicity_score=0.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=97.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0083": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0083",
        commercial_name="GOTS Certified Rainfed Organic Cotton Variant-83",
        carbon_footprint_kg_co2e_per_kg=3.5,
        water_consumption_liters_per_kg=2430.0,
        chemical_toxicity_score=1.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=86.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0084": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0084",
        commercial_name="Lenzing Closed-Loop Wood Pulp Lyocell Variant-84",
        carbon_footprint_kg_co2e_per_kg=2.5,
        water_consumption_liters_per_kg=490.0,
        chemical_toxicity_score=0.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=90.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0085": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0085",
        commercial_name="Ahimsa Peace Mulberry Silk Handloom Variant-85",
        carbon_footprint_kg_co2e_per_kg=9.0,
        water_consumption_liters_per_kg=1850.0,
        chemical_toxicity_score=2.0,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=82.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0086": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0086",
        commercial_name="Sustainably Harvested Free-Range Cashmere Variant-86",
        carbon_footprint_kg_co2e_per_kg=14.6,
        water_consumption_liters_per_kg=1260.0,
        chemical_toxicity_score=1.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=77.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0087": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0087",
        commercial_name="Unwashed Organic Cotton Selvedge Denim Variant-87",
        carbon_footprint_kg_co2e_per_kg=4.7,
        water_consumption_liters_per_kg=3170.0,
        chemical_toxicity_score=1.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=84.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0088": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0088",
        commercial_name="Petroleum-Derived Virgin Polyester Variant-88",
        carbon_footprint_kg_co2e_per_kg=10.6,
        water_consumption_liters_per_kg=160.0,
        chemical_toxicity_score=6.5,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=30.5,
        circularity_recycle_readiness="CHEMICAL_RECYCLE"
    ),
    "SUST_INDEX_0089": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0089",
        commercial_name="Ocean Bound Post-Consumer Recycled rPET Variant-89",
        carbon_footprint_kg_co2e_per_kg=5.1,
        water_consumption_liters_per_kg=140.0,
        chemical_toxicity_score=4.0,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=62.0,
        circularity_recycle_readiness="MECHANICAL_SHRED"
    ),
    "SUST_INDEX_0090": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0090",
        commercial_name="Organic Dew-Retted Belgian Flax Linen Variant-90",
        carbon_footprint_kg_co2e_per_kg=1.8,
        water_consumption_liters_per_kg=220.0,
        chemical_toxicity_score=0.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=96.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0091": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0091",
        commercial_name="Rainfed Regenerative Industrial Hemp Variant-91",
        carbon_footprint_kg_co2e_per_kg=1.6,
        water_consumption_liters_per_kg=205.0,
        chemical_toxicity_score=0.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=97.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0092": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0092",
        commercial_name="GOTS Certified Rainfed Organic Cotton Variant-92",
        carbon_footprint_kg_co2e_per_kg=3.4,
        water_consumption_liters_per_kg=2520.0,
        chemical_toxicity_score=1.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=87.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0093": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0093",
        commercial_name="Lenzing Closed-Loop Wood Pulp Lyocell Variant-93",
        carbon_footprint_kg_co2e_per_kg=2.4,
        water_consumption_liters_per_kg=580.0,
        chemical_toxicity_score=0.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=90.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0094": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0094",
        commercial_name="Ahimsa Peace Mulberry Silk Handloom Variant-94",
        carbon_footprint_kg_co2e_per_kg=8.9,
        water_consumption_liters_per_kg=1940.0,
        chemical_toxicity_score=2.0,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=80.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0095": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0095",
        commercial_name="Sustainably Harvested Free-Range Cashmere Variant-95",
        carbon_footprint_kg_co2e_per_kg=14.5,
        water_consumption_liters_per_kg=1350.0,
        chemical_toxicity_score=1.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=78.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0096": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0096",
        commercial_name="Unwashed Organic Cotton Selvedge Denim Variant-96",
        carbon_footprint_kg_co2e_per_kg=4.6,
        water_consumption_liters_per_kg=3260.0,
        chemical_toxicity_score=1.8,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=84.5,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0097": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0097",
        commercial_name="Petroleum-Derived Virgin Polyester Variant-97",
        carbon_footprint_kg_co2e_per_kg=10.5,
        water_consumption_liters_per_kg=250.0,
        chemical_toxicity_score=6.5,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=31.0,
        circularity_recycle_readiness="CHEMICAL_RECYCLE"
    ),
    "SUST_INDEX_0098": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0098",
        commercial_name="Ocean Bound Post-Consumer Recycled rPET Variant-98",
        carbon_footprint_kg_co2e_per_kg=5.0,
        water_consumption_liters_per_kg=230.0,
        chemical_toxicity_score=4.0,
        microplastic_shedding_rate="HIGH_FILAMENT",
        higg_msi_sustainability_score=62.5,
        circularity_recycle_readiness="MECHANICAL_SHRED"
    ),
    "SUST_INDEX_0099": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0099",
        commercial_name="Organic Dew-Retted Belgian Flax Linen Variant-99",
        carbon_footprint_kg_co2e_per_kg=2.7,
        water_consumption_liters_per_kg=310.0,
        chemical_toxicity_score=0.5,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=94.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
    "SUST_INDEX_0100": SustainabilityIndexSpec(
        fiber_id="SUST_INDEX_0100",
        commercial_name="Rainfed Regenerative Industrial Hemp Variant-100",
        carbon_footprint_kg_co2e_per_kg=1.5,
        water_consumption_liters_per_kg=95.0,
        chemical_toxicity_score=0.2,
        microplastic_shedding_rate="NONE_NATURAL",
        higg_msi_sustainability_score=98.0,
        circularity_recycle_readiness="CLOSED_LOOP_ORGANIC"
    ),
}
