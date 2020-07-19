from typing import Dict

from andrew.plugin import Plugin
from andrew.service import Service


class PluginsService(Service):
    plugins: Dict[str, Plugin]

    def register(self, plugin):
        self.plugins[plugin.get_name()] = plugin
        plugin.load()
        print(plugin)

    def unload(self):
        for plugin in self.plugins.values():
            plugin.unload()


def register_plugin(plugin):
    plugins = PluginsService()
    plugins.register(plugin.__init__())
