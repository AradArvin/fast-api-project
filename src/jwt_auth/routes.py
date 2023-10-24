from fastapi import APIRouter, Body, status, HTTPException
from fastapi.encoders import jsonable_encoder

from book_library.schemas import *
from book_library.db import MongoDBConnectionManager, ObjectId
from .handler import *


router = APIRouter()


user_collection = MongoDBConnectionManager(database="users", collection="user_data")
jwt_collection = MongoDBConnectionManager(database="jwt_auth", collection="tokens")

