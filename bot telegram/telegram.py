import teleani
import telebot
import random
mesage_old=''
mesage=''
bot = telebot.TeleBot('5375856364:AAFmin7Nwl4fo8_-xzzsygzAayfoIgE1DCk')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global mesage
    if message.text=='save':
        bot.send_message(message.from_user.id, 'Напиши своё имя.')
        #print(123456)
        mesage='save'
        #print(123)
        
    
        #message.text
        
    elif message.text[1:] == 'асскажи анекдот':
        x=teleani.givc()
        bot.send_message(message.from_user.id, x)
    elif message.text[1:]== "ривет":
        bot.send_message(message.from_user.id, "Привет, я пока мало что умею, но пытаюсь совершенствоваться, так что не забывай про меня./help")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'Привет' или напиши 'Расскажи анекдот'")
    else:
        bot.send_message(message.from_user.id, "Напиши /help")
        zz=open("bot.txt",'a')
        zz.write(message.text+'. ')
        zz.close()
    if message.text != mesage:
        mesage=message.text
        zx=open('save.txt','w')
        zx.write(message.text)
        zx.close()
        mesage=message.text
        #print(message.text)
    if message.text[1:]=='оё имя':
        zx=open('save.txt','r')
        bot.send_message(message.from_user.id , zx)
        zx.close()
    #print(message.text)
bot.polling(none_stop=True, interval=0)
