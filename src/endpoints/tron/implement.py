from _decimal import Decimal

from tronpy import Tron
from tronpy.exceptions import AddressNotFound

from endpoints.tron.abstract import AbstractTronClient


class TronClient(AbstractTronClient):

    def __init__(self, client: Tron):
        self.client = client

    async def get_balance(self, address: str) -> Decimal:
        """Get TRX balance for the given TRON address.

        Args:
            address: TRON address to check balance for

        Returns:
            Balance in TRX as Decimal
        """
        balance = self.client.get_account_balance(address)
        return Decimal(str(balance))

    async def get_bandwidth(self, address: str) -> int:
        """Get bandwidth information for the given TRON address.

        Args:
            address: TRON address to check bandwidth for

        Returns:
            Available bandwidth as integer
        """
        account = self.client.get_account(address)
        return account.get("net_usage", 0)

    async def get_energy(self, address: str) -> int:
        """Get energy information for the given TRON address.

        Args:
            address: TRON address to check energy for

        Returns:
            Available energy as integer
        """
        account = self.client.get_account(address)
        return account.get("energy_usage", 0)

    def is_exist_address(self, address: str) -> bool:
        try:
            self.client.get_account(address)
            return True
        except AddressNotFound:
            return False
