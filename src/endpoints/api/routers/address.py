from fastapi import APIRouter

from endpoints.api.models.address_request import AddressRequest
from endpoints.tron import tron
from endpoints.tron.tronpy import TronClient
from service.fill_data import fill_data_from_tron_net
from uow.sql_alchemy import SqlAlchemyUnitOfWork

router = APIRouter()


@router.post("/address")
async def create_address(request: AddressRequest):
    uow = SqlAlchemyUnitOfWork()
    client = TronClient(tron, request.address)

    balance, bandwidth, energy = await fill_data_from_tron_net(uow, client, request.address)

    return {
        "address": request.address,
        "balance": balance,
        "bandwidth": bandwidth,
        "energy": energy,
    }
