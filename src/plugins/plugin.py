"""Metaclasses for creating new plugin"""

from abc import abstractmethod

REGISTRY = {}


class Plugin:
    """TODO"""

    def __init_subclass__(cls, aliases=None | list, **kwargs):
        """TODO"""

        super().__init_subclass__(**kwargs)
        if aliases:
            for alias in aliases:
                REGISTRY.update({alias: cls})
        cls.aliases = aliases

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def check(self):
        """TODO"""
        raise NotImplementedError

    @abstractmethod
    def run(self):
        """TODO"""
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError
