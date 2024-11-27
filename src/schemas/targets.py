from pydantic import BaseModel


class TargetSchema(BaseModel):
    name: str
    country: str
    note: str
    complete_state: bool = False

    class Config:
        json_schema_extra = {
            "example": {
                "mission_id": 1,
                "name": "Dimyla",
                "country": "Ukraine",
                "note": "Very strong",
                "complete_state": False
            }
        }


class TargetsNoteSchema(BaseModel):
    note: str | None = None

