from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.fields import ModelField
from pydantic.typing import is_union, get_origin, get_args

from src.operations.models import operation


class OperationCreate(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str


class OperationRead(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str

    class Config:
        orm_mode = True
