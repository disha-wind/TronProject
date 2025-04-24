from _decimal import Decimal

from endpoints.tron.abstract import AbstractTronClient


class FakeTronClient(AbstractTronClient):
    def __init__(self, balance: Decimal, bandwidth: int, energy: int):
        self.balance = balance
        self.bandwidth = bandwidth
        self.energy = energy

    async def get_balance(self) -> Decimal:
        return self.balance

    async def get_bandwidth(self) -> int:
        return self.bandwidth

    async def get_energy(self) -> int:
        return self.energy
