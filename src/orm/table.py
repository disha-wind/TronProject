from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, Numeric, func

metadata = MetaData()

address_queries = Table(
    "address_query", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("address", String, nullable=False),
    Column("timestamp", DateTime, server_default=func.now(), nullable=False),
    Column("balance", Numeric, nullable=True),
    Column("bandwidth", Integer, nullable=True),
    Column("energy", Integer, nullable=True),
)
