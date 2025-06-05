"""septa.py"""

from logging import getLogger

from httpx import Client

from mcp_septa.septa.bus_and_trolley import BusAndTrolley
from mcp_septa.septa.regional_rail import RegionalRail


class Septa:  # pylint: disable=too-few-public-methods
    """Class representing interactions with the public Septa APIs
    that are found at the following address: https://www3.septa.org/#/."""

    __slots__ = ("client", "log", "regional_rail", "bus_and_trolley")

    def __init__(self):
        self.client = Client()
        self.log = getLogger()

        self.regional_rail = RegionalRail(client=self.client, log=self.log)
        self.bus_and_trolley = BusAndTrolley(client=self.client, log=self.log)
