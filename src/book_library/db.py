from pymongo import MongoClient
# from pydantic import BaseModel



client = MongoClient("mongodb://localhost:27017/")
db = client.book_library
collection = db.q_search


# class MongoManager:
#     HOST = "localhost"
#     PORT = 27017
    

#     def __init__(self, database: str) -> None:
#         self.client = MongoClient(host=self.HOST, port=self.PORT)
#         self.database = self.client(database)

    
#     def add_collection(self, name, )