from fastapi import HTTPException
from sqlalchemy import update
from sqlalchemy.orm import joinedload
from src.database.db_session import db_session
from src.database.models.missions import Target
from starlette import status


class TargetsController:
    @staticmethod
    @db_session
    async def update_target_status(
        session, target_id: int, status: bool = False
    ):
        await session.execute(
            update(Target)
            .where(Target.id == target_id)
            .values(complete_state=status)
        )

    @staticmethod
    @db_session
    async def update_target_note(session, target_id: int, new_note: str):
        target = await session.get(
            Target, target_id, options=[joinedload(Target.mission)]
        )

        if not target:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Target not found",
            )

        if target.complete_state or (
            target.mission and target.mission.complete_state
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot update note because the target or mission status is true",
            )

        # Update the note if validation passes
        target.note = new_note
        await session.commit()
        return target
