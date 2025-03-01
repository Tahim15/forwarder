from pyrogram import Client, filters
import re
from config import SOURCE_CHANNEL, DEST_CHANNEL

@Client.on_message(filters.chat(SOURCE_CHANNEL) & filters.text)
async def forwarder(client, message):
    # Extract unique links
    gofile_links = list(set(re.findall(r"https?://gofile.io/d/\S+", message.text)))
    streamtape_links = list(set(re.findall(r"https?://streamtape.to/\S+", message.text)))

    # Prioritize gofile.io links, then streamtape.to links
    unique_links = gofile_links if gofile_links else streamtape_links

    # Send each link one by one
    for link in unique_links:
        formatted_text = f"/leech {link}\n<b>Tag:</b> <c>@Mr_official_300 2142536515</c>"
        await client.send_message(DEST_CHANNEL, formatted_text, parse_mode="html")
