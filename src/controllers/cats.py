import difflib

from fastapi import HTTPException
from sqlalchemy import select, delete
from starlette import status

from src.core.logger import get_logger
from src.core.settings import settings
from src.database.db_session import db_session
from src.database.models.cats import SpyCat
from src.utils import async_get

logger = get_logger(__name__)


class CatsController:

    @staticmethod
    @db_session
    async def create_cat(session, data: dict):
        try:
            cats_breed = await async_get(settings.cats_breed_url)
            if cats_breed and any(obj['name'] == data['breed'] for obj in cats_breed):
                cat = SpyCat(**data)
                session.add(cat)
                await session.commit()
                return cat
            else:
                names = [obj['name'] for obj in cats_breed]
                most_similar = difflib.get_close_matches(data['breed'], names, n=2, cutoff=0.0)
                if most_similar:
                    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                         detail=f"Wrong cat breed, most similar one: {most_similar}")
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong cat breed")
        except Exception as e:
            logger.error(f"Error while creating cat, data: {data}, Error: {e}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    @db_session
    async def get_all_cats(session):
        res = await session.execute(select(SpyCat))
        return res.scalars().all()

    @staticmethod
    @db_session
    async def get_cat_by_id(session, cat_id):
        res = await session.execute(select(SpyCat).where(SpyCat.id==cat_id))
        return res.scalar_one_or_none()

    @staticmethod
    @db_session
    async def remove_cat_by_id(session, cat_id: int):
        res = await session.execute(delete(SpyCat).where(SpyCat.id == cat_id))
        return res.scalar_one_or_none()

    @staticmethod
    @db_session
    async def update_cat_by_id(session, cat_id: int, data: dict):
        try:
            cat = await session.get(SpyCat, cat_id)
            if cat is None:
                raise HTTPException(status_code=400, detail="Cat not found")
            for name, value in data.items():
                setattr(cat, name, value)
            await session.commit()
            return cat
        except Exception as e:
            logger.error(f"Error while updating cat: {cat_id}, Error: {e}")
            raise HTTPException(status_code=400, detail=str(e))



