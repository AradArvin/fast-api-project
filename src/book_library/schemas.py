
from pydantic import BaseModel, Field, EmailStr
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




class User(BaseModel):
    _id: str
    username: str = Field()
    email: EmailStr = Field()
    password: str = Field()

    class Config:
        populate_by_name = True


class UserLogin(BaseModel):
    _id: str
    email: EmailStr = Field()
    password: str = Field()
