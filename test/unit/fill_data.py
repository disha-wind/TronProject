from decimal import Decimal

from domain.address_query import AddressQuery
from fake.repo import FakeRepository
from fake.tron import FakeTronClient
from fake.unit_of_work import FakeUnitOfWork

from service.fill_data import fill_data_from_tron_net


async def test_fill_data_from_tron_net():
    repo = FakeRepository()
    uow = FakeUnitOfWork(repo)
    client = FakeTronClient(Decimal(100), 5, 23)
    address = "TCMssXEMmn4z6Y2JaKC419jjdguKMao2MR"

    balance, bandwidth, energy = await fill_data_from_tron_net(uow, client, address)

    assert balance == client.balance
    assert bandwidth == client.bandwidth
    assert energy == client.energy

    assert uow.addresses.addresses == [
        AddressQuery(address, Decimal(100), 5, 23)
    ]

    assert uow.commited is True
