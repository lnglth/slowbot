import logging

import requests
from fastapi import FastAPI
from ray import serve

logger = logging.getLogger(__name__)
app = FastAPI()


@serve.deployment
@serve.ingress(app)
class FastAPIDeployment:
    @app.get("/")
    async def root(self):
        return {"message": "Hello World"}


serve.run(FastAPIDeployment.bind(), route_prefix="/")

print(requests.get("http://localhost:8000").json())
