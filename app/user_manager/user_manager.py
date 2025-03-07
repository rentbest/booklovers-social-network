from fastapi import Depends
from fastapi_users import BaseUserManager, IntegerIDMixin

from app.db.models.users import User
from app.auth.database import get_user_db
from app.core.config import settings


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.SECRET
    verification_token_secret = settings.SECRET


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)