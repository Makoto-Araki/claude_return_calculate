from fastapi import FastAPI

from apps.routers import add

app = FastAPI()

app.include_router(add.router)
