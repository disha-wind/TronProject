from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import registry

from domain.address_query import AddressQuery
from orm.table import metadata, address_queries


def start_mappers():
    mapper_registry = registry()
    mapper_registry.map_imperatively(
        AddressQuery,
        address_queries,
        properties={
            'address': address_queries.c.address,
            'balance': address_queries.c.balance,
            'bandwidth': address_queries.c.bandwidth,
            'energy': address_queries.c.energy
        }
    )


async def init_db(async_engine: AsyncEngine):
    async with async_engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
