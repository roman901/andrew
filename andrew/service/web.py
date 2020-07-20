import os
from typing import List

from aiohttp import web

from andrew.service import Service


class WebService(Service):
    started: bool = False
    app: web.Application = web.Application()
    routes: List = []

    async def start(self):
        host = os.environ.get('WEB_HOST', '0.0.0.0')
        port = int(os.environ.get('WEB_PORT', 8000))
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, host, port)
        await site.start()

        self.started = True
