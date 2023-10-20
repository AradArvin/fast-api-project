import uuid
from pydantic import BaseModel, Field
from typing import Optional



class Book(BaseModel): 
    _id: str
    title: str = Field()
    pages: int = Field()
    author: str = Field()
    publisher: str = Field()

    class Config:
        populate_by_name = True



class UpdateBook(BaseModel):
    _id: str
    title: str = Optional[str]
    pages: int = Optional[int]
    author: str = Optional[str]
    publisher: str = Optional[str]