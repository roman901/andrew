from abc import ABCMeta, abstractmethod


class Plugin(metaclass=ABCMeta):

    @abstractmethod
    async def load(self):
        pass

    @abstractmethod
    async def unload(self):
        pass
