"""server.py"""

from mcp.server.fastmcp import FastMCP

from mcp_septa.models.bus_and_trolley import Location
from mcp_septa.septa import Septa


mcp = FastMCP("mcp-septa")
septa = Septa()


@mcp.tool(
    name="get_septa_bus_or_trolley_locations_by_route_number",
    description="""
        Given a route number for a bus or trolley, return the 
        locations of all currently running buses or trolleys.
    """,
    annotations={
        "title": "Get SEPTA bus or trolley locations by route number",
        "readOnlyHint": True,
        "openWorldHint": True,
        "idempotentHint": False,
        "destructiveHint": False,
    },
)
def get_location_by_route_number(route_number: int) -> list[Location]:
    """Given a route number for a bus or trolley, return the
    locations of all currently running buses or trolleys.

    Args:
        route_number (int):         The number of the route to get locations for.

    Returns:
        list[Location]:             A list of locations for the given route number.
    """

    return septa.bus_and_trolley.get_location_by_route_number(route_number=route_number)


def main():
    """Main function for running the MCP server."""
    mcp.run(transport="stdio")
