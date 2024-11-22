import telebot
from db import Database
token = '7792408011:AAEZKlxr5KchQPOhR5O8VPTC7M0prW2uhV4';
bot = telebot.TeleBot(token);  

#7729336143:AAFs3fKMgC7PDEhmwSm1-ZChBdg9alfsHcs -1    7792408011:AAEZKlxr5KchQPOhR5O8VPTC7M0prW2uhV4 -2
user_message = ""
#Приветсвие

@bot.message_handler(commands=['start'])
def welcome(message):

    msg = bot.send_message(message.chat.id, "Привет, я бот, напиши /text, чтобы ввести своё сообщение")
    bot.register_next_step_handler(msg, callback=hand)

@bot.message_handler(commands=['text'], func=lambda message: True)
def hand(message):                                                                                         #Ввод сообщения

    msg = bot.send_message(message.chat.id, "Введи своё сообщение")
    global user_message
    user_message = message.text
    bot.register_next_step_handler(msg, callback=messg)
        
def messg(message):                                                                                        #Да\нет

    bot.send_message(message.chat.id, "Стоит ли отправлять Твоё сообщение?")
    msg = bot.send_message(message.chat.id, "Напиши Да/Нет.")
    bot.register_next_step_handler(msg, callback=yn)

def yn(message):                                                                                           #Отправка(или нет)
    global user_message
    owner_id = 5426110205
    if message.text =="Да":	
        bot.send_message(message.chat.id, "Хорошо! Сообщение отправлено!")
        bot.forward_message(owner_id, message.chat.id, message);
    if message.text=="Нет":
        msg = bot.send_message(message.chat.id, "Плохо! Чтож, давай по новой.")
        return(bot.register_next_step_handler(msg, callback=hand));
    

bot.polling(none_stop=True, interval=0) 