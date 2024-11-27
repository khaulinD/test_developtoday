import re

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column,
)


class Base(DeclarativeBase):
    pass


class BaseMixin:
    """
    Base class for PostgreSQL databases. That creat id and correct name
    """

    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        # Convert camel case or Pascal case to snake case
        return re.sub(r"([a-z])([A-Z])", r"\1_\2", cls.__name__).lower() + "s"

    id: Mapped[int] = mapped_column(primary_key=True)
