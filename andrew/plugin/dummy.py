from andrew.plugin import Plugin
from andrew.service.plugins import register_plugin


@register_plugin
class DummyPlugin(Plugin):
    def get_description(self) -> str:
        return 'Plugin for Andrew bot testing'

    def get_author(self) -> str:
        return 'Roman Shishkin <spark@uwtech.org>'
