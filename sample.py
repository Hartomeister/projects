# -*- coding: utf-8 -*-

import telebot
import logging
logger = logging.getLogger("mylogger")
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)

logger.addHandler(streamHandler)

bot = telebot.TeleBot('YOUR TOKEN')

@bot.message_handler(commands=['start'])
def handle_text(message):
    cid = message.chat.id
    bot.send_message(cid, 'ENTER TEXT HERE')




while 1 == 1:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception:
        pass
