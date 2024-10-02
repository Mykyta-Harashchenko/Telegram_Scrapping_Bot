from typing import Union
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from main import bot
from constants import WEBHOOK_URL
from routes.telegram import router as telegram_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await bot.set_webhook(url=WEBHOOK_URL, drop_pending_updates=True)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(telegram_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run("run:app", reload=True, host="localhost", port=8000)