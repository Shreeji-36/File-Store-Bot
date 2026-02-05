from pyrogram import Client, filters
from config import *
import plugins

app = Client(
    "FileStoreBot",
    api_id=38528447,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

print("Bot Started Successfully 🚀")
app.run()
