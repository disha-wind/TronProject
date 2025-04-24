from decimal import Decimal

import pytest
from tronpy import Tron

from endpoints.tron import get_tron_balance
from endpoints.tron import get_tron_bandwidth
from endpoints.tron import get_tron_energy


@pytest.fixture
def client():
    return Tron(network='nile')


@pytest.fixture
def address():
    return "TKDC6hVMnuFBWLsS8EL3PU44yLFrRnXMbC"


async def test_get_tron_balance(client: Tron, address: str):
    balance = await get_tron_balance(client, address)

    assert balance == Decimal(0)


async def test_get_tron_bandwidth(client: Tron, address: str):
    bandwidth = await get_tron_bandwidth(client, address)

    assert bandwidth == 0


async def test_get_tron_energy(client: Tron, address: str):
    energy = await get_tron_energy(client, address)

    assert energy == 0
