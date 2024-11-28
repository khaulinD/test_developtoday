from pydantic import BaseModel
from src.schemas.cats import CatSchema
from src.schemas.targets import TargetSchema, TargetInputSchema


class MissionInputSchema(BaseModel):
    targets: list[TargetInputSchema]


class MissionSchema(BaseModel):
    id: int
    cat: CatSchema | None = None
    targets: list[TargetSchema]
