from sqlalchemy.orm import DeclarativeBase, declared_attr

from app.utils.camel_to_snake import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}"
