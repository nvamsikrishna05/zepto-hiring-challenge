from email.policy import default
from decouple import config

API_TITLE = config("API_TITLE", default="IRCTC API")
API_DESCRIPTION = config("API_DESCRIPTION", default="IRCTC Ticket Booking System")
API_VERSION = config("API_VERSION", default="1.0")
HOST = config("HOST", default="localhost")
PORT = config("PORT", default=8000, cast=int)
