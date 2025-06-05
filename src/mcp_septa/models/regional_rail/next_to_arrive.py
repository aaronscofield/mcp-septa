"""next_to_arrive.py"""

from typing import Optional
from pydantic import BaseModel, Field


class NextToArriveResult(BaseModel):
    """Pydantic model representing the result of a next to arrive call"""

    orig_train: str
    orig_line: str
    orig_departure_time: str
    orig_arrival_time: str
    orig_delay: str
    term_train: Optional[str] = None
    term_line: Optional[str] = None
    term_depart_time: Optional[str] = None
    term_arrival_time: Optional[str] = None
    connection: Optional[str] = Field(None, alias="Connection")
    term_delay: Optional[str] = None
    is_direct: bool = Field(False, alias="isdirect")
