from pydantic import BaseModel


class ReviewBase(BaseModel):
    rating: int
    text: str | None
    user_id: int
    book_id: int


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int

    class Config:
        from_attributes = True


class ReviewFilter(ReviewBase):
    rating: int | None = None
    text: str | None = None
    user_id: int | None = None
    book_id: int | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "rating": 5,
                "text": "Amazing book!",
                "user_id": 1,
                "book_id": 1
            }
        }