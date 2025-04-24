from abc import abstractmethod
from decimal import Decimal


class AbstractTronClient:

    @abstractmethod
    async def get_balance(self) -> Decimal:
        pass

    @abstractmethod
    async def get_bandwidth(self) -> int:
        pass

    @abstractmethod
    async def get_energy(self) -> int:
        pass
