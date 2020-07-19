from bot.credentials import bot_token, bot_user_name, telegram_user_id, URL, api_id, api_hash
import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

import logging


global TOKEN
TOKEN = bot_token
# PROJECT_NAME = os.getenv('PROJECT_NAME', 'aiogram-example')  # Set it as you've set TOKEN env var

WEBHOOK_HOST = URL  # Enter here your link from Heroku project settings
WEBHOOK_PATH = '/webhook/'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.environ.get('PORT', 33507))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.warning(f'PORT:{WEBAPP_PORT}')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
# dp.middleware.setup(LoggingMiddleware())


@dp.message_handler()
async def echo(message: types.Message):
    # Regular request
    # await bot.send_message(message.chat.id, message.text)

    # or reply INTO webhook
    return SendMessage(message.chat.id, message.text)


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    # await dp.storage.close()
    # await dp.storage.wait_closed()

    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
