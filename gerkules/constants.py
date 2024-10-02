from config.config import config

TOKEN=config.get("BOT_TOKEN")


WEBHOOK_PATH=f"/bot/{TOKEN}"

WEBHOOK_URL=f"{config.get('NGROK_URL')}{WEBHOOK_PATH}"