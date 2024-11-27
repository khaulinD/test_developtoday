from fastapi import HTTPException
from sqlalchemy import select, update
from sqlalchemy.orm import joinedload
from starlette import status
from starlette.responses import JSONResponse

from src.core.logger import get_logger
from src.database.db_session import db_session
from src.database.models import SpyCat
from src.database.models.missions import Mission, Target

logger = get_logger(__name__)


class MissionController:
    @staticmethod
    @db_session
    async def create_mission(session, data: dict):
        try:
            if "targets" not in data:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing 'targets'")

            mission = Mission()
            targets = [Target(**target_data, mission=mission) for target_data in data["targets"]]

            session.add_all(targets)
            session.add(mission)
            await session.commit()
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={"id": mission.id})
        except Exception as e:
            session.rollback()
            logger.error(f"Error creating mission data: {data}, Error: {e}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))



    @staticmethod
    @db_session
    async def delete_mission(session, mission_id: int):
        try:
            mission = await session.get(Mission, mission_id)
            if mission:
                # Check if the mission is assigned to a cat
                if mission.cat:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                        detail=f"Mission '{mission.description} is"
                                               f" assigned to Cat '{mission.cat.name}' and cannot be deleted.")
                else:
                    # Safe to delete the mission
                    session.delete(mission)
                    await session.commit()
                    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content={'status': 'ok'})
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Mission not found!")
        except Exception as e:
            logger.error(f"Error deleting mission. Error: {e}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    @db_session
    async def assign_mission(session, mission_id: int, cat_id: int):
        try:
            cat = await session.get(SpyCat, cat_id)
            if cat:
                mission = await session.get(Mission, mission_id)
                if mission:
                    mission.cat = cat
                    await session.commit()
                    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "Cat successfully assigned"})
                else:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Mission not found!")
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cat not found!")
        except Exception as e:
            logger.error(f"Error assign mission. Cat: {cat_id}, Mission: {mission_id}. Error: {e}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    @db_session
    async def get_mission_by_id(session, mission_id: int):

        res = await session.execute(
            select(Mission)
            .where(Mission.id == mission_id)
            .options(
                joinedload(Mission.cat),
                joinedload(Mission.targets)
            )
        )
        mission = res.scalar_one_or_none()
        print(mission)
        return mission

    @staticmethod
    @db_session
    async def get_missions(session):

        res = await session.execute(
            select(Mission)
            .options(
                joinedload(Mission.cat),
                joinedload(Mission.targets)
            )
        )
        mission = res.scalars().all()
        return mission

    @staticmethod
    @db_session
    async def update_mission_status(session, mission_id: int, status: bool):
        res = await session.execute(update(Mission).where(Mission.id == mission_id).values(complete_state=status))
        return True



