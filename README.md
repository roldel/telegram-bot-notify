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

## 2. Getting Your Chat ID (Personal or Group)

Your bot needs a **CHAT_ID** to know *where* to send messages.  
There are **two possible setups** depending on your use case:

---

### 1. Personal Chat ID — For private notifications (single user)

1. Open this link in your browser (replace `<YOUR_TOKEN>` with the one from your STEP 1 message above):

`https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`

2. Send any message to your bot in Telegram (click "Start" or just say hi)
3. Refresh the link above
4. You will see JSON containing 
```json
"chat":{"id":987654321,... }
```

That number (`987654321`) is your **CHAT_ID**

---


### 2. Group / Channel Chat ID — For shared notifications (multi-user)

Use this if **multiple people should receive your notifications.**

1. Create a Telegram group or channel. Examples:
- `Server Alerts`
- `Deployment Notifications`

2. Add your bot to that group/channel

3. Send any message in the group/channel  
This ensures it appears in `/getUpdates`.

4. Open the same link:

`https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`

5. Look for a chat object like:

```json
# Group example:
"chat": { "id": -1001234567890, "type": "supergroup", "title": "Server Alerts" }
```

#### Channel example:
```json
# Channel example
"chat": { "id": -1009876543210, "type": "channel", "title": "My Notifications" }
```

> **Group/channel CHAT_IDs are usually negative numbers starting with `-100`.**

Now **everyone in that group/channel** will receive all bot notifications.

---

### Summary Table

| Use Case | CHAT_ID Type | Who Sees Messages? |
|---------|--------------|--------------------|
| **Personal alerts** | `123456789` | Only you |
| **Group notifications** | `-100xxxxxxxxxx` | All group members |
| **Channel notifications** | `-100xxxxxxxxxx` | All channel subscribers |







## 3. Setup `.env` in the repository root

Copy the example file:

```sh
git clone https://github.com/yourname/telegram-bot-notify.git
cd telegram-bot-notify
cp .env.sample .env
```

Then edit:

```sh
# API_TOKEN from step 1
API_TOKEN=123456789:ABC-xxxxxxxxxxxxxxxxxxxxxxxx
#CHAT_ID from step 2
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

## 5. Send a Multi Lines Message

Usage :
```sh
tg "$(printf 'Line 1\nLine 2\nLine 3\n')"
```