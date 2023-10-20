from pymongo import MongoClient
# from pydantic import BaseModel



client = MongoClient("mongodb://localhost:27017/")
db = client.book_library
collection = db.q_search

