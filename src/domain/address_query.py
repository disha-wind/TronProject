from decimal import Decimal
from typing import Optional

from tronpy.keys import is_base58check_address


class AddressQuery:
    def __init__(self, address: str):

        if self.__is_tron_address(address):
            self.address = address
        else:
            raise ValueError("Invalid TRON address")

        # Todo: m.b. setters and getters ?
        self.balance: Optional[Decimal] = None
        self.bandwidth: Optional[int] = None
        self.energy: Optional[int] = None

    @staticmethod
    def __is_tron_address(address: str):
        try:
            return is_base58check_address(address)
        except IndexError:
            return False
