import os
import asyncio
import signal
from asyncio import AbstractEventLoop

import uvloop

from andrew.service.connectors import ConnectorsService
from andrew.service.plugins import PluginsService
from andrew.service.web import WebService


class AndrewBot:
    loop: AbstractEventLoop

    def run_loop(self):
        """
        Starts bot async loop and setup core services
        """

        uvloop.install()
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.start())

        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            self.stop()

    async def start(self):
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        plugins = PluginsService()
        plugins.scan(os.path.join(os.path.dirname(__file__), 'plugin'))

        await plugins.pre_connect()

        connectors = ConnectorsService()
        await connectors.connect()

        web = WebService()
        await web.start()

    def stop(self):
        plugins = PluginsService()
        self.loop.create_task(plugins.post_connect())

        connectors = ConnectorsService()
        self.loop.create_task(connectors.disconnect())

        self.loop.close()
