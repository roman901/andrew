from random import randint
import re
from andrew.api.plugin import AbstractPlugin


class Plugin(AbstractPlugin):
    def __init__(self, andrew):
        super().__init__(andrew)

        self.p = re.compile('^(\d+)[дd](\d+)$', re.IGNORECASE)

    def pre_connect(self):
        self.andrew.filters.add_filter(self.filter_handler)

    def get_description(self):
        return 'Отвечает за разбор дайсов вида 1д6'

    async def filter_handler(self, message):
        m = self.p.match(message.text)
        if m is None:
            return True

        count, val = m.groups()

        count = int(count)
        val = int(val)
        if count > 100:
            await message.send_back('Ты пытаешься бросить слишком много кубиков!')
            return True
        if count == 0 or val == 0:
            await message.send_back('Не пытайся меня сломать!')
            return True

        if val > 100:
            await message.send_back('Слишком много рёбер!')
            return True

        string = '{}д{}: '.format(count, val)
        dice_sum = 0
        for i in range(count):
            rand = randint(1, val)
            string += '\[{}] '.format(rand)
            dice_sum += rand

        string += '| \[{}]'.format(dice_sum)

        await message.send_back(string)
