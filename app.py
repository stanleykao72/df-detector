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
# bot = telegram.Bot(token=TOKEN)

# Create a DLBot instance
dlbot = DLBot(token=TOKEN, URL=URL, user_id=telegram_user_id)

# 印出log的方法
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# 有Debug 以及 Info 模式，因為我不需要印太多資訊只需要Info就好
# logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)

# Initial Flask app
app = Flask(__name__)

'''
# @app.route('/hook', methods=['POST'])
@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)

        chat_id = update.message.chat.id
        msg_id = update.message.message_id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8').decode()
        # for debugging purposes only
        print("got text message :", text)

        response = "response OK"
        # bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)
        dlbot.send_message(response)
    return 'ok'
'''


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = dlbot.set_webhook()
    if s:
        dlbot.activate_bot()
        return "webhook setup ok"
    else:
        return "webhook setup failed"


'''
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
'''

@app.route('/')
def index():
    return 'root directory'

'''
def echo(bot, update):
    """
     簡稱自動回話，也就是你打什麼，他就回你什麼
    """
    text = update.message.text  # 取得對話的內容
    update.message.reply_text(text)  # 回覆你輸入的內容


# for testing bot & webhook connection
dispatcher = Dispatcher(bot, None, use_context=True)
echo_handler = MessageHandler(Filters.text, echo)  # 當你輸入 hi 機器人就會回你 hi
dispatcher.add_handler(echo_handler)  # 也將剛剛自動回覆的功能加到你的 bot內
'''

if __name__ == '__main__':
    app.run(threaded=True)
