# plugins/batch.py
from pyrogram import Client, filters
from database import files
import random, string

@Client.on_message(filters.command("batch") & filters.private)
async def batch(client, message):
    await message.reply_text(
        "📦 Send **first file**, then **last file** of batch.\n"
        "Both must be forwarded from this bot."
    )
