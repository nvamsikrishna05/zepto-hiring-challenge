from fastapi import FastAPI

from .config import apiconfig
from .config import database
from .core.models.user import User

# Initialize the app
app = FastAPI(
    title=apiconfig.API_TITLE,
    description=apiconfig.API_DESCRIPTION,
    version=apiconfig.API_VERSION,
)


@app.on_event("startup")
async def startup_event():
    await database.init_models()


# Add the Routers
@app.get("/")
async def hello():
    return {"message": "Hello IRCTC"}
