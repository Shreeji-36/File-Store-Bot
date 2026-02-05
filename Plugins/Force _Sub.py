# plugins/fsub.py
from pyrogram import Client, filters
from database import fsub
from config import OWNER_ID

@Client.on_message(filters.command("fsub") & filters.user(OWNER_ID))
async def add_fsub(client, message):
    channel = message.command[1]
    fsub.insert_one({"channel": channel})
    await message.reply("✅ Force sub channel added")

@Client.on_message(filters.command("remove_fsub") & filters.user(OWNER_ID))
async def remove_fsub(client, message):
    channel = message.command[1]
    fsub.delete_one({"channel": channel})
    await message.reply("❌ Force sub removed")
