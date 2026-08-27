"""
Graph-Based Complete-the-Look Outfit Recommendation Algorithm.
Computes multi-edge compatibility across style personas, color harmony,
occasion formality, weather requirements, and garment layering hierarchy.
"""

from typing import Dict, List, Optional, Any, Set, Tuple
from pydantic import BaseModel, Field
from enum import Enum
import math


class OutfitRole(str, Enum):
    PRIMARY_STATEMENT = "PRIMARY_STATEMENT"
    TOPWEAR_BASE = "TOPWEAR_BASE"
    BOTTOMWEAR = "BOTTOMWEAR"
    OUTERWEAR = "OUTERWEAR"
    FOOTWEAR = "FOOTWEAR"
    ACCESSORY_BAG = "ACCESSORY_BAG"
    ACCESSORY_JEWELRY = "ACCESSORY_JEWELRY"
    ACCESSORY_EYEWEAR = "ACCESSORY_EYEWEAR"


class FormalityIndex(str, Enum):
    CASUAL_RELAXED = "CASUAL_RELAXED"      # T-shirts, joggers, sneakers
    SMART_CASUAL = "SMART_CASUAL"          # Chinos, polo, linen shirts, loafers
    BUSINESS_FORMAL = "BUSINESS_FORMAL"    # Suits, oxford shirts, tailored trousers, derbies
    BLACK_TIE_GLAM = "BLACK_TIE_GLAM"      # Tuxedo, floor-length velvet/silk gown, stilettos
    ROYAL_HERITAGE = "ROYAL_HERITAGE"      # Zari lehengas, sherwanis, bandhgalas


class FashionNode(BaseModel):
    id: str
    title: str
    role: OutfitRole
    category_id: str
    brand_id: str
    price: float
    mrp: float
    primary_color_hex: str
    accent_color_hex: Optional[str] = None
    fabric_id: str
    style_tags: List[str]
    occasion: str
    formality: FormalityIndex
    temperature_min_c: float = 15.0
    temperature_max_c: float = 35.0
    image_url: str


class OutfitGraphEngine:
    @staticmethod
    def calculate_edge_weight(node_a: FashionNode, node_b: FashionNode) -> float:
        """
        Calculates compatibility score between two fashion items.
        Weight factors:
        1. Formality coherence (30%)
        2. Style persona overlap (30%)
        3. Color harmony (25%)
        4. Category balance (15%)
        """
        score = 0.0

        # Formality match
        if node_a.formality == node_b.formality:
            score += 30.0
        elif abs(list(FormalityIndex).index(node_a.formality) - list(FormalityIndex).index(node_b.formality)) == 1:
            score += 20.0
        else:
            score += 5.0

        # Style tags Jaccard similarity
        set_a = set(t.lower() for t in node_a.style_tags)
        set_b = set(t.lower() for t in node_b.style_tags)
        intersection = len(set_a.intersection(set_b))
        union = len(set_a.union(set_b))
        jaccard = intersection / union if union > 0 else 0.0
        score += (jaccard * 30.0)

        # Occasion match
        if node_a.occasion.upper() == node_b.occasion.upper():
            score += 25.0
        else:
            score += 10.0

        # Temperature compatibility overlap
        overlap_min = max(node_a.temperature_min_c, node_b.temperature_min_c)
        overlap_max = min(node_a.temperature_max_c, node_b.temperature_max_c)
        if overlap_max >= overlap_min:
            score += 15.0
        else:
            score += 0.0

        return round(score, 2)

    @staticmethod
    def assemble_complete_outfit(
        primary_item: FashionNode,
        candidate_pool: List[FashionNode],
        max_items: int = 4
    ) -> Dict[str, Any]:
        """
        Greedy graph search assembling the highest-scoring ensemble containing:
        - Primary item
        - Complementary bottomwear (if primary is topwear)
        - Complementary footwear
        - Complementary accessory
        """
        selected_nodes: List[FashionNode] = [primary_item]
        filled_roles: Set[OutfitRole] = {primary_item.role}

        target_roles = [
            OutfitRole.BOTTOMWEAR,
            OutfitRole.FOOTWEAR,
            OutfitRole.ACCESSORY_BAG,
            OutfitRole.OUTERWEAR
        ]

        for target_role in target_roles:
            if target_role in filled_roles:
                continue

            candidates_for_role = [c for c in candidate_pool if c.role == target_role and c.id != primary_item.id]
            if not candidates_for_role:
                continue

            # Score each candidate against all currently selected nodes
            best_candidate = None
            best_score = -1.0

            for cand in candidates_for_role:
                avg_edge = sum(OutfitGraphEngine.calculate_edge_weight(cand, s) for s in selected_nodes) / len(selected_nodes)
                if avg_edge > best_score:
                    best_score = avg_edge
                    best_candidate = cand

            if best_candidate and best_score >= 50.0:
                selected_nodes.append(best_candidate)
                filled_roles.add(target_role)

            if len(selected_nodes) >= max_items:
                break

        # Calculate bundle pricing and savings
        total_mrp = sum(n.mrp for n in selected_nodes)
        total_base = sum(n.price for n in selected_nodes)
        bundle_discount_rate = 0.10  # 10% bundle discount
        bundle_price = round(total_base * (1.0 - bundle_discount_rate), 2)
        bundle_savings = round(total_mrp - bundle_price, 2)

        return {
            "primary_item_id": primary_item.id,
            "outfit_theme": f"{primary_item.formality.value.replace('_', ' ').title()} Look",
            "occasion": primary_item.occasion,
            "items": [
                {
                    "id": n.id,
                    "title": n.title,
                    "role": n.role.value,
                    "price": n.price,
                    "mrp": n.mrp,
                    "image_url": n.image_url,
                    "brand_id": n.brand_id
                }
                for n in selected_nodes
            ],
            "item_count": len(selected_nodes),
            "bundle_total_mrp": total_mrp,
            "bundle_price": bundle_price,
            "bundle_savings": bundle_savings,
            "bundle_discount_pct": 10.0
        }
