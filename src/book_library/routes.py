from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder
from .schemas import Book
from .db import collection
# from bson.objectid import ObjectId

router = APIRouter()


@router.post("/", response_description="Add a new book", status_code=status.HTTP_201_CREATED)
async def create_books(book: Book = Body()):
    book = jsonable_encoder(book)

    new_book = collection.insert_one(book)
    created_book = collection.find_one(
        {"_id": new_book.inserted_id}
    )

    return created_book


@router.get("/", response_description="List all books", status_code=status.HTTP_200_OK)
def list_books():
    book_list = list()
    
    books = collection.find()
    
    for book in books:
        book["_id"] = str(book["_id"])
        book_list.append(book)

    return book_list