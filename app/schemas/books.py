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


class BookFilter(BooksBase):
    title: str | None = None
    author: str | None = None
    description: str | None = None
    year: int | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "The Catcher in the Rye",
                "author": "J.D. Salinger",
                "year": 1951,
                "description": "A novel about a young man's experiences in New York City."
            }
        }
