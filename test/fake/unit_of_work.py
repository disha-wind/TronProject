from fake.repo import FakeRepository
from uow.abstract import AbstractUnitOfWork


class FakeUnitOfWork(AbstractUnitOfWork):
    addresses: FakeRepository

    def __init__(self, addresses: FakeRepository):
        self.addresses = addresses
        self.commited = False

    async def commit(self):
        self.commited = True

    async def rollback(self):
        self.commited = False
