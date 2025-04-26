from orm import async_session
from repositories.sql_alchemy import SqlAlchemyRepository
from uow.abstract import AbstractUnitOfWork


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):

    def __init__(self):
        self._session = async_session()
        self.addresses = SqlAlchemyRepository(self._session)

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
