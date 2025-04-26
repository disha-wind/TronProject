from _decimal import Decimal

from tronpy import Tron
from tronpy.exceptions import AddressNotFound

from endpoints.tron.abstract import AbstractTronClient


class TronClient(AbstractTronClient):

    def __init__(self, client: Tron, address: str) -> None:
        self.client = client
        try:
            self.account = client.get_account(address)
        except AddressNotFound:
            raise AddressNotFound

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
