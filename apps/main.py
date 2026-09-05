"""FastAPIアプリのエントリポイント。各演算ルーターをここに登録する。"""

import os

from fastapi import FastAPI

from apps.routers import add, divide, multiply, subtract

app = FastAPI()

app.include_router(add.router)
app.include_router(subtract.router)
app.include_router(multiply.router)
app.include_router(divide.router)
