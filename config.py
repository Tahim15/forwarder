import os

API_ID = int(os.getenv("API_ID", "your_api_id"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
SESSION_NAME = "forward_bot"

SOURCE_CHANNEL = int(os.getenv("SOURCE_CHANNEL", "-100xxxxxxxxx"))
DEST_CHANNEL = int(os.getenv("DEST_CHANNEL", "-100xxxxxxxxx"))
TG_WORKERS = 4  # Set to 4 for instant message processing
