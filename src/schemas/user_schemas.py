from pydantic import BaseModel, Field, EmailStr



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


