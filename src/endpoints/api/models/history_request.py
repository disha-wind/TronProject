from pydantic import BaseModel


class HistoryRequest(BaseModel):
    limit: int
    offset: int
