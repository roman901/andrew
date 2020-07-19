from abc import ABCMeta, abstractmethod


class Plugin(metaclass=ABCMeta):
    async def load(self):
        pass

    async def unload(self):
        pass

    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_author(self) -> str:
        raise NotImplementedError
