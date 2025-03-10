from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from app.utils.utc_now import utc_now
from app.db.base import Base


class BaseComment(Base):
    __abstract__ = True

    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=utc_now)
    updated_at = Column(DateTime, default=utc_now, onupdate=utc_now)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


class BookComment(BaseComment):
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)


class ReviewComment(BaseComment):
    review_id = Column(Integer, ForeignKey("reviews.id"), nullable=False)
