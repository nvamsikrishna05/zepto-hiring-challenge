from fastapi import FastAPI

from .config import apiconfig

# Initialize the app
app = FastAPI(
    title=apiconfig.API_TITLE,
    description=apiconfig.API_DESCRIPTION,
    version=apiconfig.API_VERSION,
)

# Add the Routers
@app.get("/")
async def hello():
    return {"message": "Hello IRCTC"}
