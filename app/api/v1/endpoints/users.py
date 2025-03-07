from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from app.db.models.users import User
from app.user_manager.user_manager import get_user_manager
from app.schemas.users import UserRead, UserUpdate
from app.auth.auth_backend import auth_backend


fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

user_router = APIRouter(prefix="/users", tags=["Users"])
user_router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))
