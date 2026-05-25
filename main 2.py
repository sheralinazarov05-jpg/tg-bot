from telethon import TelegramClient, events

api_id = 35449044
api_hash = "5674b70c6df3bf2fb94527e9a2891894"

client = TelegramClient(
    "session",
    api_id,
    api_hash
)

@client.on(events.NewMessage(incoming=True))
async def auto(event):

    text = event.raw_text.lower()

    if "привет" in text:
        await event.reply("Привет 👋")

client.start()

client.run_until_disconnected()