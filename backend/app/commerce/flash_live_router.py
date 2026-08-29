"""
Flash Sales & Live Streaming Commerce REST Router.
"""

from fastapi import APIRouter, HTTPException, Query, status
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime, timezone, timedelta

from app.commerce.flash_sales import flash_engine, FlashSaleDrop
from app.commerce.live_streaming import live_manager

router = APIRouter(prefix="/commerce/live", tags=["Flash Sales & Live Commerce"])


class RegisterFlashDropRequest(BaseModel):
    drop_id: str
    product_id: str
    title: str
    original_price: float
    flash_price: float
    total_inventory: int
    duration_minutes: int = 60
    starts_in_minutes: int = 0


class ClaimReservationRequest(BaseModel):
    drop_id: str
    user_id: str
    quantity: int = 1


class CreateStreamRequest(BaseModel):
    vendor_id: str
    channel_title: str
    host_name: str
    pinned_product_id: Optional[str] = None


class StartAuctionRequest(BaseModel):
    product_id: str
    starting_price: float
    duration_minutes: int = 5
    min_increment: float = 25.0


class PlaceBidRequest(BaseModel):
    user_id: str
    user_name: str
    bid_amount: float


@router.post("/flash-sales/register")
def register_flash_drop(payload: RegisterFlashDropRequest):
    now = datetime.now(timezone.utc)
    start = now + timedelta(minutes=payload.starts_in_minutes)
    end = start + timedelta(minutes=payload.duration_minutes)

    drop = FlashSaleDrop(
        drop_id=payload.drop_id,
        product_id=payload.product_id,
        title=payload.title,
        original_price=payload.original_price,
        flash_price=payload.flash_price,
        total_inventory=payload.total_inventory,
        start_time=start,
        end_time=end
    )
    flash_engine.register_drop(drop)
    return {"message": "Flash drop registered successfully", "drop_id": drop.drop_id}


@router.get("/flash-sales/active")
def list_active_flash_drops():
    return {"drops": flash_engine.get_active_drops()}


@router.post("/flash-sales/reserve")
def claim_flash_reservation(payload: ClaimReservationRequest):
    res = flash_engine.claim_atomic_reservation(
        drop_id=payload.drop_id,
        user_id=payload.user_id,
        quantity=payload.quantity
    )
    if not res.get("success"):
        raise HTTPException(status_code=400, detail=res.get("error"))
    return res


@router.post("/streams/create")
def create_live_stream(payload: CreateStreamRequest):
    session = live_manager.start_stream(
        vendor_id=payload.vendor_id,
        title=payload.channel_title,
        host_name=payload.host_name,
        pinned_product_id=payload.pinned_product_id
    )
    return session


@router.get("/streams/{stream_id}")
def get_stream_details(stream_id: str):
    session = live_manager.streams.get(stream_id)
    if not session:
        raise HTTPException(status_code=404, detail="Stream session not found")
    return session


@router.post("/streams/{stream_id}/auction/start")
def start_runway_auction(stream_id: str, payload: StartAuctionRequest):
    res = live_manager.launch_runway_auction(
        stream_id=stream_id,
        product_id=payload.product_id,
        starting_price=payload.starting_price,
        duration_minutes=payload.duration_minutes,
        min_increment=payload.min_increment
    )
    if not res.get("success"):
        raise HTTPException(status_code=400, detail=res.get("error"))
    return res


@router.post("/streams/{stream_id}/bids")
def submit_auction_bid(stream_id: str, payload: PlaceBidRequest):
    res = live_manager.place_auction_bid(
        stream_id=stream_id,
        user_id=payload.user_id,
        user_name=payload.user_name,
        bid_amount=payload.bid_amount
    )
    if not res.get("success"):
        raise HTTPException(status_code=400, detail=res.get("error"))
    return res


@router.post("/streams/{stream_id}/reaction")
def send_stream_reaction(stream_id: str):
    return live_manager.record_reaction(stream_id)
