from fastapi import FastAPI

from app.api.v1.endpoints.books import router as books_router
from app.api.v1.endpoints.reviews import router as reviews_router
from app.api.v1.endpoints.users import router as users_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, wolrd!"}

app.include_router(books_router, prefix="/api/v1")
app.include_router(reviews_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")
