"""
Haute Couture Styling Aesthetic Rules & Lookbook Combination Matrix.
Defines aesthetic cohesion weights, occasion harmony matrices, forbidden clashes,
and 3-tier layering hierarchies across 30 premier fashion archetypes.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel

class StylingRuleSpec(BaseModel):
    aesthetic_id: str
    aesthetic_name: str
    formality_index: int  # 1 (Casual) to 5 (Ultra Formal/Bridal)
    compatible_fabrics: List[str]
    forbidden_fabric_clashes: List[str]
    color_palette_hexes: List[str]
    base_layer_silhouettes: List[str]
    outerwear_silhouettes: List[str]
    footwear_styles: List[str]
    accessory_must_haves: List[str]
    signature_styling_mantra: str

STYLIST_AESTHETIC_REGISTRY: Dict[str, StylingRuleSpec] = {
    "MINIMALIST_ARCHITECTURAL": StylingRuleSpec(
        aesthetic_id="MINIMALIST_ARCHITECTURAL",
        aesthetic_name="Architectural Minimalist",
        formality_index=3,
        compatible_fabrics=['Belgian Linen', 'Giza Cotton Poplin', 'Wool Gabardine'],
        forbidden_fabric_clashes=['Polyester Sequins', 'Crushed Velvet'],
        color_palette_hexes=['#111111', '#FAF9F6', '#8A9A86', '#36454F'],
        base_layer_silhouettes=['Mandarin Collar Shirt', 'Boxy Crewneck'],
        outerwear_silhouettes=['Tailored Single-Breasted Blazer', 'Clean Car Coat'],
        footwear_styles=['Italian Leather Penny Loafers', 'Minimal White Court Sneakers'],
        accessory_must_haves=['Monolithic Titanium Watch', 'Matte Leather Tote'],
        signature_styling_mantra="Form follows function: uncluttered geometric lines, pristine natural drape, zero unnecessary embellishments."
    ),
    "QUIET_LUXURY_ESTATE": StylingRuleSpec(
        aesthetic_id="QUIET_LUXURY_ESTATE",
        aesthetic_name="Quiet Luxury / Estate Living",
        formality_index=4,
        compatible_fabrics=['Grade-A Cashmere', 'Mulberry Silk', 'Sea Island Cotton', 'Vicuña'],
        forbidden_fabric_clashes=['Neon Synthetics', 'Distressed Denim'],
        color_palette_hexes=['#C19A6B', '#101B2B', '#FAF0E8', '#2B1D16'],
        base_layer_silhouettes=['Cashmere Fine Gauge Crewneck', 'Silk Crepe Blouse'],
        outerwear_silhouettes=['Double-Faced Unlined Cashmere Coat', 'Double-Breasted Wool Blazer'],
        footwear_styles=['Unlined Suede Belgian Loafers', 'Handmade Leather Riding Boots'],
        accessory_must_haves=['Unbranded Calfskin Kelly Bag', 'Subtle Gold Signet Ring'],
        signature_styling_mantra="Whispered prestige: unbranded perfection, peerless tactile materials and timeless tonal balance."
    ),
    "ROYAL_HERITAGE_BRIDAL": StylingRuleSpec(
        aesthetic_id="ROYAL_HERITAGE_BRIDAL",
        aesthetic_name="Royal Heritage Bridal & Festive",
        formality_index=5,
        compatible_fabrics=['Banarasi Katan Silk', 'Raw Mulberry Silk', 'Zari Georgette', 'Silk Velvet'],
        forbidden_fabric_clashes=['Synthetic Rayon', 'Crude Polyester Lurex'],
        color_palette_hexes=['#9B111E', '#D4AF37', '#046307', '#4C1C24'],
        base_layer_silhouettes=['32-Kali Pure Silk Anarkali', 'Embroidered Raw Silk Choli'],
        outerwear_silhouettes=['Royal Zardozi Bandhgala Velvet Jacket', 'Handwoven Pashmina Shawl'],
        footwear_styles=['Handcrafted Embroidered Mojaris', 'Polki Embellished Juttis'],
        accessory_must_haves=['Polki Kundan Jadau Choker', 'Real Gold Zari Handwoven Saree Dupatta'],
        signature_styling_mantra="Centuries of regal splendour: intricate hand zardozi, precious bullion wires, and majestic imperial flares."
    ),
    "TOKYO_URBAN_STREETWEAR": StylingRuleSpec(
        aesthetic_id="TOKYO_URBAN_STREETWEAR",
        aesthetic_name="Tokyo Raw Urban Streetwear",
        formality_index=1,
        compatible_fabrics=['14.5oz Japanese Raw Denim', '450 GSM French Terry', 'Ripstop Nylon'],
        forbidden_fabric_clashes=['Formal Silk Satin', 'Metallic Sequins'],
        color_palette_hexes=['#0A0A0A', '#36454F', '#8A9A86', '#C86D51'],
        base_layer_silhouettes=['Heavyweight Drop-Shoulder Graphic Tee', 'Boxy Thermal Waffle Shirt'],
        outerwear_silhouettes=['Type III Raw Selvedge Trucker', 'Oversized Utility Fishtail Parka'],
        footwear_styles=['Retro Canvas High-Tops', 'Chunky Vibram-Soled Lug Boots'],
        accessory_must_haves=['Cordura Crossbody Bag', 'Silver Goro-Style Feather Pendant'],
        signature_styling_mantra="Heavyweight drape, boxy drop shoulders, authentic raw denim fades, and functional utility."
    ),
    "PARISIAN_CHIC_SARTORIAL": StylingRuleSpec(
        aesthetic_id="PARISIAN_CHIC_SARTORIAL",
        aesthetic_name="Parisian Chic & Tailoring",
        formality_index=3,
        compatible_fabrics=['Fine Merino Wool', 'Silk Charmeuse', 'Bouclé Tweed', 'Cotton Twill'],
        forbidden_fabric_clashes=['Loud Neons', 'Extreme Distressing'],
        color_palette_hexes=['#0A0A0A', '#FAF9F6', '#B0C4DE', '#4C1C24'],
        base_layer_silhouettes=['Breton Striped Boatneck', 'Bias-Cut Silk Slip Top'],
        outerwear_silhouettes=['Cropped Bouclé Tweed Jacket', 'Oversized Trench Coat'],
        footwear_styles=['Leather Slingback Pumps', 'Classic Almond-Toe Ballerina Flats'],
        accessory_must_haves=['Structured Leather Flap Bag', 'Silk Twill Neck Scarf'],
        signature_styling_mantra="Nonchalant elegance: balancing structured tailoring with fluid slips and iconic Parisian ease."
    ),
}
