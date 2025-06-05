"""bus_and_trolley.py"""

from logging import Logger

from httpx import Client

from mcp_septa.models.bus_and_trolley import Location, Route, RouteInfo


class BusAndTrolley:
    """Class to define interactions with the Septa API for regional rail services.

    Args:
        client (Client):            The HTTPX client to use for HTTP operations
        log (Logger):               The logger instance to use
    """

    __slots__ = ("client", "log")

    def __init__(self, client: Client, log: Logger):
        self.client = client
        self.log = log

    def get_location_by_route_number(self, route_number: int) -> list[Location]:
        """Function to call the "bus and trolley location by route" endpoint. Works
        for both buses and trolleys.

        Args:
            route_number (int):     The number of the bus/trolley route.

        Returns:
            list[Location]:         The current locations of buses/trolleys on that route.
        """

        response = self.client.get(
            url="https://www3.septa.org/api/TransitView/index.php",
            params={"route": str(route_number)},
        )
        result = response.json()

        locations = []
        if "bus" in result:
            for location in result["bus"]:
                locations.append(Location(**location))

        if "trolley" in result:
            for location in result["trolley"]:
                locations.append(Location(**location))

        return locations

    def get_detours_by_route_number(self, route_number: int) -> list[Route]:
        """Function to call the "bus detours" endpoint. Returns the details of
        detours for a given route if present.

        Args:
            route_number (int):             The number of the route to retrieve detours for

        Returns:
            list[Route]:                    Details of the route detours if any are present.
        """
        response = self.client.get(
            url="https://www3.septa.org/api/BusDetours/index.php",
            params={"req1": str(route_number)},
        )
        result = response.json()

        routes = []
        for route in result:
            route_info = []
            route_id = route["route_id"]

            for info in route["route_info"]:
                route_info.append(RouteInfo(**info))

            routes.append(Route(route_id=str(route_id), route_info=route_info))

        return routes
