from pydantic import BaseModel, Field


class HistoryRequest(BaseModel):
    limit: int = Field(gt=0)
    offset: int = Field(ge=0)
