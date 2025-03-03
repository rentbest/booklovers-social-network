from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.session import get_session
from app.schemas.books import Book, BookCreate, BookFilter
from app.crud import books

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=List[Book], response_description="List of books filtered by parameters")
async def read_books(
    db: AsyncSession = Depends(get_session),
    filter: BookFilter = Depends(),
):
    """
    Get a list of books filtered by title, author, year, or description.

    - **title**: Search for books with titles containing the given string.
    - **author**: Search for books with authors containing the given string.
    - **year**: Search for books published in a specific year.
    - **description**: Search for books with descriptions containing the given string.
    """
    return await books.get_books(db=db, **filter.model_dump(exclude_unset=True))


@router.post("/", response_model=Book, response_description="The newly created book")
async def create_new_book(book: BookCreate, db: AsyncSession = Depends(get_session)):
    """
    Create a new book entry.

    - **book**: A `BookCreate` object containing the necessary information to create a new book.
    """
    return await books.create_book(db, book=book)


@router.put(("/{id}/"), response_model=Book, response_description="The updated book")
async def update_book(
    id: int,
    db: AsyncSession = Depends(get_session),
    new_attrs: BookFilter = Depends(),
):
    """
    Update a book's information by its ID.

    - **id**: ID of the book to be updated.
    - **new_attrs**: New attributes for the book (can be title, author, year, or description).
    """
    return await books.update_book_by_id(db=db, id=id, **new_attrs.model_dump(exclude_unset=True))


@router.delete("/", response_model=List[Book], response_description="List of deleted books")
async def delete_books(
    db: AsyncSession = Depends(get_session),
    filter: BookFilter = Depends(),
):
    """
    Delete books that match the given filters.

    - **title**: Delete books with titles containing the given string.
    - **author**: Delete books with authors containing the given string.
    - **year**: Delete books published in a specific year.
    - **description**: Delete books with descriptions containing the given string.
    """
    return await books.delete_books(db=db, **filter.model_dump(exclude_unset=True))
