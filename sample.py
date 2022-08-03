# -*- coding: utf-8 -*-

import telebot

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
