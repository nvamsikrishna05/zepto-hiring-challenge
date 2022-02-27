from fastapi import FastAPI

from .config import apiconfig
from .config import database
from .core.models.user import User
from .core.models.seat import Seat
from .core.models.booking import Booking
from app.core.routers.seat_router import router as SeatRouter
from app.core.routers.booking_router import router as BookingRouter

# Initialize the app
app = FastAPI(
    title=apiconfig.API_TITLE,
    description=apiconfig.API_DESCRIPTION,
    version=apiconfig.API_VERSION,
)

app.include_router(SeatRouter, tags=["Seats"], prefix="/seat")
app.include_router(BookingRouter, tags=["Booking"], prefix="/booking")


@app.on_event("startup")
async def startup_event():
    await database.init_models()


# Add the Routers
@app.get("/")
async def hello():
    return {"message": "Hello IRCTC"}
