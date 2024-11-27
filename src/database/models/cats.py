from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.base import Base, BaseMixin


class SpyCat(Base, BaseMixin):
    name: Mapped[str] = mapped_column(String)
    breed: Mapped[str] = mapped_column(String)
    salary: Mapped[float] = mapped_column(Float)
    years_experience: Mapped[float] = mapped_column(Float)
    mission_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("missions.id"), unique=True, nullable=True
    )

    mission = relationship("Mission", back_populates="cat")
