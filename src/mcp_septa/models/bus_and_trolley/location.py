"""location.py"""

from typing import Optional
from pydantic import BaseModel, Field


class Location(BaseModel):
    """Pydantic model represneting the location of a bus or trolley."""

    lat: str
    lng: str
    label: str
    trip: str
    vehicle_id: str = Field(..., alias="VehicleID")
    block_id: str = Field(..., alias="BlockID")
    direction: str = Field(..., alias="Direction")
    destination: str
    heading: Optional[str | float] = None
    late: int
    next_stop_id: Optional[float | str] = None
    next_stop_name: Optional[str] = None
    next_stop_sequence: Optional[int] = None
    estimated_seat_availability: str
    offset: int = Field(..., alias="Offset")
    offset_sec: str = Field(..., alias="Offset_sec")
    timestamp: int
