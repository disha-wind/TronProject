from fastapi import APIRouter

from endpoints.api.models.address_request import AddressRequest

router = APIRouter()


@router.post("/address")
async def create_address(request: AddressRequest):
    pass
