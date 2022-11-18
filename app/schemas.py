from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class DataSetSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    items: List["ItemSchema"] = []


class ItemSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    description: Optional[str]=None
    image_one: Optional[bytes] = None
    image_two: Optional[str] = None

    class Config:
        orm_mode = True

class RequestItem(BaseModel):
    parameter: ItemSchema = Field(...)

class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
