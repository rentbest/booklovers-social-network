from fastapi import FastAPI

from app.api.v1.endpoints.books import router as books_router
from app.api.v1.endpoints.reviews import router as reviews_router
from app.api.v1.endpoints.users import user_router as users_router
from app.api.v1.endpoints.auth import auth_router

app = FastAPI(
    openapi_tags=[
        {
            "name": "Auth",
            "description": "Operations with authentication: login, register, verify, reset password.",
        },
        {
            "name": "Users",
            "description": "Operations with users: get, update, delete.",
        },
    ],
    prefix="/api/v1"
)


@app.get("/")
async def root():
    return {"message": "Hello, wolrd!"}

app.include_router(books_router)
app.include_router(reviews_router)
app.include_router(users_router)
app.include_router(auth_router)
