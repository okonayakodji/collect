import asyncio

from plugin import Plugin


class Schedular:
    def __init__(self, plugins: list[Plugin] = []):
        self.plugins = plugins

    async def run(self):
        ready_plugins = []
        for plugin in self.plugins:
            if plugin.ready():
                ready_plugins.append(plugin.run)
        asyncio.gather(*ready_plugins)
