from tronpy.keys import is_base58check_address


class AddressQuery:
    def __init__(self, address: str):

        if self.is_tron_address(address):
            self.address = address
        else:
            raise ValueError("Invalid TRON address")

        self.balance: float | None = None
        self.bandwidth: int | None = None
        self.energy: int | None = None

    @staticmethod
    def is_tron_address(address: str):
        return is_base58check_address(address)
