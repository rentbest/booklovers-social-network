from sqlalchemy import Column, Integer, String, Text

from app.db.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    year = Column(Integer, nullable=True)
