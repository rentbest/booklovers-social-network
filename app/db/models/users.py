from typing import TYPE_CHECKING
from sqlalchemy import Column, String
from fastapi_users.db import SQLAlchemyBaseOAuthAccountTable, SQLAlchemyUserDatabase

from app.db.base import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, SQLAlchemyBaseOAuthAccountTable[int]):
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)