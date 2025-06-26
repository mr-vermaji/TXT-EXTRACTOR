import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "28947698"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "181af3baf73a37c24a429ca08e3f34f8")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7865286514:AAEmR24UTgXPUqiytHgvhd2GdSdxFtkxfm4")

OWNER_ID = int(os.environ.get("OWNER_ID", "7035612796"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "7035612796").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://user:<user>@cluster0.84a1ndc.mongodb.net")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002586433753"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002586433753")  # Optional here you'll get all logs
