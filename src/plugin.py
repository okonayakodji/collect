from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class PluginResult:
    pass


@dataclass
class PluginSettings:
    pass


class Plugin:
    def __init__(self, settings: PluginSettings):
        self.settings = settings

    @abstractmethod
    async def ready(self) -> bool:
        return True

    async def run(self) -> PluginResult:
        raise NotImplemented
