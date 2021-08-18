from pydantic import BaseModel
from typing import List, Optional, Dict
from decimal import Decimal
from datetime import datetime


class SpotSchema(BaseModel):
    spot_id: str
    buy_price: Decimal
    chart_url: Optional[str]
    created_at: datetime
    current_price: Optional[Decimal]
    risk: str  # TODO Turn into Enum if needed
    pair: str
    stop_price: Decimal
    symbol: str
    tp1: Decimal
    tp2: Decimal
    tp3: Decimal
    tp_done: int
    total_tp: int
    spot_type: str  # TODO Turn into Enum if needed
    coin_logo_url: str


class FutureSchema(BaseModel):
    future_id: str
    chart_url: Optional[str]
    created_at: datetime
    current_price: Optional[Decimal]
    entry_price: Decimal  # TODO Make sure
    future_type: str
    initial_price: Decimal
    is_filled: bool
    risk: str  # TODO Turn into Enum if needed
    leverage: str  # TODO Fix
    pair: str
    stop_price: Decimal
    tp1: Decimal
    tp2: Decimal
    tp3: Decimal
    tp_done: int
    total_tp: int
    future_type: str  # TODO Turn into Enum if needed


class SignalSchema(BaseModel):
    spots: Optional[List[SpotSchema]]
    futures: Optional[List[FutureSchema]]
