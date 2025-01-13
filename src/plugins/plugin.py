"""Metaclasses for creating new plugin"""

from abc import abstractmethod


REGISTRY = {}


class Plugin:
    """
    Metaclass for creating plugins.

    > When creating a new plugin, you need to specify the
    `aliases` parameter - a list of possible plugin names
    that will be searched for in the configuration file.

    > Each alias will be added to the `REGISTRY` - a dictionary
    used to search for plugins by other program modules.
    """

    def __init_subclass__(cls, aliases=None | list, **kwargs):
        """
        Function called when subclasses are created.
        Used to implement alias logic.
        """

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
        """
        Function to check if the plugin should be run now.
        """
        raise NotImplementedError

    @abstractmethod
    def run(self):
        """
        Function to run if the plugin is ready.
        Separated so that plugin readiness can be logged.
        """

        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError
