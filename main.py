from imp import reload
import uvicorn
from app.config import apiconfig

if __name__ == "__main__":
    uvicorn.run("app.app:app", host=apiconfig.HOST, port=apiconfig.PORT, reload=True)
