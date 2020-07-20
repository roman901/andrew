import os

from andrew.plugin import Plugin
from andrew.service.connectors import Connector, register_connector
from andrew.service.logger import LoggerService
from andrew.service.plugins import register_plugin


@register_plugin
@register_connector
class TelegramConnector(Plugin, Connector):
    def get_description(self) -> str:
        return 'Connector for Telegram protocol'

    def get_author(self) -> str:
        return 'Roman Shishkin <spark@uwtech.org>'

    async def connect(self):
        logger = LoggerService()
        token = os.environ.get('TG_TOKEN')
        if not token:
            logger.logger.error('Telegram connector requires bot token which not given. Connector disabled')
            return

        mode = os.environ.get('TG_MODE', 'poll')
        if mode == 'poll':
            pass
        else:
            raise NotImplementedError

        print('tg connect')

    async def disconnect(self):
        print('tg disconnect')
