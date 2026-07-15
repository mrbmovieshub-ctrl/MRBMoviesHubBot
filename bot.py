from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.filters import command

from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "MRBMoviesHubBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(command("start"))
async def start(client, message):
    await message.reply_text(
        "👋 Welcome to MRB Movies Hub Bot!\n\n"
        "🔎 Send a movie name to search."
    )

print("🤖 Bot is starting...")

app.run()
