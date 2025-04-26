from decimal import Decimal

from domain.address_query import AddressQuery
from endpoints.tron.abstract import AbstractTronClient
from uow.abstract import AbstractUnitOfWork


async def fill_data_from_tron_net(uow: AbstractUnitOfWork, client: AbstractTronClient, address: str)\
        -> (Decimal, int, int):
    address_query = AddressQuery(address)
    balance = await client.get_balance()
    bandwidth = await client.get_bandwidth()
    energy = await client.get_energy()

    async with uow:
        address_query.balance = balance
        address_query.bandwidth = bandwidth
        address_query.energy = energy
        await uow.addresses.add_address_query(address_query)
        await uow.commit()

    return balance, balance, energy
