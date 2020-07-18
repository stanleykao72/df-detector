from flask import Flask, request
import telegram
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from bot.credentials import bot_token, bot_user_name, telegram_user_id, URL
from bot.dl_bot import DLBot
import logging


global bot
global TOKEN
TOKEN = bot_token

# 機器人token
bot = telegram.Bot(token=TOKEN)
# Create a DLBot instance
dlbot = DLBot(token=TOKEN, user_id=telegram_user_id)
dlbot.activate_bot()

# 印出log的方法
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# 有Debug 以及 Info 模式，因為我不需要印太多資訊只需要Info就好
# logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)

# Initial Flask app
app = Flask(__name__)

'''
@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
'''

if __name__ == '__main__':
    app.run(threaded=True)
