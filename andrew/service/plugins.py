import os
import sys
from typing import Dict

from andrew.plugin import Plugin
from andrew.service import Service


class PluginsService(Service):
    plugins: Dict[str, Plugin]

    def __init__(self):
        self.plugins = {}

    def scan(self, path):
        sys.path.insert(0, path)
        for f in os.listdir(path):
            fname, ext = os.path.splitext(f)
            if ext == '.py':
                __import__(fname)
        sys.path.pop(0)

    def register(self, plugin):
        name = type(plugin).__name__.lower().replace('plugin', '')
        self.plugins[name] = plugin
        plugin.load()

    def unload(self):
        for plugin in self.plugins.values():
            plugin.unload()

    async def pre_connect(self):
        for plugin in self.plugins.values():
            await plugin.pre_connect()

    async def post_connect(self):
        for plugin in self.plugins.values():
            await plugin.post_connect()


def register_plugin(plugin):
    plugins = PluginsService()
    plugins.register(plugin())
