from typing import Any

from uow.abstract import AbstractUnitOfWork


async def get_history_with_pagination(uow: AbstractUnitOfWork, limit: int, offset: int) -> list[dict[str, Any]]:
    async with uow:
        history = await uow.addresses.get_page_addresses(limit, offset)

    response = []
    for address_query in history:
        response.append(address_query.to_json())

    return response
