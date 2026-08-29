"""
Real-Time Live Streaming Fashion Commerce & Runway Auction Bidding Engine.
Coordinates live runway drop broadcasts, interactive viewer reaction streams,
and real-time auction bidding with sniper-defense protection.
"""

from typing import Dict, List, Optional, Any, Set
from pydantic import BaseModel, Field
from datetime import datetime, timezone, timedelta
import uuid


class RunwayBid(BaseModel):
    bid_id: str
    stream_id: str
    product_id: str
    user_id: str
    user_name: str
    bid_amount: float
    timestamp: datetime


class LiveBroadcastSession(BaseModel):
    stream_id: str
    vendor_id: str
    channel_title: str
    host_name: str
    is_live: bool = True
    viewer_count: int = 1
    likes_count: int = 0
    pinned_product_id: Optional[str] = None
    auction_active: bool = False
    auction_start_price: float = 100.0
    auction_min_increment: float = 20.0
    auction_end_time: Optional[datetime] = None
    highest_bid: Optional[RunwayBid] = None
    bids_history: List[RunwayBid] = []


class LiveCommerceManager:
    def __init__(self):
        self.streams: Dict[str, LiveBroadcastSession] = {}

    def start_stream(
        self,
        vendor_id: str,
        title: str,
        host_name: str,
        pinned_product_id: Optional[str] = None
    ) -> LiveBroadcastSession:
        stream_id = f"stream_{uuid.uuid4().hex[:10]}"
        session = LiveBroadcastSession(
            stream_id=stream_id,
            vendor_id=vendor_id,
            channel_title=title,
            host_name=host_name,
            pinned_product_id=pinned_product_id,
            is_live=True,
            viewer_count=120,
            likes_count=450
        )
        self.streams[stream_id] = session
        return session

    def launch_runway_auction(
        self,
        stream_id: str,
        product_id: str,
        starting_price: float,
        duration_minutes: int = 5,
        min_increment: float = 25.0
    ) -> Dict[str, Any]:
        if stream_id not in self.streams:
            return {"success": False, "error": "Stream not found"}

        session = self.streams[stream_id]
        now = datetime.now(timezone.utc)
        session.auction_active = True
        session.pinned_product_id = product_id
        session.auction_start_price = starting_price
        session.auction_min_increment = min_increment
        session.auction_end_time = now + timedelta(minutes=duration_minutes)
        session.highest_bid = None
        session.bids_history = []

        return {
            "success": True,
            "stream_id": stream_id,
            "product_id": product_id,
            "starting_price": starting_price,
            "min_increment": min_increment,
            "auction_end_time": session.auction_end_time.isoformat()
        }

    def place_auction_bid(
        self,
        stream_id: str,
        user_id: str,
        user_name: str,
        bid_amount: float
    ) -> Dict[str, Any]:
        if stream_id not in self.streams:
            return {"success": False, "error": "Stream not found"}

        session = self.streams[stream_id]
        if not session.auction_active or not session.auction_end_time:
            return {"success": False, "error": "No active auction in this stream"}

        now = datetime.now(timezone.utc)
        if now > session.auction_end_time:
            session.auction_active = False
            return {"success": False, "error": "Auction has ended"}

        current_min = (
            session.highest_bid.bid_amount + session.auction_min_increment
            if session.highest_bid
            else session.auction_start_price
        )

        if bid_amount < current_min:
            return {
                "success": False,
                "error": f"Bid must be at least ${current_min:.2f}"
            }

        # Anti-sniping: extend by 45 seconds if bid arrives in final 30 seconds
        time_left = (session.auction_end_time - now).total_seconds()
        sniper_extended = False
        if time_left < 30.0:
            session.auction_end_time += timedelta(seconds=45)
            sniper_extended = True

        new_bid = RunwayBid(
            bid_id=f"bid_{uuid.uuid4().hex[:8]}",
            stream_id=stream_id,
            product_id=session.pinned_product_id or "runway_item",
            user_id=user_id,
            user_name=user_name,
            bid_amount=bid_amount,
            timestamp=now
        )
        session.highest_bid = new_bid
        session.bids_history.append(new_bid)

        return {
            "success": True,
            "bid_id": new_bid.bid_id,
            "highest_bid": new_bid.bid_amount,
            "bidder": new_bid.user_name,
            "sniper_extension_triggered": sniper_extended,
            "new_end_time": session.auction_end_time.isoformat(),
            "total_bids": len(session.bids_history)
        }

    def record_reaction(self, stream_id: str, reaction_type: str = "LIKE") -> Dict[str, Any]:
        if stream_id not in self.streams:
            return {"success": False, "error": "Stream not found"}
        session = self.streams[stream_id]
        session.likes_count += 1
        return {"stream_id": stream_id, "likes_count": session.likes_count}


# Singleton live commerce manager
live_manager = LiveCommerceManager()
