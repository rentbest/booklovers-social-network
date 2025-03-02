from sqlalchemy import Column, String
from fastapi_users.db import SQLAlchemyBaseOAuthAccountTable

from app.db.base import Base


class User(Base, SQLAlchemyBaseOAuthAccountTable[int]):
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
