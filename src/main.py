from fastapi import FastAPI
from book_library.routes import router as book_router


app = FastAPI()

app.include_router(book_router, tags=["books"], prefix="/book")

