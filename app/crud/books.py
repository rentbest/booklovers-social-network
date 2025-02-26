from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from app.db.models.books import Book
from app.schemas.books import BookCreate


async def get_books(db: AsyncSession, **params):
    query = select(Book)

    if params.get("title"):
        query = query.filter(Book.title.ilike(f"%{params['title']}%"))
    if params.get("author"):
        query = query.filter(Book.author.ilike(f"%{params['author']}%"))
    if params.get("year"):
        query = query.filter(Book.year == params['year'])
    if params.get("description"):
        query = query.filter(Book.description.ilike(
            f"%{params['description']}%"))

    result = await db.execute(query)
    return result.scalars().all()


def is_params_not_none(params) -> bool:
    for value in params.values():
        if value:
            return True
    return False


async def update_book_by_id(db: AsyncSession, id: int, **params):
    # If not parameters provided, then nothing to update
    if not is_params_not_none(params=params):
        raise HTTPException(
            status_code=400,
            detail="At least one parameter must be provided to update book",
        )
    
    book_to_update = await db.execute(select(Book).where(Book.id == id))
    book_to_update = book_to_update.scalars().first()

    if not book_to_update:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )
    
    for key, value in params.items():
        if value:
            setattr(book_to_update, key, value)

    await db.commit()
    await db.refresh(book_to_update)
    return book_to_update


async def delete_books(db: AsyncSession, **params):
    # If not parameters provided, then nothing to delete
    if not is_params_not_none(params=params):
        raise HTTPException(
            status_code=400,
            detail="At least one parameter must be provided to delete books.",
        )

    query = select(Book).filter_by(
        **{key: value for key, value in params.items() if value})
    result = await db.execute(query)
    books_to_delete = result.scalars().all()

    if not books_to_delete:
        return []

    for book in books_to_delete:
        await db.delete(book)

    await db.commit()
    return books_to_delete


async def create_book(db: AsyncSession, book: BookCreate):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book
