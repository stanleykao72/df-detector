from bot.credentials import bot_token, bot_user_name, telegram_user_id, URL, api_id, api_hash
from telethon import TelegramClient, events
import logging


global TOKEN
TOKEN = bot_token

# 機器人token
# bot = telegram.Bot(token=TOKEN)
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=TOKEN)

# 印出log的方法
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# 有Debug 以及 Info 模式，因為我不需要印太多資訊只需要Info就好
logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)


@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """Send a message when the command /start is issued."""
    await event.respond('Hi!')
    raise events.StopPropagation


@bot.on(events.NewMessage)
async def echo(event):
    """Echo the user message."""
    await event.respond(event.text)


def main():
    """Start the bot."""
    bot.run_until_disconnected()


if __name__ == '__main__':
    main()
