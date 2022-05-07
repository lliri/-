import telebot
from requests import get
bot = telebot.TeleBot('5203002247:AAEW18D_hhgG87j-CMEAidEz0FSxGa4HKqw')

@bot.message_handler(commands=["r"])
def r(message):
    bot.send_message(message.chat.id, "ТЕСТ")
    bot.send_photo(message.chat.id, get('https://habrastorage.org/r/w1560/getpro/habr/upload_files/ec2/3e8/bfc/ec23e8bfce51faec092733d4d92e60a4.png').content)
@bot.message_handler(commands=["w"])
def w(message):
    bot.send_message(message.chat.id, "ТЕСТ")
    bot.send_photo(message.chat.id, get('https://phonoteka.org/uploads/posts/2021-06/1624655600_18-phonoteka_org-p-oboi-vindovs-khr-standartnie-krasivo-18.jpg').content) 







bot.polling()
