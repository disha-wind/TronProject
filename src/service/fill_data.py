from tronpy import Tron

from domain.address_query import AddressQuery
from endpoints.tron import get_tron_balance, get_tron_bandwidth, get_tron_energy


async def fill_data_from_tron_net(client: Tron, address: str) -> None:
    address_query = AddressQuery(address)

    address_query.balance = await get_tron_balance(client, address_query.address)
    address_query.bandwidth = await get_tron_bandwidth(client, address_query.address)
    address_query.energy = await get_tron_energy(client, address_query.address)
