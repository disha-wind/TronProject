from decimal import Decimal
from typing import Optional

from tronpy.keys import is_base58check_address


class AddressQuery:
    def __init__(self, address: str,
                 balance: Optional[Decimal] = None,
                 bandwidth: Optional[int] = None,
                 energy: Optional[int] = None) -> None:

        if self.__is_tron_address(address):
            self.address = address
        else:
            raise ValueError("Invalid TRON address")

        # Todo: m.b. setters and getters ?
        self.balance = balance
        self.bandwidth = bandwidth
        self.energy = energy

    @staticmethod
    def __is_tron_address(address: str):
        try:
            return is_base58check_address(address)
        except IndexError:
            return False

    def __eq__(self, other):
        if not isinstance(other, AddressQuery):
            return False
        return (self.address == other.address and
                self.balance == other.balance and
                self.bandwidth == other.bandwidth and
                self.energy == other.energy)
