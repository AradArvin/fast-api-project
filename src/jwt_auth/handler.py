import jwt
import uuid
from typing import Dict
from decouple import config
from datetime import datetime, timedelta
from bson.objectid import ObjectId

JWT_SECRET = config("JWT_SECRET_KEY")
JWT_ALGORITHM = config("JWT_ALGORITHM")



def token_response(token: str, type: str):
    if type == "access":
        return {
            "access_token": token
        }
    elif type == "refresh":
        return {
            "refresh_token": token
        }



def gen_jti():
    """Generate hexed unique id for user"""
    return str(uuid.uuid4().hex)


jti = gen_jti()




