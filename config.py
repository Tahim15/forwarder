import os

API_ID = int(os.getenv("API_ID", "16531092"))
API_HASH = os.getenv("API_HASH", "b073b97bd4c8c56616fc2cbbd4da845a")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8059489284:AAH2RwyNXy02aWLrAjQ-IvNTDtuF8XQO_RQ")
SESSION_NAME = "forward_bot"

SOURCE_CHANNEL = int(os.getenv("SOURCE_CHANNEL", "-1002398179296"))
DEST_CHANNEL = int(os.getenv("DEST_CHANNEL", "-1002440398569"))
TG_WORKERS = 4  # Set to 4 for instant message processing
