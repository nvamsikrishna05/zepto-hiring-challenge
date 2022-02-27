from sqlalchemy import Column, Integer, String, Boolean
from app.config.database import Base


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)
