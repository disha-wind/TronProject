from decimal import Decimal

import pytest
from tronpy import Tron

from endpoints.tron.implement import TronClient


@pytest.fixture
def tron():
    return Tron(network='nile')


@pytest.fixture
def tron_client(tron):
    return TronClient(tron)


@pytest.fixture
def address():
    return "TKDC6hVMnuFBWLsS8EL3PU44yLFrRnXMbC"


def test_is_exist_address(tron_client, address: str):
    assert tron_client.is_exist_address(address) is True
    assert tron_client.is_exist_address("THntTu3nEqF4Z89ieXg2ERvBL7rKphtNPZ") is False


async def test_get_tron_balance(tron_client, address: str):
    balance = await tron_client.get_balance(address)

    assert balance == Decimal(0)


async def test_get_tron_bandwidth(tron_client, address: str):
    bandwidth = await tron_client.get_bandwidth(address)

    assert bandwidth == 0


async def test_get_tron_energy(tron_client, address: str):
    energy = await tron_client.get_energy(address)

    assert energy == 0