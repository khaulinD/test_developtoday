from fastapi import APIRouter
from .endpoints import cats_router, missions_router, targets_router

router = APIRouter()

router.include_router(cats_router, prefix="/cats", tags=["Cats"])
router.include_router(missions_router, prefix="/missions", tags=["Missions"])
router.include_router(targets_router, prefix="/targets", tags=["Targets"])
