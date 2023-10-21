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



@router.get("/list", response_description="List all books in the library", status_code=status.HTTP_200_OK)
async def see_the_list_of_books():
    book_list = collection.get_data_from_db_collection()

    return book_list



@router.delete("/del", response_description="Delete a book from library", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id: str):
    result = collection.delete_data_from_db_collection(ObjectId(book_id))
    
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book with this id does not exist!")
    

