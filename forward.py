from pyrogram import Client, filters
from config import API_ID, API_HASH, SESSION_NAME, SOURCE_CHANNEL, DEST_CHANNEL, TG_WORKERS

app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    workers=TG_WORKERS
)

@app.on_message(filters.chat(SOURCE_CHANNEL) & filters.text)
async def forward_message(client, message):
    gofile_link = None
    streamtape_link = None

    for word in message.text.split():
        if "gofile.io" in word:
            gofile_link = word
        elif "streamtape.to" in word:
            streamtape_link = word

    final_link = gofile_link if gofile_link else streamtape_link
    if final_link:
        formatted_text = f"/leech {final_link}\n<b>Tag:</b> <c>@Mr_official_300</c> <c>2142536515</c>"
        await client.send_message(DEST_CHANNEL, formatted_text, parse_mode="html")

app.run()
