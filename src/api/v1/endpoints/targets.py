from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.controllers.targets import TargetsController
from src.core.logger import get_logger
from src.schemas.targets import TargetsNoteSchema

router = APIRouter()
logger = get_logger(__name__)


@router.patch("/{target_id}")
async def update_target(target_id: int, status: bool | None = None):
    res = await TargetsController.update_target_status(target_id=target_id, status=status)
    return JSONResponse(status_code=200, content={"status": "Status update successful"})


@router.patch("/{target_id}/note")
async def update_target_note(target_id: int, note: TargetsNoteSchema):

    res = await TargetsController.update_target_note(target_id=target_id, new_note=note.note)
    return res
