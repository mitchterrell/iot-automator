"""Base class for device properties"""

from abc import abstractmethod
from typing import TypeVar


T = TypeVar("T")


class IProperty:
    @abstractmethod
    def set(self, val: T) -> None:
        """
        set Generic property setter method, to be overriden by implementer

        :param val: Value to set the property to of generic type
        :type val: T
        :raises Exception: If unimplemented, raises exception
        """
        raise Exception("Method is not implemented")

    @abstractmethod
    def get(self) -> T:
        """
        get Generic propety getter method, to be overridden by implementer

        :raises Exception: If unimplemented, raises exception
        :return: Generic return value to be overriden
        :rtype: T
        """
        raise Exception("Method is not implemented")
