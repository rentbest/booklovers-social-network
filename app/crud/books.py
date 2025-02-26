from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.models.books import Book
from app.schemas.books import BookCreate


async def get_all_books(db: AsyncSession):
    result = await db.execute(select(Book))
    return result.scalars().all()


async def create_book(db: AsyncSession, book: BookCreate):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book
