class TronAddressIncorrectFormat(Exception):
    def __init__(self):
        super().__init__("Tron address has incorrect format")


class TronAddressNotFound(Exception):
    def __init__(self, address):
        super().__init__(f'Tron address {address} not found')
