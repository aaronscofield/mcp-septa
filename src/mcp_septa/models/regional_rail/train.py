"""train.py"""

from typing import Optional
from pydantic import BaseModel, Field


class Train(BaseModel):
    """Pydantic model representing the status of a regional rail train."""

    lat: str
    lon: str
    train_number: str = Field(..., alias="trainno")
    service: str
    dest: str
    current_stop: str = Field(..., alias="currentstop")
    next_stop: str = Field(..., alias="nextstop")
    line: str
    consist: str
    heading: str
    late: int
    source: Optional[str] = Field(None, alias="SOURCE")
    track: Optional[str] = Field(None, alias="TRACK")
    track_change: Optional[str] = Field(None, alias="TRACK_CHANGE")
