from pymongo import MongoClient
from pydantic import BaseModel
from bson.objectid import ObjectId



class MongoDBConnectionManager:

    HOST_ADDRESS = "mongodb://localhost:27017/"


    def __init__(self, database: str, collection: str) -> None:
        self.client = MongoClient(self.HOST_ADDRESS)
        self.database = self.client[database]
        self.collection = self.database[collection]
    

