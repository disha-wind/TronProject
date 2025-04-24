from domain.address_query import AddressQuery
from repositories.abstract import AbstractRepository


class FakeRepository(AbstractRepository):
    def __init__(self, addresses: list[AddressQuery] = None) -> None:
        if addresses is None:
            addresses = []
        self.addresses = addresses

    async def add_address_query(self, address: AddressQuery) -> None:
        self.addresses.append(address)

    async def get_page_addresses(self, limit: int, offset: int) -> list[AddressQuery]:
        return self.addresses[offset:offset + limit]
