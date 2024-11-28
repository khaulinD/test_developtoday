from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.base import Base, BaseMixin


class Mission(Base, BaseMixin):
    complete_state: Mapped[bool] = mapped_column(Boolean, default=False)

    cat = relationship("SpyCat", back_populates="mission", uselist=False)
    targets = relationship("Target", back_populates="mission", cascade="all, delete-orphan")


class Target(Base, BaseMixin):
    mission_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("missions.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String)
    country: Mapped[str] = mapped_column(String)
    note: Mapped[str] = mapped_column(String)
    complete_state: Mapped[bool] = mapped_column(Boolean, default=False)

    mission = relationship("Mission", back_populates="targets")
