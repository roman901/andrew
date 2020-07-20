from andrew.plugin import Plugin
from andrew.service.connectors import Connector, register_connector
from andrew.service.plugins import register_plugin


@register_plugin
@register_connector
class TelegramConnector(Plugin, Connector):
    def get_description(self) -> str:
        return 'Connector for Telegram protocol'

    def get_author(self) -> str:
        return 'Roman Shishkin <spark@uwtech.org>'

    async def connect(self):
        print('tg connect')

    async def disconnect(self):
        print('tg disconnect')
