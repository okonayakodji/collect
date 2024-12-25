"""
Module for creating plugins for services 
that will be automatically used 
when found in a configuration file.
"""

from abc import abstractmethod


class PluginTask:
    """"""

    def __init__(self):
        raise NotImplementedError

    def __repr__(self):
        return str(self.__dict__)

    @abstractmethod
    async def complete(self):
        """The main work of the plugin should be implemented in this function."""

        raise NotImplementedError


class PluginSettings:
    """"""

    def __init__(self):
        raise NotImplementedError

    def __repr__(self):
        return str(self.__dict__)


class Plugin:
    def __init__(self, settings: PluginSettings):
        self.settings = settings

    def __repr__(self):
        return str(self.__dict__)

    @abstractmethod
    async def generate_task(self, time) -> PluginTask | None:
        """
        The `Scheduler` will use this function at each check.
        If the time is right, it will return `PluginTask`,
        otherwise it will return `None`
        """
        raise NotImplementedError
