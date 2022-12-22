import sys
import uvicorn
from fastapi import FastAPI
from .Models.connection import engine

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.engine = engine
    return ("Connection Established to DATABASE")


@app.on_event("shutdown")
async def shutdown():
    app.engine.dispose()


@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    app.engine.
    return {"message": message}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)