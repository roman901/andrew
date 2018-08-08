from andrew.api.plugin import AbstractPlugin


class Plugin(AbstractPlugin):
    def __init__(self, andrew):
        self.andrew = andrew

    def post_connect(self):
        connections = self.andrew.connections.connections
        for c in connections:
            connection = self.andrew.connections.connections[c]
            if connection.protocol == 'telegram':
                connection.add_handler('new_chat_member', self.new_member_handler)

    def get_description(self):
        return 'Приветствует вошедших пользователей (только в Telegram-чатах)'

    def is_visible(self):
        return True

    async def new_member_handler(self, connector, chat, message):
        nickname = message['first_name'] if 'first_name' in message else ''
        nickname += ' {}'.format(message['last_name']) if 'last_name' in message else ''
        await chat.send_text('En taro, {}!'.format(nickname))
