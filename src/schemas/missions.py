from pydantic import BaseModel

from src.schemas.cats import CatSchema
from src.schemas.targets import TargetSchema


class MissionInputSchema(BaseModel):
    targets: list[TargetSchema]


class MissionSchema(BaseModel):
    id: int
    cat: CatSchema | None = None
    target: list[TargetSchema]

