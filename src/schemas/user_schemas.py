from pydantic import BaseModel, Field, EmailStr
from typing import Optional


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



class UserProfile(BaseModel):
    _id: str
    email: EmailStr = Field()
    password: str = Field()


class UpdateProfile(BaseModel):
    _id: str
    username: str = Optional[str]
    email: EmailStr = Optional[str]
    password: str = Optional[int]



class AuthJWT(BaseModel):
    token: str = Field()