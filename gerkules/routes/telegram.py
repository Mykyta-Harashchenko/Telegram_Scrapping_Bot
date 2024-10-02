from fastapi import status, APIRouter, Request
from constants import WEBHOOK_PATH
from main import bot, dp, types

router=APIRouter()

@router.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update=types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)