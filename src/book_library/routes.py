from fastapi import APIRouter, Body, status, HTTPException
from fastapi.encoders import jsonable_encoder

from .schemas import Book, UpdateBook
from .db import MongoDBConnectionManager, ObjectId


collection = MongoDBConnectionManager(database="book_library", collection="q_search")

router = APIRouter()



@router.post("/create", response_description="Add a new book to library", status_code=status.HTTP_201_CREATED)
async def create_a_book(book: Book = Body()):
    book = jsonable_encoder(book)
    new_book = collection.save_data_to_db_collection(instance=book)

    created_book = collection.find_data_by_id(new_book.inserted_id)
    
    return created_book



@router.get("/", response_description="List all books", status_code=status.HTTP_200_OK)
def list_books():
    book_list = list()
    
    books = collection.find()
    
    for book in books:
        book["_id"] = str(book["_id"])
        book_list.append(book)

    return book_list