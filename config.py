import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '5010'
OWNER_ID = 7355641270

MSG_EFFECT = 5046509860389126442

SHORT_URL = "linkshortify.com" # shortner url 
SHORT_API = "" 
SHORT_TUT = "https://t.me/How_to_Download_7x/26"

# Bot Configuration
SESSION = "𝗖𝗵𝗿𝗼𝗹𝗹𝗼"
TOKEN = "8578998808:AAHzol7mfZuHHNMT0g3Hv6u9SjiQXwxifJY"
API_ID = "38528447"
API_HASH = "a0b76b9ff89c3f30adbb2696438c6581"
WORKERS = 1

DB_URI = "mongodb+srv://Galaxy_Network:Zlqz3sLOMyAaOlT5@cluster0.prfw2el.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "Galaxy_Network"

FSUBS = [[-1002716211901, True, 10]] # Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Database Channel (Primary)
DB_CHANNEL = -1003075810179    # just put channel id dont add ""
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002595092736": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1001234567890": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 300
# Admin IDs
ADMINS = [7355641270]
# Bot Settings
DISABLE_BTN = False
PROTECT = True

# Messages Configuration
MESSAGES = {
    "START": "<b>◈ Hᴇʏ  {update.effective_user.mention_html()} ×</b>\n"
"<blockquote expandable><b>➤ ɪ ᴀᴍ ᴘʟᴇᴀsᴇᴅ ᴛᴏ ɪɴғᴏʀᴍ ʏᴏᴜ ᴛʜᴀᴛ ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴡɪᴛʜ ᴀɴɪᴍᴇ ғɪʟᴇs ғʀᴏᴍ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ sᴇʀɪᴇs.\n"
"➖➖➖➖➖➖➖➖➖\n"
"➤ ʏᴏᴜ ᴡɪʟʟ ʜᴀᴠᴇ ᴛʜᴇ ᴏᴘᴛɪᴏɴ ᴛᴏ sᴇʟᴇᴄᴛ ᴛʜᴇ ғᴏʀᴍᴀᴛ ᴏғ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ, ᴡʜᴇᴛʜᴇʀ ɪᴛ ʙᴇ 480ᴘ, 720ᴘ, 1080ᴘ, ᴏʀ ᴀɴʏ ᴏᴛʜᴇʀ ᴘʀᴇғᴇʀᴇɴᴄᴇ ʏᴏᴜ ᴍᴀʏ ʜᴀᴠᴇ.\n"
"➖➖➖➖➖➖➖➖➖\n"
"➤ ᴡᴇ ᴀʀᴇ ʜᴇʀᴇ ᴛᴏ ᴄᴀᴛᴇʀ ᴛᴏ ʏᴏᴜʀ ᴀɴɪᴍᴇ ɴᴇᴇᴅs ᴡɪᴛʜ ᴛʜᴇ ᴜᴛᴍᴏsᴛ ᴘʀᴏғᴇssɪᴏɴᴀʟɪsᴍ ᴀɴᴅ ǫᴜᴀʟɪᴛʏ.</b></blockquote>\n\n"
"<b>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : </b>"
"<a href='https://t.me/Prince_Vegeta_36'>𝗖𝗵𝗿𝗼𝗹𝗹𝗼</a>",
    "FSUB": "<blockquote><b>◈ Hᴇʏ  {update.effective_user.mention_html()} ×\n"
            "›› Yᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ. Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs ᴘʀᴏᴠɪᴅᴇᴅ ʙᴇʟᴏᴡ, ᴛʜᴇɴ ᴛʀʏ ᴀɢᴀɪɴ.. !</b></blockquote>\n\n"
            "<b>››❗Fᴀᴄɪɴɢ ᴘʀᴏʙʟᴇᴍs, ᴜsᴇ: /help</b>",
    "ABOUT": "<b>›› ғᴏʀ ᴍᴏʀᴇ: @Galaxy_Networkk \n <blockquote expandable>›› ᴍʏ ɴᴀᴍᴇ: <a href='https://t.me/AG_Unohana_bot'>sᴏɪғᴏɴ</a> \n›› ᴏᴡɴᴇʀ: @ProYato\n›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a> \n›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a> \n›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a> \n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/Prince_Vegeta_36'>𝗖𝗵𝗿𝗼𝗹𝗹𝗼</a></b></blockquote>",
    "REPLY": "<b>ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃..</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "https://i.ibb.co/TMzM8QP0/x.jpg",
    "FSUB_PHOTO": "https://i.ibb.co/wFB83dXW/x.jpg",
    "SHORT_PIC": "https://i.ibb.co/Sw7jdmSB/x.jpg",
    "SHORT": "https://telegra.ph/file/8aaf4df8c138c6685dcee-05d3b183d4978ec347.jpg"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger