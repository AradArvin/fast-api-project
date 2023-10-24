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



def access_token_gen(user_id: ObjectId):
    """Generate access token based on usser id."""

    access_token = token_encode({
        'token_type':'access',
        'user_id':str(user_id),
        'exp': datetime.utcnow() + timedelta(minutes=10),
        'iat': datetime.utcnow(),
        'jti':jti
    })

    return access_token




