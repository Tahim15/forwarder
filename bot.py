import asyncio
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME, TG_WORKERS

bot = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=TG_WORKERS,
    plugins=dict(root="plugins")
)

async def main():
    await bot.start()
    print("Bot is running and listening for new messages...")
    await idle()
    await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())
