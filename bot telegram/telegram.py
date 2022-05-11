import teleani
import telebot
import random

bot = telebot.TeleBot('5375856364:AAFmin7Nwl4fo8_-xzzsygzAayfoIgE1DCk')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Расскажи анекдот':
        x=teleani.givc()
        bot.send_message(message.from_user.id, x)
    elif message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я пока мало, что умею, но мой ассортимент будет увеличиваться, и чтобы узнать что я могу на данный момент напиши /help")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет или напиши расскажи анекдот")
    else:
        bot.send_message(message.from_user.id, "напиши /help")
        zz=open('bot.txt', 'a')
        zz.write(message.text)
        zz.close()
bot.polling(none_stop=True, interval=0)
