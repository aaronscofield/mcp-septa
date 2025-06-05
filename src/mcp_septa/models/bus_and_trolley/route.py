"""route.py"""

from pydantic import BaseModel


class RouteInfo(BaseModel):
    """Pydantic model representing information for a given route."""

    route_direction: str
    reason: str
    start_location: str
    end_location: str
    start_date_time: str
    end_date_time: str
    current_message: str


class Route(BaseModel):
    """Pydantic model representing a route."""

    route_id: str
    route_info: list[RouteInfo]
