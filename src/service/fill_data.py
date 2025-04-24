from decimal import Decimal

from domain.address_query import AddressQuery
from endpoints.tron.abstract import AbstractTronClient
from uow.abstract import AbstractUnitOfWork


async def fill_data_from_tron_net(uow: AbstractUnitOfWork, client: AbstractTronClient, address: str)\
        -> (Decimal, int, int):
    address_query = AddressQuery(address)

    with uow:
        address_query.balance = await client.get_balance(address)
        address_query.bandwidth = await client.get_bandwidth(address)
        address_query.energy = await client.get_energy(address)
        await uow.commit()

    return address_query.balance, address_query.bandwidth, address_query.energy
