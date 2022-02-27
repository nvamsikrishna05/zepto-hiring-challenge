from typing import Counter
from sqlalchemy import Column, Integer, String
from app.config.database import Base


class Seat(Base):
    __tablename__ = "Seat"

    id = Column(Integer, primary_key=True)
    coach_type = Column(String(50), nullable=False, index=True)
    coach_number = Column(String(5), nullable=False)
    seat_number = Column(Integer, nullable=False)
