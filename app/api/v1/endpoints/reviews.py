from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.session import get_session
from app.schemas.reviews import ReviewCreate, ReviewFilter, Review
from app.crud import reviews

router = APIRouter(tags=["Reviews"])


@router.get("/reviews/", response_model=List[Review], response_description="List of reviews filtered by parameters")
async def read_reviews(
    db: AsyncSession = Depends(get_session),
    filter: ReviewFilter = Depends(),
):
    """
    Get a list of reviews filtered by rating, user, or book_id.
    """
    return await reviews.get_reviews(db=db, **filter.model_dump(exclude_unset=True))


@router.get("/books/{book_id}/reviews/", response_model=List[Review], response_description="List of reviews for a specific book")
async def get_reviews_for_book(
    book_id: int,
    db: AsyncSession = Depends(get_session)
):
    """
    Get all reviews for a specific book by its ID.
    """
    return await reviews.get_reviews(db=db, book_id=book_id)


@router.post("/reviews/", response_model=Review, response_description="The newly created review")
async def create_new_review(
    review: ReviewCreate,
    db: AsyncSession = Depends(get_session)
):
    """
    Create a new review.

    - **review**: A `ReviewCreate` object containing the necessary information to create a new review.
    """
    return await reviews.create_review(db, review=review)


@router.post("/books/{book_id}/reviews/", response_model=Review, response_description="Create a review for a specific book")
async def create_review_for_book(
    book_id: int,
    review: ReviewCreate,
    db: AsyncSession = Depends(get_session)
):
    """
    Create a new review for a specific book.

    - **book_id**: The ID of the book to which the review belongs.
    - **review**: A `ReviewCreate` object with review details.
    """
    return await reviews.create_review(db, review=review, book_id=book_id)


@router.put("/reviews/{id}/", response_model=Review, response_description="The updated review")
async def update_review(
    id: int,
    new_attrs: ReviewFilter = Depends(),
    db: AsyncSession = Depends(get_session)
):
    """
    Update a review by its ID.

    - **id**: ID of the review to update.
    - **new_attrs**: Fields to update (e.g., rating, comment).
    """
    return await reviews.update_review_by_id(db=db, id=id, **new_attrs.model_dump(exclude_unset=True))


@router.delete("/reviews/{id}/", response_model=Review, response_description="The deleted review")
async def delete_review(
    id: int,
    db: AsyncSession = Depends(get_session),
):
    """
    Delete a review by its ID.

    - **id**: ID of the review to delete.
    """
    return await reviews.delete_review_by_id(db=db, id=id)
