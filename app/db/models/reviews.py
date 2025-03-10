from sqlalchemy import Column, Integer, Text, ForeignKey

from app.db.base import Base


class Review(Base):
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer, nullable=False)
    text = Column(Text, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
