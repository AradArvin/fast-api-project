import uuid
from pydantic import BaseModel, Field
from typing import Optional



class Book(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field()
    pages: int = Field()
    author: str = Field()

    class Config:
        allow_population_by_field_name = True



class UpdateBook(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field()
    pages: int = Field()
    author: str = Field()