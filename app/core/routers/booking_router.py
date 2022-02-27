import imp
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.config.database import get_session
from app.core.models.booking import Booking
from app.core.schemas.booking import AddBooking, Booking as BookingSchema
from app.core.services import bookings
from app.core.schemas.seat import Seat as SeatSchema

router = APIRouter()


@router.get("/", response_model=list[BookingSchema])
async def fetch_all_bookings(session: AsyncSession = Depends(get_session)):
    """
    Fetches all the Bookings
    """
    result = await bookings.get_all(session)
    return result


@router.get("/{coach_number}", response_model=list[BookingSchema])
async def fetch_coach_bookings(
    coach_number: str, session: AsyncSession = Depends(get_session)
):
    """
    Fetches all the Bookings of a specified coach number
    """
    result = await bookings.get_coach_bookings(coach_number, session)
    return result


@router.post("/")
async def book_seats(
    new_bookings: AddBooking, session: AsyncSession = Depends(get_session)
):
    """
    Book seats in a coach
    """
    try:
        await bookings.add_bookings(new_bookings, session)
        await session.commit()
        return {"mesage": "Tickets Booked"}
    except IntegrityError as err:
        await session.rollback()
        return {"error": "Seat is already booked. Try new seats"}


@router.get("/available/{coach_number}", response_model=list[SeatSchema])
async def coach_available_seats(
    coach_number: str, session: AsyncSession = Depends(get_session)
):
    """
    Returns the Available Seats for Booking in a Coach
    """
    result = await bookings.available_seats_coach(coach_number, session)
    return result


@router.get("/available/", response_model=list[SeatSchema])
async def available_seats(session: AsyncSession = Depends(get_session)):
    """
    Returns the all Available Seats for Booking
    """
    result = await bookings.all_available_seats(session)
    return result
