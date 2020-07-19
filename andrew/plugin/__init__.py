from abc import ABCMeta, abstractmethod


class Plugin(metaclass=ABCMeta):
    def load(self):
        pass

    def unload(self):
        pass

    async def pre_connect(self):
        pass

    async def post_connect(self):
        pass

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_author(self) -> str:
        raise NotImplementedError
