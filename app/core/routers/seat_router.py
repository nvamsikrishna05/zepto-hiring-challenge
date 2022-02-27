import imp
from sqlite3 import IntegrityError
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.services import seats
from app.config.database import get_session
from app.core.schemas.seat import Seat as SeatSchema, CoachType

router = APIRouter()


@router.get("/{coach_number}", response_model=list[SeatSchema])
async def fetch_coach_seats(
    coach_number: str, session: AsyncSession = Depends(get_session)
):
    result = await seats.get_coach_seats(session, coach_number)
    return result


@router.post("/{coach_type}")
async def add_new_coach(
    coach_type: CoachType, session: AsyncSession = Depends(get_session)
):
    await seats.add_coach(session, coach_type)
    try:
        await session.commit()
        return {"message": "Success"}
    except IntegrityError as ex:
        await session.rollback()
        return {"error": "Error Occured Adding a new Coach"}
