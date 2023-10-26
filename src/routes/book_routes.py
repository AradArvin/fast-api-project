from fastapi import APIRouter, Body, status, HTTPException
from fastapi.encoders import jsonable_encoder

from schemas.book_schemas import *
from db.mongodb import MongoDBConnectionManager, ObjectId


collection = MongoDBConnectionManager(database="book_library", collection="q_search")

book_router = APIRouter()

# response_model

@book_router.post("/create", response_description="Add a new book to library", status_code=status.HTTP_201_CREATED)
async def create_a_book(book: Book = Body()):
    book = jsonable_encoder(book)
    new_book = collection.save_data_to_db_collection(instance=book)

    created_book = collection.find_data_by_id(new_book.inserted_id)
    
    return created_book



@book_router.get("/list", response_description="List all books in the library", status_code=status.HTTP_200_OK)
async def see_the_list_of_books():
    book_list = await collection.get_data_from_db_collection()

    return book_list



@book_router.delete("/del", response_description="Delete a book from library", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id: str):
    result = collection.delete_data_from_db_collection(ObjectId(book_id))
    
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book with this id does not exist!")
    


@book_router.get("/find", response_description="Find a book in the library.", status_code=status.HTTP_200_OK)
async def find_a_book(book_id: str):
    result = collection.find_data_by_id(ObjectId(book_id))
    
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book with this id does not exist!")
    
    return result



@book_router.put("/update", response_description="Update a books data in the library.", status_code=status.HTTP_201_CREATED)
async def update_a_book(book_id: str, book: UpdateBook = Body()):
    find_book = collection.find_data_by_id(ObjectId(book_id))
    
    if find_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book with this id does not exist!")
    
    book = {k: v for k, v in dict(book).items() if v if not None}

    if len(book) >= 1:
        result = collection.update_db_collection_data(instance_id=ObjectId(book_id), updated_instance=book)
        
        if result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No changes detected!")
        
        updated_book = collection.find_data_by_id(ObjectId(book_id))
        return updated_book
        
    