from abc import ABC, abstractmethod

from domain.address_query import AddressQuery


class AbstractRepository(ABC):

    @abstractmethod
    async def add_address_query(self, address: AddressQuery) -> None:
        pass

    @abstractmethod
    async def get_page_addresses(self, limit: int, offset: int) -> list[AddressQuery]:
        pass
