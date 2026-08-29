"""
Styling, Virtual Try-On & AI Advisor REST Router.
"""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

from app.styling.virtual_tryon import (
    VirtualTryOnEngine, CustomerAnthropometrics, GarmentSpecs, FabricType, BodyShapeArchetype
)
from app.styling.ai_stylist import (
    ColorTheoryEngine, CapsuleWardrobeCoordinator, AIStylistAdvisor, UndertoneType
)

router = APIRouter(prefix="/styling", tags=["Styling & Virtual Try-On"])


class TryOnSimulationRequest(BaseModel):
    anthropometrics: CustomerAnthropometrics
    garment: GarmentSpecs


class ColorMatchRequest(BaseModel):
    primary_color_hex: str
    secondary_color_hex: str


class CapsuleRequest(BaseModel):
    items: List[Dict[str, Any]]
    style_persona: Optional[str] = "SMART_ELEGANCE"


class AIAdvisorChatRequest(BaseModel):
    prompt: str
    user_gender: Optional[str] = "FEMALE"
    occasion: Optional[str] = "WEDDING_GUEST"


@router.post("/try-on/simulate", response_model=Dict[str, Any])
def simulate_virtual_try_on(payload: TryOnSimulationRequest):
    """Executes anthropometric 3D virtual try-on and tension drape simulation."""
    return VirtualTryOnEngine.simulate_try_on(payload.anthropometrics, payload.garment)


@router.get("/try-on/body-shapes")
def get_supported_body_shapes():
    """Lists anthropometric body archetypes and classification metrics."""
    return {
        "archetypes": [s.value for s in BodyShapeArchetype],
        "fabrics_supported": [f.value for f in FabricType]
    }


@router.post("/advisor/palette-match")
def evaluate_palette_match(payload: ColorMatchRequest):
    """Calculates color harmony, chromatic distance, and stylist pairing notes."""
    return ColorTheoryEngine.calculate_color_harmony_score(
        payload.primary_color_hex,
        payload.secondary_color_hex
    )


@router.get("/advisor/undertone/{undertone}")
def get_undertone_palette(undertone: UndertoneType):
    """Retrieves curated power colors, flattering neutrals, and color advice for an undertone."""
    return ColorTheoryEngine.get_palette_for_undertone(undertone)


@router.post("/advisor/capsule")
def generate_capsule_wardrobe(payload: CapsuleRequest):
    """Generates a multi-day capsule wardrobe rotation from core pieces."""
    return CapsuleWardrobeCoordinator.generate_7_day_capsule(
        payload.items,
        payload.style_persona or "SMART_ELEGANCE"
    )


@router.post("/advisor/chat")
def chat_with_ai_stylist(payload: AIAdvisorChatRequest):
    """Interactive real-time consultation with AI Fashion Stylist."""
    return AIStylistAdvisor.answer_styling_query(
        payload.prompt,
        payload.user_gender,
        payload.occasion
    )
