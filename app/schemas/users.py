from pydantic import BaseModel, EmailStr
from fastapi_users import schemas


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase, schemas.BaseUserCreate):
    password: str


class UserRead(UserBase, schemas.BaseUser[int]):
    id: int
    is_active: bool
    is_verified: bool
    is_admin: bool

    class Config:
        from_attributes = True


class UserUpdate(schemas.BaseUserUpdate):
    username: str | None = None
    email: EmailStr | None = None
    is_admin: bool | None = None
