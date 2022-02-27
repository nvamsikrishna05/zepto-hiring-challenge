import queue
from sqlalchemy import select, func, distinct, delete, and_, join
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models.booking import Booking
from app.core.schemas.booking import AddBooking
from app.core.models.seat import Seat


async def get_all(session: AsyncSession):
    """
    Returns all the bookings
    """
    result = await session.execute(
        select(Booking).order_by(Booking.coach_number, Booking.seat_number)
    )
    return result.scalars().all()


async def get_coach_bookings(coach_number: str, session: AsyncSession):
    """
    Returns all bookings of a specific coach numbers
    """
    result = await session.execute(
        select(Booking)
        .where(Booking.coach_number == coach_number)
        .order_by(Booking.seat_number)
    )
    return result.scalars().all()


async def add_bookings(new_bookings: AddBooking, session: AsyncSession):
    """
    Adds new bookings
    """
    for berth in new_bookings.seats:
        print("Inside Loop =", berth)
        ticket = Booking(
            coach_number=new_bookings.coach_number,
            seat_number=berth,
            user_id=new_bookings.user_id,
        )
        session.add(ticket)


async def available_seats_coach(coach_number: str, session: AsyncSession):
    """
    Returns the avaiable seats ina  coach for booking
    """
    query = (
        select(Seat)
        .where(and_(Seat.coach_number == coach_number, Booking.seat_number == None))
        .join(
            Booking,
            and_(
                Seat.seat_number == Booking.seat_number,
                Seat.coach_number == Booking.coach_number,
            ),
            isouter=True,
            full=False,
        )
    )
    result = await session.execute(query)
    return result.scalars().all()
