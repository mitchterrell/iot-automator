"""Base class for all devices"""

from typing import Iterable
from _IHub._IDevice._IProperty import IProperty
from _IHub._IDevice._IAction import IAction


class IDevice:
    """
    Abstract class for devices to be implemented individually by each hub
    """

    _properties = []
    _actions = []

    @property
    def properties(self) -> Iterable[IProperty]:
        """
        properties Set of properties that belong to a particular device

        :return: Returns a list of property types
        :rtype: list
        """
        return self._properties

    @property
    def actions(self) -> Iterable[IAction]:
        """
        actions Set of actions that belong to a particular device

        :return: Returns a list of action types
        :rtype: list
        """
        return self._actions
