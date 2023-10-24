import jwt
import uuid
from typing import Dict
from decouple import config
from datetime import datetime, timedelta
from bson.objectid import ObjectId

JWT_SECRET = config("JWT_SECRET_KEY")
JWT_ALGORITHM = config("JWT_ALGORITHM")


