from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from domain.address_query import AddressQuery
from repositories.abstract import AbstractRepository


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_address_query(self, address: AddressQuery) -> None:
        self.session.add(address)

    async def get_page_addresses(self, limit: int, offset: int) -> list[AddressQuery]:
        result = await self.session.execute(
            select(AddressQuery)
            .limit(limit)
            .offset(offset)
        )
        return list(result.scalars().all())
