from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class ItemSchema(BaseModel):
    id: Optional[int] = None
    dataset_id: Optional[int] = None
    _data: Optional[str]=None
    geometry: Optional[bytes]=None
    dataset: Optional["DataSetSchema"] = None

    class Config:
        orm_mode = True


class DataSetSchema(BaseModel):
    id: int
    name: Optional[str] = None
    owner: Optional[str] = None
    items: List[ItemSchema] = []
    
    class Config:
        orm_mode = True


class RequestItem(BaseModel):
    parameter: ItemSchema = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
