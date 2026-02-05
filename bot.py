from pyrogram import Client, filters
from config import *
import plugins

app = Client(
    "FileStoreBot",
    api_id=38528447,
    api_hash=a0b76b9ff89c3f30adbb2696438c6581,
    bot_token=8578998808:AAHzol7mfZuHHNMT0g3Hv6u9SjiQXwxifJY
    plugins=dict(root="plugins")
)

print("Bot Started Successfully 🚀")
app.run()
