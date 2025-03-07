from sqlalchemy import Column, String, Boolean
from fastapi_users.db import SQLAlchemyBaseUserTable
from app.db.base import Base


class User(Base, SQLAlchemyBaseUserTable[int]):
    username = Column(String, unique=True, nullable=False)
    is_admin = Column(Boolean, default=False)
    email = Column(String, unique=True, nullable=False) 
    hashed_password = Column(String, nullable=False)