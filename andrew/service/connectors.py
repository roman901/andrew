from typing import List
from abc import ABCMeta, abstractmethod

from andrew.service import Service


class Connector(metaclass=ABCMeta):
    @abstractmethod
    async def connect(self):
        raise NotImplementedError

    async def disconnect(self):
        raise NotImplementedError


class ConnectorsService(Service):
    connectors: List[Connector] = []

    async def connect(self):
        for c in self.connectors:
            await c.connect()

    async def disconnect(self):
        for c in self.connectors:
            await c.disconnect()


def register_connector(connector):
    connectors = ConnectorsService()
    connectors.connectors.append(connector())
    return connector
