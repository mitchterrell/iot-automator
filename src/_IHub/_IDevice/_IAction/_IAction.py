"""Base class for device actions"""

from abc import abstractmethod


class IAction:
    """
    Abstract class for device actions
    """

    @abstractmethod
    def run(self):
        """
        run Abstract method to run an action

        :raises Exception: If left unimplemented an exception will be raised
        """
        raise Exception("Method is not implemented")
