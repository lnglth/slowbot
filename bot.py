import logging

from fastapi import FastAPI

logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
