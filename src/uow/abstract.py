from abc import ABC, abstractmethod

from repositories.abstract import AbstractRepository


class AbstractUnitOfWork(ABC):
    addresses: AbstractRepository

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.rollback()
