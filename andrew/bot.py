import os
import uvloop
import asyncio

from andrew.service.plugins import PluginsService


class AndrewBot:
    def run_loop(self):
        """
        Starts bot async loop and setup core services
        """

        uvloop.install()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.start())

    async def start(self):
        plugins = PluginsService()
        plugins.scan(os.path.join(os.path.dirname(__file__), 'plugin'))
        await plugins.pre_connect()

        await plugins.post_connect()
