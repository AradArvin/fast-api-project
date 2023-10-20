from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from .schemas import Book
from typing import List
from .db import collection

router = APIRouter()


@router.post("/", response_description="Add a new book", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_books(request: Request, book: Book = Body()):
    book = jsonable_encoder(book)
    new_book = collection.insert_one(book)
    created_book = collection.find_one(
        {"_id": new_book.inserted_id}
    )

    return created_book


@router.get("/", response_description="List all books", status_code=status.HTTP_200_OK, response_model=List[Book])
def list_books(request: Request):
    books = list(collection.find())
    return books