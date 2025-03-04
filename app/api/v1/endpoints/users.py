from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_session
from app.db.models.users import User


router = APIRouter(prefix="/users", tags=["Users"])

# Только для админов
@router.get("/")
async def read_users(
    db: AsyncSession = Depends(get_session),
):
    query = select(User)

    result = await db.execute(query)
    return result.scalars().all()


@router.post("/register/")
def login():
    pass


@router.post("/login/")
def login():
    pass


@router.get("/me/")
def protected():
    pass


@router.get("/me/change-password")
def protected():
    pass


@router.delete("/me/")
def protected():
    pass
