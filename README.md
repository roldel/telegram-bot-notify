# telegram-bot-notify
Simple, clear and reusable Telegram notification setup.
Create a bot in 2 minutes → send messages from shell or Python with one line :

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


# Telegram Bot Notification – Super Simple Setup

Send Telegram messages from your terminal or Python script in one line.

## 1. Create your bot with @BotFather (2 minutes)

1. Open Telegram and talk to [@BotFather](https://t.me/BotFather)
2. Send `/newbot`
3. Choose a name (e.g. "My Server Bot")
4. Choose a username ending with `bot` (e.g. `@my_server_bot`)
5. BotFather will reply with something like:

```
Done! Congratulations on your new bot.

...

Use this token to access the HTTP API:
123456789:AAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Keep your token secure...
```

## 2. Get your personal Chat ID

1. Open this link in your browser (replace `YOUR_TOKEN` with the one from your message above):
`https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`

2. Send any message to your bot in Telegram (click "Start" or just say hi)
3. Refresh the link above
4. You will see JSON containing `"chat":{"id":987654321,...`
→ That number (`987654321`) is your **CHAT_ID**


## 3. Setup `.env` in the repository root

Copy the example file:

```sh
git clone https://github.com/yourname/telegram-bot-notify.git
cd telegram-bot-notify
cp .env.sample .env
```

Then edit:

```
API_TOKEN=123456789:ABC-xxxxxxxxxxxxxxxxxxxxxxxx
CHAT_ID=123456789
```



## 4. Bash version – `tg "your message"`

### Install

Make script executable and put it in your PATH:
```sh
chmod +x bash/tg
sudo cp bash/tg /usr/local/bin/tg   # now you can use `tg` anywhere
```
### Usage :
```sh
tg "Server backup finished successfully ✅"
tg "Disk usage > 90% on $(hostname) ⚠️"
```

## 5. Python version – one-liner

### Install Python version

```sh
cd python
pip install -r requirements.txt
# or: pip install python-dotenv requests
Copy .env to the python folder or project root.
```

```python
from tg import tg

tg("Hello from Python 🚀")
tg(f"Job completed at {__import__('datetime').datetime.now()}")
```

### Usage

```sh
cd python
pip install -r requirements.txt
# or: pip install python-dotenv requests
Copy .env to the project root
```