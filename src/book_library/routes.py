@router.post("/", response_description="Add a new book", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_books(request: Request, book: Book = Body()):
    book = jsonable_encoder(book)
    new_book = collection.insert_one(book)
    created_book = collection.find_one(
        {"_id": new_book.inserted_id}
    )

    return created_book

