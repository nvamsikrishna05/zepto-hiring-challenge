from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.core.services import seats
from app.config.database import get_session
from app.core.schemas.seat import Seat as SeatSchema, CoachType

router = APIRouter()


@router.get("/", response_model=list[SeatSchema])
async def fetch_all_seats(session: AsyncSession = Depends(get_session)):
    """
    Fetches all the Seats in the train along with Coach Details
    """
    result = await seats.get_all_seats(session)
    return result


@router.get("/{coach_number}", response_model=list[SeatSchema])
async def fetch_coach_seats(
    coach_number: str, session: AsyncSession = Depends(get_session)
):
    """
    Fetches all the Seats of the specified coach number
    """
    result = await seats.get_coach_seats(session, coach_number)
    return result


@router.post("/{coach_type}")
async def add_new_coach(
    coach_type: CoachType, session: AsyncSession = Depends(get_session)
):
    """
    Adds a new coach to the train of the specified coach type
    """
    await seats.add_coach(session, coach_type)
    try:
        await session.commit()
        return {"message": "Success"}
    except IntegrityError as ex:
        await session.rollback()
        return {"error": "Error Occured Adding a new Coach"}


@router.delete("/{coach_number}")
async def delete_coach(coach_number: str, session: AsyncSession = Depends(get_session)):
    """
    Deletes a Coach if exists and no bookings have been made against it.
    """
    await seats.delete_coach(session, coach_number)
    try:
        await session.commit()
        return {"message": "Success"}
    except:
        await session.rollback()
