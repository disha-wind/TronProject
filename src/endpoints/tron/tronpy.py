from _decimal import Decimal

from tronpy import Tron
from tronpy.exceptions import AddressNotFound

from endpoints.tron.abstract import AbstractTronClient
from exaption.tron import TronAddressNotFound


class TronClient(AbstractTronClient):

    def __init__(self, client: Tron) -> None:

        self.client = client
        self.account = None

    async def load_account(self, address: str) -> None:
        try:
            self.account = self.client.get_account(address)
        except AddressNotFound:
            raise TronAddressNotFound(address)

    async def get_balance(self) -> Decimal:
        """Get TRX balance for the given TRON address.

        Returns:
            Balance in TRX as Decimal
        """
        return self.account.get("balance")

    async def get_bandwidth(self) -> int:
        """Get bandwidth information for the given TRON address.

        Returns:
            Available bandwidth as integer
        """
        return self.account.get("net_usage", 0)

    async def get_energy(self) -> int:
        """Get energy information for the given TRON address.

        Returns:
            Available energy as integer
        """
        return self.account.get("energy_usage", 0)

    def is_exist_address(self, address: str) -> bool:
        try:
            self.client.get_account(address)
            return True
        except AddressNotFound:
            return False
