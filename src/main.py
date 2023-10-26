from fastapi import FastAPI
from routes.book_routes import book_router
from routes.user_routes import user_router


app = FastAPI()

app.include_router(book_router, tags=["books"], prefix="/book")
app.include_router(user_router, tags=["users"], prefix="/user")

