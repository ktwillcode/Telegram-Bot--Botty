
import asyncio
from telegram import Bot

async def send_telegram_message(api_token, chat_id, message):
    # Initialize the bot
    bot = Bot(token=api_token)
    
    try:
        # Send the message asynchronously
        await bot.send_message(chat_id=chat_id, text=message)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Failed to send message: {e}")

async def main():
    API_TOKEN='YOUR API TOKEN'
    FRIEND_CHAT_ID='FRIEND_CHAT_ID'
    MESSAGE_TEXT='Your Message here'


    await send_telegram_message(API_TOKEN, FRIEND_CHAT_ID, MESSAGE_TEXT)

if __name__ == "__main__":
    asyncio.run(main())
