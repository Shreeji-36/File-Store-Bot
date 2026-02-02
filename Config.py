import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

BOT_NAME = os.getenv("BOT_NAME", "File Store Bot")
OWNER_ID = int(os.getenv("OWNER_ID"))

MONGO_URI = os.getenv("MONGO_URI")

FORCE_SUB_CHANNELS = []  # will be loaded from DB
