# telegram-bot-notify

Simple, clean and reusable Telegram notification system.  
Send messages using:

- `tg "message"` from shell  
- `tg("message")` from Python



```
telegram-bot-notify/
├── .env.sample
├── .env
├── README.md
├── sh/
│   └── tg
└── python/
    ├── tg.py
    └── requirements.txt
```

## 1. Create your bot with @BotFather

1. Open Telegram → Search for **@BotFather**
2. `/newbot`
3. Choose a name + username (ending with `bot`)
4. BotFather sends you a token like:

```
123456789:ABC-xxxxxxxxxxxxxxxxxxxxxxxx
```

This is your **API_TOKEN**.

## 2. Get your Chat ID

1. Replace YOUR_TOKEN in:

```
https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
```

2. Send a message to your bot in Telegram  
3. Refresh the URL above  
4. Look for:

```
"chat":{"id":123456789}
```

That number is your **CHAT_ID**.

## 3. Setup `.env` in the repository root

Copy the example file:

```sh
cp .env.sample .env
```

Then edit:

```
API_TOKEN=123456789:ABC-xxxxxxxxxxxxxxxxxxxxxxxx
CHAT_ID=123456789
```

## 4. Shell usage

Make script executable:

```sh
chmod +x sh/tg
```

Send a message:

```sh
./sh/tg "Deployment finished successfully 🚀"
```

### Install system-wide

```sh
sudo cp sh/tg /usr/local/bin/tg
```

Use globally:

```sh
tg "Hello from anywhere 🌍"
```

## 5. Python usage

Install dependencies:

```sh
pip install -r python/requirements.txt
```

Use:

```python
from tg import tg
tg("Hello from Python 🐍")
```

## 6. Summary

| Component | Reads `.env` from repo root | Purpose |
|----------|------------------------------|---------|
| `sh/tg`  | ✅ Yes                       | Shell notifications |
| `python/tg.py` | ✅ Yes                 | Python notifications |

There is now **one single, opinionated config source**:

```
./.env
```

## 7. Example `.env.sample`

```env
API_TOKEN=replace_with_your_bot_token
CHAT_ID=replace_with_your_chat_id
```
