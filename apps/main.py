"""FastAPIアプリのエントリポイント。各演算ルーターをここに登録する。"""

from fastapi import FastAPI

from apps.routers import add, multiply, subtract

app = FastAPI()

app.include_router(add.router)
app.include_router(subtract.router)
app.include_router(multiply.router)
