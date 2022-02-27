from pydantic import BaseModel


class Booking(BaseModel):
    id: int
    coach_number: str
    seat_number: int
    user_id: int

    class Config:
        orm_mode = True


class AddBooking(BaseModel):
    coach_number: str
    user_id: int
    seats: list[int]
