from flask import Flask, request
import telegram
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

import logging


class DLBot():
    def __init__(self, bot, token, URL, user_id=None):
        assert isinstance(token, str), 'Token must be of type string'
        assert user_id is None or isinstance(user_id, int), 'user_id must be of type int (or None)'

        self.bot = bot
        self.token = token  # bot token
        self.URL = URL
        self.user_id = user_id  # id of the user with access
        self.filters = None
        self.chat_id = None  # chat id, will be fetched during /start command
        # Enable logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        # Message to display on /start and /help commands
        self.startup_message = "Hi, I'm the DL bot! I will send you updates on your training process.\n" \
                               " send /start to activate automatic updates every epoch\n" \
                               " send /help to see all options.\n" \
                               " Send /status to get the latest results.\n" \
                               " Send /getlr to query the current learning rate.\n" \
                               " Send /setlr to change the learning rate.\n" \
                               " Send /quiet to stop getting automatic updates each epoch\n" \
                               " Send /plot to get a loss convergence plot.\n" \
                               " Send /stoptraining to stop training process.\n\n"

    def activate_bot(self):
        """ Function to initiate the Telegram bot """
        '''
        # for testing bot & webhook connection
        dispatcher = Dispatcher(bot, None, use_context=True)
        echo_handler = MessageHandler(Filters.text, echo)  # 當你輸入 hi 機器人就會回你 hi
        dispatcher.add_handler(echo_handler)  # 也將剛剛自動回覆的功能加到你的 bot內
        '''
        dp = Dispatcher(self.bot, None, use_context=True)
        dp.add_error_handler(self.error)  # log all errors

        # update = telegram.Update.de_json(request.get_json(force=True), bot)
        # dp.process_update(update)
        # self.chat_id = update.message.chat.id
        # self.msg_id = update.message.message_id

        self.filters = Filters.user(user_id=self.user_id) if self.user_id else None
        # Command and conversation handles
        #CommandHandler("start")
        #MessageHandler()
        dp.add_handler(CommandHandler("start", self.start, filters=self.filters))  # /start

    def start(self, update, context):    # (self, bot, update):
        """ Telegram bot callback for the /start command.
        Fetches chat_id, activates automatic epoch updates and sends startup message"""
        print(f'update:{update}')
        print(f'context:{context}')
        update.message.reply_text(self.startup_message, reply_markup=ReplyKeyboardRemove())
        self.chat_id = update.message.chat_id
        self.verbose = True

    def error(self, update, error):
        """Log Errors caused by Updates."""
        self.logger.warning('Update "%s" caused error "%s"', update, error)
