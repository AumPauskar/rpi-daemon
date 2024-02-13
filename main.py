import fan_control
import rgb_control
import json
# telegram stuff
import asyncio
import telegram

with open('api_key.json') as f:
    data = json.load(f)
    BOT_TOKEN = data['telegramAPI']

async def get_chat_id():
    bot = telegram.Bot(token=BOT_TOKEN)
    updates = await bot.get_updates()
    if updates:
        return updates[-1].message.chat_id
    else:
        raise ValueError("No updates found")
    
async def send_message(chat_id, text):
    bot = telegram.Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=chat_id, text=text)

async def main():
    try:
        TARGET_CHAT_ID = await get_chat_id()
        MESSAGE_TEXT = 'Hello, World!'
        await send_message(TARGET_CHAT_ID, MESSAGE_TEXT)
    except Exception as e:
        print(f"Error: {e}")
    fan_control.fan_control()
    rgb_control.rgb_control()

if __name__ == '__main__':
    # main()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())