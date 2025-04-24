from tronpy import Tron
from decimal import Decimal


async def get_tron_balance(client: Tron, address: str) -> Decimal:
    """Get TRX balance for the given TRON address.

    Args:
        client: Tron client instance
        address: TRON address to check balance for

    Returns:
        Balance in TRX as Decimal
    """
    balance = client.get_account_balance(address)
    return Decimal(str(balance))


async def get_tron_bandwidth(client: Tron, address: str) -> int:
    """Get bandwidth information for the given TRON address.

    Args:
        client: Tron client instance
        address: TRON address to check bandwidth for

    Returns:
        Available bandwidth as integer
    """
    account = client.get_account(address)
    return account.get("net_usage", 0)


async def get_tron_energy(client: Tron, address: str) -> int:
    """Get energy information for the given TRON address.

    Args:
        client: Tron client instance
        address: TRON address to check energy for

    Returns:
        Available energy as integer
    """
    account = client.get_account(address)
    return account.get("energy_usage", 0)
