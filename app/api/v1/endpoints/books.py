from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.session import get_session
from app.schemas.books import Book, BookCreate
from app.crud import books

router = APIRouter()

@router.get("/books/", response_model=List[Book])
async def read_books(db: AsyncSession = Depends(get_session)):
    book_list = await books.get_all_books(db=db)
    return book_list

@router.post("/books/", response_model=Book)
async def create_new_book(book: BookCreate, db: AsyncSession = Depends(get_session)):
    return await books.create_book(db, book=book)

