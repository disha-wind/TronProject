from abc import ABC, abstractmethod

from repositories.abstract import AbstractRepository


class AbstractUnitOfWork(ABC):
    addresses: AbstractRepository

    @abstractmethod
    async def commit(self) -> None:
        pass

    @abstractmethod
    async def rollback(self) -> None:
        pass

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
