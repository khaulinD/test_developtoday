import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

from .logger import get_logger


logger = get_logger(__name__)

load_dotenv()

BASE_DIR = Path(__file__).parent.parent


class DbSettings(BaseModel):
    """Database settings from environment variables."""

    DB_USER: str = os.getenv("POSTGRES_USER", "postgres")
    DB_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
    DB_HOST: str = os.getenv("POSTGRES_HOST", "db")
    DB_PORT: int = os.getenv("POSTGRES_PORT", 5432)
    DB_NAME: str = os.getenv("POSTGRES_DB", "dbname")
    url: str = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    echo: bool = False


class Settings(BaseSettings):
    """Aggregated application settings."""
    cats_breed_url: str = "https://api.thecatapi.com/v1/breeds"
    db: DbSettings = DbSettings()


settings = Settings()
