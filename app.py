import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID= os.getenv("TELEGRAM_CHAT_ID")
URL = "https://api.telegram.org/bot"+TOKEN+"/sendMessage"

msg = sys.argv[1]

obj = {
    "text": msg,
    "chat_id": CHAT_ID
}

x = requests.post(URL, data = myobj)
print("OK")