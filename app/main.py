from fastapi import FastAPI

from app.api.v1.endpoints.books import router as books_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, wolrd!"}

app.include_router(books_router, prefix="/api/v1")
