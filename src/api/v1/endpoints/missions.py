from fastapi import APIRouter
from src.controllers.missions import MissionController
from src.core.logger import get_logger
from src.schemas.missions import MissionInputSchema, MissionSchema


router = APIRouter()
logger = get_logger(__name__)


@router.get("/{mission_id}", response_model=MissionSchema | None)
async def get_mission(mission_id: int):
    res = await MissionController.get_mission_by_id(mission_id=mission_id)
    return res


@router.get("", response_model=list[MissionSchema])
async def get_missions():
    res = await MissionController.get_missions()
    return res


@router.post("")
async def create_mission(mission: MissionInputSchema):
    res = await MissionController.create_mission(data=mission.model_dump())
    return res


@router.delete("/{mission_id}")
async def delete_mission(mission_id: int):
    res = await MissionController.delete_mission(mission_id=mission_id)
    return res


@router.patch("/{mission_id}")
async def update_mission_status(mission_id: int, status: bool = False):
    res = await MissionController.update_mission_status(
        mission_id=mission_id, status=status
    )
    return res


@router.patch("/{mission_id}/cat/{cat_id}")
async def assign_mission(mission_id: int, cat_id: int):
    res = await MissionController.assign_mission(
        mission_id=mission_id, cat_id=cat_id
    )
    return res
