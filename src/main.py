from fastapi import FastAPI
from book_library.routes import router as book_router
from jwt_auth.routes import router as user_router


app = FastAPI()

app.include_router(book_router, tags=["books"], prefix="/book")
app.include_router(user_router, tags=["users"], prefix="/user")

