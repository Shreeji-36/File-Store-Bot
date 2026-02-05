# plugins/start.py
from pyrogram import Client, filters
from database import users

@Client.on_message(filters.command("start"))
async def start(client, message):
    users.update_one(
        {"user_id": message.from_user.id},
        {"$set": {"user_id": message.from_user.id}},
        upsert=True
    )

    await message.reply_text(
        f"👋 **Welcome to {client.me.first_name}**\n\n"
        "📂 Store files & generate shareable links.\n\n"
        "Use /help to see commands."
    )
