from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from app.db.models.reviews import Review
from app.schemas.reviews import ReviewCreate


async def get_reviews(db: AsyncSession, **params):
    query = select(Review).filter_by(**params)

    result = await db.execute(query)
    return result.scalars().all()


def is_params_not_none(params) -> bool:
    for value in params.values():
        if value:
            return True
    return False


async def update_review_by_id(db: AsyncSession, id: int, **params):
    # If not parameters provided, then nothing to update
    if not is_params_not_none(params=params):
        raise HTTPException(
            status_code=400,
            detail="At least one parameter must be provided to update review",
        )

    review_to_update = await db.execute(select(Review).where(Review.id == id))
    review_to_update = review_to_update.scalars().first()

    if not review_to_update:
        raise HTTPException(
            status_code=404,
            detail="Review not found",
        )

    for key, value in params.items():
        if value:
            setattr(review_to_update, key, value)

    await db.commit()
    await db.refresh(review_to_update)
    return review_to_update


async def delete_review_by_id(db: AsyncSession, id):
    query = select(Review).where(Review.id == id)

    result = await db.execute(query)
    review_to_delete = result.scalars().all()

    if not review_to_delete:
        return []

    await db.delete(review_to_delete)
    await db.commit()
    return review_to_delete


async def create_review(db: AsyncSession, review: ReviewCreate):
    db_review = Review(**review.model_dump())
    db.add(db_review)
    await db.commit()
    await db.refresh(db_review)
    return db_review
