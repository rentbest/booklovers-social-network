from sqlalchemy import Column, Integer, String

from app.db.base import Base


class User(Base):
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
