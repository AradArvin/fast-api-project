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
        'exp': datetime.utcnow() + timedelta(seconds=30),
        'iat': datetime.utcnow(),
        'jti':jti
    })

    return access_token



def refresh_token_gen(user_id: ObjectId):
    """Generate refresh token based on usser id."""

    refresh_token = token_encode({
        'token_type':'refresh',
        'user_id':str(user_id),
        'exp': datetime.utcnow() + timedelta(minutes=1),
        'iat': datetime.utcnow(),
        'jti':jti
    })
    
    return refresh_token



def token_encode(payload):
    """Encode tokens based on HS256 algorithm"""

    token = jwt.encode(payload=payload, key=JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token




def token_decode(token):
    """Dencode tokens based on HS256 algorithm"""

    payload = jwt.decode(jwt=token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return payload


