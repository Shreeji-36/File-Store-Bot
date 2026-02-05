# plugins/broadcast.py
from pyrogram import Client, filters
from database import users
from config import OWNER_ID

@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(client, message):
    if not message.reply_to_message:
        return await message.reply("Reply to message to broadcast.")

    count = 0
    for user in users.find():
        try:
            await message.reply_to_message.copy(user["user_id"])
            count += 1
        except:
            pass

    await message.reply(f"✅ Broadcast sent to {count} users")
