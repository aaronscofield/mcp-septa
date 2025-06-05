"""regional_rail.py"""

from logging import Logger
from httpx import Client

from mcp_septa.models.regional_rail import (
    RegionalRailStation,
    Train,
    NextToArriveResult,
)


class RegionalRail:
    """Class to define interactions with the Septa API for regional rail services.

    Args:
        client (Client):            The HTTPX client to use for HTTP operations
        log (Logger):               The logger instance to use
    """

    __slots__ = ("client", "log")

    def __init__(self, client: Client, log: Logger):
        self.client = client
        self.log = log

    def get_next_to_arrive(
        self, starting_station: RegionalRailStation, ending_station: RegionalRailStation
    ) -> list[NextToArriveResult]:
        """Function to call the "next to arrive" endpoint. Returns departure
        and arrival times between two different stations.

        Args:
            starting_station (RegionalRailStations):    Starting regional rail station
            ending_station (RegionalRailStations):      Ending regional rail station

        Returns:
            list[NextToArriveResult]:                   A list of results
        """

        response = self.client.get(
            url="https://www3.septa.org/api/NextToArrive/index.php",
            params={"req1": starting_station.value, "req2": ending_station.value},
        )
        result = response.json()

        result_list = []
        for entry in result:
            result_list.append(NextToArriveResult(**entry))

        return result_list

    def get_all_trains(
        self,
    ) -> list[Train]:
        """Function to call the "get train view" endpoint. Returns status
        of all regional rail trains, showing the trains ID number,
        its starting location, its destination, and if its late or not.

        Args:
            None

        Returns:
            list[Train]:    A list of all active regional rail trains and their info.
        """

        response = self.client.get(
            url="https://www3.septa.org/api/TrainView/index.php",
        )
        result = response.json()

        trains = []
        for train in result:
            trains.append(Train(**train))

        return trains
