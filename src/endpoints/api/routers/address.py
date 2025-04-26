from fastapi import APIRouter, HTTPException

from endpoints.api.models.address_request import AddressRequest
from endpoints.tron import tron
from endpoints.tron.tronpy import TronClient
from exaption.tron import TronAddressNotFound, TronAddressIncorrectFormat
from service.fill_data import fill_data_from_tron_net
from uow.sql_alchemy import SqlAlchemyUnitOfWork

router = APIRouter()


@router.post("/address")
async def get_address(request: AddressRequest):
    uow = SqlAlchemyUnitOfWork()
    client = TronClient(tron)

    try:
        balance, bandwidth, energy = await fill_data_from_tron_net(uow, client, request.address)
    except TronAddressIncorrectFormat as e:
        raise HTTPException(status_code=400, detail=str(e))
    except TronAddressNotFound as e:
        return HTTPException(status_code=404, detail=str(e))

    return {
        "address": request.address,
        "balance": balance,
        "bandwidth": bandwidth,
        "energy": energy,
    }
