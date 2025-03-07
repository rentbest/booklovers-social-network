from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from app.db.models.users import User
from app.user_manager.user_manager import get_user_manager
from app.auth.auth_backend import auth_backend
from app.schemas.users import UserRead, UserCreate


fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

auth_router.include_router(fastapi_users.get_auth_router(auth_backend))
auth_router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
auth_router.include_router(fastapi_users.get_verify_router(UserRead))
auth_router.include_router(fastapi_users.get_reset_password_router())
