from pydantic import BaseModel


class CatSchema(BaseModel):
    name: str
    years_experience: float
    salary: float
    breed: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Whiskers",
                "years_experience": 3.5,
                "salary": 20000.0,
                "breed": "Siamese",
            }
        }


class CatUpdateSchema(BaseModel):
    salary: float | None = None
