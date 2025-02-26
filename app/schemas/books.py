from pydantic import BaseModel


class BooksBase(BaseModel):
    title: str
    author: str
    description: str | None = None
    year: int | None = None


class BookCreate(BooksBase):
    pass


class Book(BooksBase):
    id: int

    class Config:
        from_attributes = True
