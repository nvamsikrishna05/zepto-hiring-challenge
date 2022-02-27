from pydantic import BaseModel
from enum import Enum


class CoachType(str, Enum):
    AC = "AC Sleeper"
    NAC = "Non AC Sleeper"
    Chair = "Seater"


class Seat(BaseModel):
    coach_type: CoachType
    coach_number: str
    seat_number: int

    class Config:
        orm_mode = True
