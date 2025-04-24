from fastapi import APIRouter

from endpoints.api.models.history_request import HistoryRequest

router = APIRouter()


@router.post("/history")
async def get_history(request: HistoryRequest):
    pass
