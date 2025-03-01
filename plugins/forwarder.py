from pyrogram import Client, filters
from config import SOURCE_CHANNEL, DEST_CHANNEL

@Client.on_message(filters.chat(SOURCE_CHANNEL) & filters.text)
async def forwarder(client, message):
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
