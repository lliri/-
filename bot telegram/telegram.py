import teleani
import telebot
import random

bot = telebot.TeleBot('5375856364:AAFmin7Nwl4fo8_-xzzsygzAayfoIgE1DCk')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет или напиши расскажи аникдот")
    else:
        bot.send_message(message.from_user.id, "напиши /help")
    if message.text == 'Расскажи анекдот':
        x=teleani.givc()
        bot.send_message(message.from_user.id, x)
bot.polling(none_stop=True, interval=0)
