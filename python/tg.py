import os
from dotenv import load_dotenv
import requests

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_FILE = os.path.join(REPO_ROOT, ".env")

load_dotenv(ENV_FILE)

API_TOKEN = os.getenv("API_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def tg(message: str):
    if not API_TOKEN or not CHAT_ID:
        raise RuntimeError(
            f"Missing API_TOKEN or CHAT_ID in {ENV_FILE}"
        )

    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)
    print(f"✅ Sent: {message}")
