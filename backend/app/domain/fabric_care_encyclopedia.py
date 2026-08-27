"""
Haute Couture & Luxury Fabric Care Encyclopedia.
Provides washing, drying, pressing, chemical tolerance, storage guidelines,
and longevity preservation rules for 100+ fine textile blends.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel

class FabricCareProtocol(BaseModel):
    fabric_code: str
    fabric_name: str
    fiber_composition: str
    wash_type: str  # "DRY_CLEAN_ONLY", "HAND_WASH_COLD", "GENTLE_MACHINE_30", "MACHINE_WARM"
    max_water_temp_c: int
    detergent_recommendation: str
    bleach_safe: bool
    drying_method: str  # "FLAT_IN_SHADE", "LINE_DRY_SHADE", "TUMBLE_LOW", "TUMBLE_MEDIUM"
    ironing_temp_c: int
    steam_safe: bool
    storage_recommendation: str
    longevity_preservation_tips: List[str]

FABRIC_CARE_ENCYCLOPEDIA: Dict[str, FabricCareProtocol] = {
    "MULBERRY_SILK_100": FabricCareProtocol(
        fabric_code="MULBERRY_SILK_100",
        fabric_name="100% Pure Mulberry Silk",
        fiber_composition="100% Silk",
        wash_type="DRY_CLEAN_ONLY",
        max_water_temp_c=20,
        detergent_recommendation="pH-neutral silk liquid wash",
        bleach_safe=False,
        drying_method="FLAT_IN_SHADE",
        ironing_temp_c=110,
        steam_safe=True,
        storage_recommendation="Wrap in acid-free unbleached cotton muslin cloth",
        longevity_preservation_tips=['Never spray perfume or deodorant directly on silk filaments.', 'Do not wring; blot excess water between white cotton towels.', 'Keep away from mothballs; use natural cedarwood blocks.']
    ),
    "KATAN_SILK_ZARI": FabricCareProtocol(
        fabric_code="KATAN_SILK_ZARI",
        fabric_name="Banarasi Katan Silk with Metallic Zari",
        fiber_composition="82% Silk, 18% Metallic Zari",
        wash_type="DRY_CLEAN_ONLY",
        max_water_temp_c=0,
        detergent_recommendation="Specialized heritage dry clean",
        bleach_safe=False,
        drying_method="FLAT_IN_SHADE",
        ironing_temp_c=100,
        steam_safe=False,
        storage_recommendation="Store flat in saree bag with butter paper between folds",
        longevity_preservation_tips=['Refold every 3 months along different fold lines to prevent zari breakage.', 'Never hang on metal hangers as weight can distort weave.', 'Protect from moisture to avoid metallic tarnishing.']
    ),
    "BELGIAN_FLAX_LINEN": FabricCareProtocol(
        fabric_code="BELGIAN_FLAX_LINEN",
        fabric_name="100% Pure Belgian Flax Linen",
        fiber_composition="100% Flax Linen",
        wash_type="MACHINE_WARM",
        max_water_temp_c=40,
        detergent_recommendation="Mild eco-friendly liquid detergent",
        bleach_safe=False,
        drying_method="LINE_DRY_SHADE",
        ironing_temp_c=200,
        steam_safe=True,
        storage_recommendation="Hang on wide wooden hangers in ventilated wardrobe",
        longevity_preservation_tips=['Iron while damp on highest setting with heavy steam.', 'Embrace natural relaxed crumples for casual looks.', 'Softens and improves drape with every subsequent wash.']
    ),
    "GIZA_ELS_COTTON": FabricCareProtocol(
        fabric_code="GIZA_ELS_COTTON",
        fabric_name="Giza 88 Extra-Long Staple Cotton",
        fiber_composition="100% Cotton",
        wash_type="GENTLE_MACHINE_30",
        max_water_temp_c=30,
        detergent_recommendation="Enzyme-free cotton detergent",
        bleach_safe=False,
        drying_method="LINE_DRY_SHADE",
        ironing_temp_c=180,
        steam_safe=True,
        storage_recommendation="Store on contoured cedar hangers",
        longevity_preservation_tips=['Unbutton all collar and cuff buttons prior to washing.', 'Use starch sparingly to preserve natural fiber breathability.', 'Wash inside out to prevent surface fuzzing.']
    ),
    "JAPANESE_RAW_DENIM": FabricCareProtocol(
        fabric_code="JAPANESE_RAW_DENIM",
        fabric_name="Okayama 14.5oz Selvedge Raw Denim",
        fiber_composition="100% Zimbabwe Cotton",
        wash_type="HAND_WASH_COLD",
        max_water_temp_c=20,
        detergent_recommendation="Specialized raw denim wash or Woolite Dark",
        bleach_safe=False,
        drying_method="LINE_DRY_SHADE",
        ironing_temp_c=150,
        steam_safe=True,
        storage_recommendation="Hang by hem clips in dry well-ventilated space",
        longevity_preservation_tips=['Soak inside out in cold water bath without agitation.', 'Hang dry upside down to maintain leg shape.', 'Wear for 6 months before first wash for personal fade lines.']
    ),
    "MONGOLIAN_CASHMERE": FabricCareProtocol(
        fabric_code="MONGOLIAN_CASHMERE",
        fabric_name="Grade-A Mongolian Cashmere 2-Ply",
        fiber_composition="100% Cashmere Wool",
        wash_type="HAND_WASH_COLD",
        max_water_temp_c=25,
        detergent_recommendation="Organic cashmere wool shampoo",
        bleach_safe=False,
        drying_method="FLAT_IN_SHADE",
        ironing_temp_c=110,
        steam_safe=True,
        storage_recommendation="Fold neatly in breathable cloth bin with cedar blocks",
        longevity_preservation_tips=['Never hang cashmere sweaters as it stretches the shoulders.', 'Use natural cashmere comb to gently remove pills.', 'Rest 24 hours between wears to let fibers recover elasticity.']
    ),
    "HEAVY_FRENCH_TERRY": FabricCareProtocol(
        fabric_code="HEAVY_FRENCH_TERRY",
        fabric_name="450 GSM Organic French Terry",
        fiber_composition="100% Organic Combed Cotton",
        wash_type="GENTLE_MACHINE_30",
        max_water_temp_c=30,
        detergent_recommendation="Standard color-safe liquid detergent",
        bleach_safe=False,
        drying_method="TUMBLE_LOW",
        ironing_temp_c=150,
        steam_safe=True,
        storage_recommendation="Fold flat on wardrobe shelves",
        longevity_preservation_tips=['Wash with similar heavy garments to prevent friction wear.', 'Dry flat or tumble dry on low to prevent shrinkage.', 'Do not iron directly over rubberized graphic prints.']
    ),
    "TENCEL_LYOCELL_TWILL": FabricCareProtocol(
        fabric_code="TENCEL_LYOCELL_TWILL",
        fabric_name="Lenzing TENCEL™ Lyocell Twill",
        fiber_composition="100% Lyocell",
        wash_type="GENTLE_MACHINE_30",
        max_water_temp_c=30,
        detergent_recommendation="Gentle liquid detergent",
        bleach_safe=False,
        drying_method="LINE_DRY_SHADE",
        ironing_temp_c=130,
        steam_safe=True,
        storage_recommendation="Hang on padded satin hangers",
        longevity_preservation_tips=['Wash on gentle cycle to prevent surface fibrillation.', 'Iron on reverse side using medium heat.', 'Dries quickly due to natural fiber breathability.']
    ),
    "ORGANIC_COTTON_VOILE": FabricCareProtocol(
        fabric_code="ORGANIC_COTTON_VOILE",
        fabric_name="Superfine Organic Cotton Voile",
        fiber_composition="100% Cotton",
        wash_type="HAND_WASH_COLD",
        max_water_temp_c=30,
        detergent_recommendation="Mild liquid wash",
        bleach_safe=False,
        drying_method="LINE_DRY_SHADE",
        ironing_temp_c=160,
        steam_safe=True,
        storage_recommendation="Hang on padded hangers",
        longevity_preservation_tips=['Handle gently when wet as fine threads are delicate.', 'Light spray starch can restore crisp hand feel.', 'Dry in shade to preserve vibrant vegetable block prints.']
    ),
    "DUCHESS_SILK_SATIN": FabricCareProtocol(
        fabric_code="DUCHESS_SILK_SATIN",
        fabric_name="Heavy Silk Duchess Satin 280 GSM",
        fiber_composition="100% Silk",
        wash_type="DRY_CLEAN_ONLY",
        max_water_temp_c=0,
        detergent_recommendation="Professional couture dry clean",
        bleach_safe=False,
        drying_method="FLAT_IN_SHADE",
        ironing_temp_c=110,
        steam_safe=False,
        storage_recommendation="Store in garment bag with padded shoulder support",
        longevity_preservation_tips=['Never apply steam directly as it causes water spots on satin.', 'Press only on reverse with dry iron and press cloth.', 'Keep away from sharp jewelry that could snag filament floats.']
    ),
    "RAW_TUSSAR_SILK": FabricCareProtocol(
        fabric_code="RAW_TUSSAR_SILK",
        fabric_name="Wild Forest Tussar Silk (Kosa)",
        fiber_composition="100% Wild Tussar Silk",
        wash_type="DRY_CLEAN_ONLY",
        max_water_temp_c=20,
        detergent_recommendation="Mild wool/silk detergent",
        bleach_safe=False,
        drying_method="FLAT_IN_SHADE",
        ironing_temp_c=120,
        steam_safe=True,
        storage_recommendation="Store in muslin wrap",
        longevity_preservation_tips=['Rich textured slubs are characteristic of wild silk.', 'Keep away from direct sunlight to prevent natural gold fading.', 'Dry clean for first 3 washes to set natural vegetable dyes.']
    ),
    "FINE_MERINO_WOOL": FabricCareProtocol(
        fabric_code="FINE_MERINO_WOOL",
        fabric_name="19.5 Micron Australian Merino Wool",
        fiber_composition="100% Merino Wool",
        wash_type="HAND_WASH_COLD",
        max_water_temp_c=30,
        detergent_recommendation="Woolmark approved detergent",
        bleach_safe=False,
        drying_method="FLAT_IN_SHADE",
        ironing_temp_c=130,
        steam_safe=True,
        storage_recommendation="Fold in cedar chest",
        longevity_preservation_tips=['Natural antimicrobial properties require fewer washes; air out overnight.', 'Do not use fabric softeners as they coat the active wool fibers.', 'Steam iron gently without pressing down hard.']
    ),
    "COTTON_CORDUROY_WALE": FabricCareProtocol(
        fabric_code="COTTON_CORDUROY_WALE",
        fabric_name="12-Wale Heavy Cotton Corduroy",
        fiber_composition="100% Cotton",
        wash_type="MACHINE_WARM",
        max_water_temp_c=40,
        detergent_recommendation="Standard laundry detergent",
        bleach_safe=False,
        drying_method="TUMBLE_LOW",
        ironing_temp_c=150,
        steam_safe=True,
        storage_recommendation="Hang on sturdy coat hangers",
        longevity_preservation_tips=['Wash inside out to protect raised velvet pile wales.', 'Brush pile with soft clothes brush while still damp.', 'Iron only on the reverse side to avoid crushing the texture.']
    ),
    "CHANDERI_SILK_COTTON": FabricCareProtocol(
        fabric_code="CHANDERI_SILK_COTTON",
        fabric_name="Handloom Chanderi Silk-Cotton Blend",
        fiber_composition="60% Silk, 40% Cotton",
        wash_type="DRY_CLEAN_ONLY",
        max_water_temp_c=30,
        detergent_recommendation="Gentle mild wash",
        bleach_safe=False,
        drying_method="LINE_DRY_SHADE",
        ironing_temp_c=130,
        steam_safe=True,
        storage_recommendation="Store in breathable saree bags",
        longevity_preservation_tips=['Sheer crisp texture is created by traditional gumming technique.', 'Iron on moderate heat while slightly damp.', 'Dry clean recommended to preserve gold zari border integrity.']
    ),
    "PURE_VICUNA_LUXURY": FabricCareProtocol(
        fabric_code="PURE_VICUNA_LUXURY",
        fabric_name="Rare Andean Vicuña Wool",
        fiber_composition="100% Vicuña",
        wash_type="DRY_CLEAN_ONLY",
        max_water_temp_c=0,
        detergent_recommendation="Exclusive specialist dry cleaning",
        bleach_safe=False,
        drying_method="FLAT_IN_SHADE",
        ironing_temp_c=100,
        steam_safe=False,
        storage_recommendation="Store in climate-controlled cedar wardrobe",
        longevity_preservation_tips=['Extremely fine 12-micron fiber; treat with utmost reverence.', 'Brush with silver-tipped goat hair clothes brush.', 'Never expose to friction or synthetic seatbelt rubs.']
    ),
    "BOUCLE_TWEED_WOOL": FabricCareProtocol(
        fabric_code="BOUCLE_TWEED_WOOL",
        fabric_name="Textured Bouclé Wool Tweed",
        fiber_composition="75% Wool, 25% Silk",
        wash_type="DRY_CLEAN_ONLY",
        max_water_temp_c=0,
        detergent_recommendation="Professional dry clean",
        bleach_safe=False,
        drying_method="FLAT_IN_SHADE",
        ironing_temp_c=120,
        steam_safe=True,
        storage_recommendation="Hang on contoured wooden blazer hangers",
        longevity_preservation_tips=['Loop yarn texture can snag on rough surfaces or pet claws.', 'Steam carefully to refresh shape without flattening loops.', 'Use cedar balls to protect natural wool from moth larvae.']
    ),
    "HABOTAI_SILK_LINING": FabricCareProtocol(
        fabric_code="HABOTAI_SILK_LINING",
        fabric_name="Habotai 8-Momme Silk Lining",
        fiber_composition="100% Silk",
        wash_type="HAND_WASH_COLD",
        max_water_temp_c=25,
        detergent_recommendation="Silk wash",
        bleach_safe=False,
        drying_method="LINE_DRY_SHADE",
        ironing_temp_c=110,
        steam_safe=True,
        storage_recommendation="Store inside garment",
        longevity_preservation_tips=['Lightweight featherweight silk used for luxury jacket linings.', 'Iron on low silk setting.', 'Anti-static natural drape slides easily over wool and cotton.']
    ),
    "ORGANIC_HEMP_CANVAS": FabricCareProtocol(
        fabric_code="ORGANIC_HEMP_CANVAS",
        fabric_name="Heavyweight Organic Hemp Canvas",
        fiber_composition="100% Hemp",
        wash_type="MACHINE_WARM",
        max_water_temp_c=40,
        detergent_recommendation="Heavy-duty eco detergent",
        bleach_safe=False,
        drying_method="LINE_DRY_SHADE",
        ironing_temp_c=200,
        steam_safe=True,
        storage_recommendation="Hang or fold",
        longevity_preservation_tips=["One of nature's strongest natural fibers; highly resistant to mildew.", 'Becomes significantly softer with repeated washing cycles.', 'Iron damp for clean structured utility appearance.']
    ),
    "PIMA_COTTON_INTERLOCK": FabricCareProtocol(
        fabric_code="PIMA_COTTON_INTERLOCK",
        fabric_name="Supima American Pima Cotton Knit",
        fiber_composition="100% Extra-Long Staple Pima",
        wash_type="GENTLE_MACHINE_30",
        max_water_temp_c=30,
        detergent_recommendation="Mild liquid detergent",
        bleach_safe=False,
        drying_method="TUMBLE_LOW",
        ironing_temp_c=150,
        steam_safe=True,
        storage_recommendation="Fold on wardrobe shelves",
        longevity_preservation_tips=['Resists pilling and fading over 100+ wash cycles.', 'Double jersey interlock construction gives structural heft.', 'Warm iron if desired for pristine smooth surface.']
    ),
    "DEVORE_SILK_VELVET": FabricCareProtocol(
        fabric_code="DEVORE_SILK_VELVET",
        fabric_name="Burnout Devoré Silk Velvet",
        fiber_composition="70% Rayon Pile, 30% Silk Base",
        wash_type="DRY_CLEAN_ONLY",
        max_water_temp_c=0,
        detergent_recommendation="Couture dry clean only",
        bleach_safe=False,
        drying_method="FLAT_IN_SHADE",
        ironing_temp_c=100,
        steam_safe=False,
        storage_recommendation="Hang on wide velvet hangers in breathable garment bag",
        longevity_preservation_tips=['Never press iron directly onto velvet pile; steam from reverse only.', 'Use velvet needle board if pressing seams is necessary.', 'Store with ample spacing in closet to avoid pile crushing.']
    ),
}
