import pytest

from domain.address_query import AddressQuery


def test_validate_address():
    address_tron = "TE9tcoGmNiWh3Rc3vWQsuh2vxkwLt9Jc2K"
    address = AddressQuery(address_tron)

    assert address.address == address_tron

    with pytest.raises(ValueError):
        AddressQuery("")

    with pytest.raises(ValueError):
        AddressQuery("YE9tcoGmNiWh3Rc3vWQsuh2vxkwLt9Jc2K")
