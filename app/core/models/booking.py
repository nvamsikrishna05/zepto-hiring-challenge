from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint
from app.config.database import Base


class Booking(Base):
    __tablename__ = "Booking"

    id = Column(Integer, primary_key=True)
    coach_number = Column(String, ForeignKey("Seat.coach_number"))
    seat_number = Column(Integer, ForeignKey("Seat.seat_number"))
    user_id = Column(Integer)

    __table_args__ = (UniqueConstraint("coach_number", "seat_number"),)
