import logging
from functools import wraps

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.core.settings import settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

engine = create_async_engine(settings.db.url, echo=False)  # Set echo to False
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


def db_session(func):
    """
    Decorator that provides a SQLAlchemy async session to the wrapped function.

    If a session is passed as a keyword argument, it uses that session.
    Otherwise, it creates and manages a new session. Rolls back on exceptions.
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        # If 'session' is already passed as an argument, use it.
        if "session" in kwargs:
            modified_kwargs = kwargs.copy()
            del modified_kwargs["session"]
            return await func(kwargs["session"], *args, **modified_kwargs)

        # Otherwise, create a new session and use it.
        async with async_session() as session:
            try:
                return await func(session, *args, **kwargs)
            except SQLAlchemyError as e:
                await session.rollback()
                logger.error(f"Failed to connect to db: {str(e)}")
                raise e

    return wrapper
