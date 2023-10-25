from fastapi import APIRouter, Body, status, HTTPException
from fastapi.encoders import jsonable_encoder

from book_library.schemas import *
from book_library.db import MongoDBConnectionManager, ObjectId
from .handler import *


router = APIRouter()


user_collection = MongoDBConnectionManager(database="users", collection="user_data")
jwt_collection = MongoDBConnectionManager(database="jwt_auth", collection="tokens")

# jwt_collection.set_index("expireAt")



@router.post("/signup", response_description="Create a new user account", status_code=status.HTTP_201_CREATED)
async def user_signup(user: User = Body()):
    user = jsonable_encoder(user)
    all_users = user_collection.get_data_from_db_collection()
    for data in all_users:
        if data["email"] == user["email"]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already exists!")
        
    new_user = user_collection.save_data_to_db_collection(instance=user)

    access_token = access_token_gen(new_user.inserted_id)
    refresh_token = refresh_token_gen(new_user.inserted_id)

    refresh_dict = {
        "user_id": str(new_user.inserted_id),
        "refresh_token": refresh_token,
        }
    json_encoded_refresh = jsonable_encoder(refresh_dict)
    jwt_collection.save_data_to_db_collection(instance=json_encoded_refresh)
   
    return token_response(access_token, "access")




def check_user(data: UserLogin):
    users = user_collection.get_data_from_db_collection()

    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False



@router.post("/login", response_description="Login to you'r user account using email & password", status_code=status.HTTP_200_OK)
async def user_login(user: UserLogin = Body()):
    if check_user(user):
        access_token = access_token_gen(user._id)
        refresh_token = refresh_token_gen(user._id)

        refresh_dict = {
            "user_id": str(user._id),
            "refresh_token": refresh_token,
            }
        json_encoded_refresh = jsonable_encoder(refresh_dict)
        jwt_collection.save_data_to_db_collection(instance=json_encoded_refresh)

        return token_response(access_token, "access")
    return {
        "error": "Wrong login Data!",
    }