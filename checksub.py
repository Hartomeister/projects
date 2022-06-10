import telebot
import telebot
from telebot import types
import time
import random


# ставим переменные бота

ID = "5058141288"
bot = telebot.TeleBot("5139079205:AAEiHfbGHLi4jWj9Rv5KBFB4SyNLtnlKdCU")
list = ["el1", "el2"]

# ставим команды

bot.send_message(
    ID, "Бот запущен! Автор: http://XOAI.ru"
)  # отправляем СМСку админу о запуске бота
print("Bot started")


@bot.message_handler(commands=["msg"])
def start(message):
    msg = bot.send_message(message.chat.id, " сообщение")
    msg = bot.reply_to(message, "Ответ на сообщение")  # ⏳
    # m_id = message.chat.id
    # user_input = message.text
    # num = user_input.replace(' ', '')


@bot.message_handler(commands=["start"])
def chat(message):
    user_id = message.chat.id
    my_channel_id = -1001709716107
    statuss = ["creator", "administrator", "member"]
    for i in statuss:
        if (
            i
            == bot.get_chat_member(
                chat_id=my_channel_id, user_id=message.from_user.id
            ).status
        ):
            bot.send_sticker(
                message.chat.id,
                "CAACAgIAAxkBAAED_9hiGGyyKQnRqMF99hcJ_pfvHvyO2AACPAAD-7g6BAwMRWBCpy3SIwQ",
            )
            user_first_name = str(message.chat.first_name)
            bot.reply_to(message, f"Привет, {user_first_name}! \n\nСпасибо за подписку! Бот пока находится в разработке, оставайтесь в курсе новостей!")
            break

    else:
        bot.send_sticker(
            message.chat.id,
            "CAACAgIAAxkBAAED_9ZiGGwD3OHU_t_YV9n1mSw0WliolQACVwAD-7g6BHKLsf07S5gQIwQ",
        )
        bot.send_message(
            message.chat.id, "Подпишись на канал @ExampleOrTest"
        )

while 1 == 1:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception:
        pass
