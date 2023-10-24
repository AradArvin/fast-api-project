from fastapi import APIRouter, Body, status, HTTPException
from fastapi.encoders import jsonable_encoder

from book_library.schemas import *
from book_library.db import MongoDBConnectionManager, ObjectId
from .handler import *


router = APIRouter()


user_collection = MongoDBConnectionManager(database="users", collection="user_data")
jwt_collection = MongoDBConnectionManager(database="jwt_auth", collection="tokens")




@router.post("/signup", response_description="Create a new user account", status_code=status.HTTP_201_CREATED)
async def user_signup(user: User = Body()):
    user = jsonable_encoder(user)

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



