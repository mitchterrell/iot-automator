"""Base class for IoT Hubs to implement """


from typing import Iterable
from _IHub._IDevice import *


class IHub:
    """Abstract hub class"""

    _devices = []

    @property
    def devices(self) -> Iterable[IDevice]:
        """
        devices List of devices for a parciular hub

        :return: List of device types
        :rtype: Iterable[IDevice]
        """
        return self._devices
