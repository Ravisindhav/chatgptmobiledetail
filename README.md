# Telegram Mobile Lookup Bot

This lightweight Telegram bot allows you to look up basic mobile number details (country, carrier, location) using the NumVerify API.

## Setup

1. Signup at [numverify.com](https://numverify.com/) and get an API key.
2. Create a Telegram bot using BotFather and get a BOT_TOKEN.
3. Obtain your Telegram API_ID and API_HASH from my.telegram.org.

## Deployment on Heroku

1. Push this repo to GitHub.
2. Create a Heroku app.
3. Connect GitHub repo under "Deploy".
4. Go to **Settings → Config Vars** and add:
    - `API_ID`
    - `API_HASH`
    - `BOT_TOKEN`
    - `NUMVERIFY_API`
5. Deploy and enable worker dyno.
6. Start the bot with `/start`.

### Usage
Send a phone number in international format (e.g. `+919876543210`) and the bot will reply with basic info.

---

⚠️ **Disclaimer**: This bot only provides publicly available info via APIs. It does **not** retrieve personal names or sensitive data without proper authorization.
