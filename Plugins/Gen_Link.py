# plugins/genlink.py
from pyrogram import Client, filters
from database import files
import random, string

def gen_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

@Client.on_message(filters.command("genlink") & filters.private)
async def genlink(client, message):
    if not message.reply_to_message:
        return await message.reply("Reply to a file or message.")

    file_id = gen_id()
    files.insert_one({
        "file_id": file_id,
        "message": message.reply_to_message.id,
        "chat": message.chat.id
    })

    await message.reply_text(
        f"🔗 **Link Generated**:\n"
        f"https://t.me/{client.me.username}?start={file_id}"
    )
