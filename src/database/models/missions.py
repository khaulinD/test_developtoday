from sqlalchemy import Boolean, String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.base import Base, BaseMixin


class Mission(Base, BaseMixin):
    complete_state: Mapped[bool] = mapped_column(Boolean, default=False)

    cat = relationship("SpyCat", back_populates="mission", uselist=False)
    targets = relationship("Target", back_populates="mission")


class Target(Base, BaseMixin):
    mission_id: Mapped[int] = mapped_column(Integer, ForeignKey("missions.id"), nullable=False)
    name: Mapped[str] = mapped_column(String)
    country: Mapped[str] = mapped_column(String)
    note: Mapped[str] = mapped_column(String)
    complete_state: Mapped[bool] = mapped_column(Boolean, default=False)

    mission = relationship("Mission", back_populates="targets")
