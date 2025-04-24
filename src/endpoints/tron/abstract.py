from abc import abstractmethod
from decimal import Decimal


class AbstractTronClient:

    @abstractmethod
    async def get_balance(self, address: str) -> Decimal:
        pass

    @abstractmethod
    async def get_bandwidth(self, address: str) -> int:
        pass

    @abstractmethod
    async def get_energy(self, address: str) -> int:
        pass
