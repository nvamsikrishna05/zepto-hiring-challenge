from sqlalchemy import select, func, distinct
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models.seat import Seat
from app.core.schemas.seat import CoachType

seats_count = {CoachType.AC: 60, CoachType.NAC: 60, CoachType.Chair: 120}
coach_prefix = {CoachType.AC: "B", CoachType.NAC: "S", CoachType.Chair: "C"}


async def get_coach_seats(session: AsyncSession, coach_number: str) -> list[Seat]:
    """
    Fetches all the Seats in a coach
    """
    result = await session.execute(
        select(Seat).where(Seat.coach_number == coach_number).order_by(Seat.seat_number)
    )
    return result.scalars().all()


async def add_coach(session: AsyncSession, coach_type: CoachType):
    """
    Adds a New Coach and all the seats
    """

    current_coaches = await session.execute(
        select(func.count(distinct(Seat.coach_number))).where(
            Seat.coach_type == coach_type
        )
    )
    new_coach_number = f"{coach_prefix[coach_type]}{current_coaches.scalar() + 1}"
    total_seats = seats_count[coach_type]
    for number in range(1, total_seats + 1):
        new_seat = Seat(
            coach_type=coach_type, seat_number=number, coach_number=new_coach_number
        )
        session.add(new_seat)
    return
