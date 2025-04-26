from fastapi import APIRouter

from endpoints.api.models.history_request import HistoryRequest
from service.history import get_history_with_pagination
from uow.sql_alchemy import SqlAlchemyUnitOfWork

router = APIRouter()


@router.get("/history")
async def get_history(request: HistoryRequest):
    uow = SqlAlchemyUnitOfWork()

    history = await get_history_with_pagination(uow, request.limit, request.offset)

    return history
