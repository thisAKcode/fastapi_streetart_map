from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel  

T = TypeVar('T')

class ArtItemSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str]=None
    lat: Optional[float] = None
    lon: Optional[float] = None
    image_one: Optional[bytes] = None
    image_two: Optional[str] = None

    class Config:
        orm_mode = True

class RequestArtItem(BaseModel):
    parameter: ArtItemSchema = Field(...)

class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
