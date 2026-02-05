# plugins/help.py
from pyrogram import Client, filters

@Client.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text("""
📌 **Available Commands**

/start – Start the bot  
/Batch – Store multiple files  
/Genlink – Store single file/message  
/Refresh – Refresh bot status  
/Help – Show this menu  
/fsub – Add force subscribe channel  
/Remove_fsub – Remove force sub  
/Broadcast – Send message to all users  
/Settings – Modify bot settings
""")
