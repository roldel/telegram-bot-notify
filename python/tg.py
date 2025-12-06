import os
from dotenv import load_dotenv
import requests

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_FILE = os.path.join(REPO_ROOT, ".env")

load_dotenv(ENV_FILE)

API_TOKEN = os.getenv("API_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

class TelegramError(RuntimeError):
    """Raised when the Telegram API returns an error response."""

def tg(message: str, *, timeout: float = 10.0) -> None:
    """
    Send a Telegram message using the bot defined in .env.

    Raises:
        RuntimeError   – when config is missing
        TelegramError  – when Telegram API returns an error
    """
    if not API_TOKEN or not CHAT_ID:
        raise RuntimeError(
            f"Missing API_TOKEN or CHAT_ID in {ENV_FILE}"
        )

    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}

    try:
        resp = requests.post(url, data=data, timeout=timeout)
    except requests.RequestException as exc:
        # Network / DNS / TLS / timeout, etc.
        raise RuntimeError(f"Failed to reach Telegram API: {exc}") from exc

    if not resp.ok:
        # Try to extract Telegram-style JSON error
        description = None
        try:
            payload = resp.json()
            description = payload.get("description") or payload
        except ValueError:
            # Not JSON, fall back to raw text
            description = resp.text.strip()[:500]

        raise TelegramError(
            f"Telegram API error {resp.status_code}: {description}"
        )

    print(f"✅ Sent: {message}")
