from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_session
from app.db.models.users import User


router = APIRouter(tags=["Users"])

@router.get("/users/")
async def read_users(
    db: AsyncSession = Depends(get_session),
):
    query = select(User)

    result = await db.execute(query)
    return result.scalars().all()