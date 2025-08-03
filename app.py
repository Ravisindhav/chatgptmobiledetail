import os
import requests
from pyrogram import Client, filters

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
NUMVERIFY_API = os.environ.get("NUMVERIFY_API")

app = Client("number_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Send me a mobile number with country code, e.g. +919876543210")

@app.on_message(filters.text)
async def lookup_number(client, message):
    number = message.text.strip()
    url = f"http://apilayer.net/api/validate?access_key={NUMVERIFY_API}&number={number}"
    try:
        res = requests.get(url).json()
        if res.get("valid"):
            reply = (
                f"📱 Number: {res.get('international_format', 'N/A')}\n"
                f"🌐 Country: {res.get('country_name', 'N/A')}\n"
                f"📶 Carrier: {res.get('carrier', 'N/A')}\n"
                f"📍 Location: {res.get('location', 'N/A')}"
            )
        else:
            reply = "⚠️ Invalid number or not found."
    except Exception as e:
        reply = f"⛔ Error fetching data: {e}"
    await message.reply(reply)

if __name__ == "__main__":
    app.run()
