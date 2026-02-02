from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["filestorebot"]

users = db.users
files = db.files
settings = db.settings
fsub = db.fsub
