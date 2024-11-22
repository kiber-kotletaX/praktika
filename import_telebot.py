import telebot
token = '7792408011:AAEZKlxr5KchQPOhR5O8VPTC7M0prW2uhV4';
bot = telebot.TeleBot(token);  

#7729336143:AAFs3fKMgC7PDEhmwSm1-ZChBdg9alfsHcs -1    7792408011:AAEZKlxr5KchQPOhR5O8VPTC7M0prW2uhV4 -2

#Приветсвие
@bot.message_handler(commands=['start'])
def welcome(message):

    msg = bot.send_message(message.chat.id, "Привет, я бот, напиши /text, чтобы ввести своё сообщение")
    bot.register_next_step_handler(msg, callback=hand)

@bot.message_handler(commands=['text'])
def hand(message):                                                                                          #Ввод сообщения

    msg = bot.send_message(message.chat.id, "Введи своё сообщение")
    bot.register_next_step_handler(msg, callback=messg)
        
def messg(message):                                                                                          #Отправка

    bot.send_message(message.chat.id, "Стоит ли отправлять Твоё сообщение?")

def yn(message):
    owner_id = 5426110205
    if message.text == 'Хз':
        bot.send_message(message.chat.id, "Вот и я хз, отправлять, или нет")
    elif message.text =="Да":	
        bot.send_message(message.chat.id, "Хорошо! Сообщение отправлено!")
        bot.forward_message(message.chat.id, message.text, owner_id)
    else:
        msg = bot.send_message(message.chat.id, "Плохо! Чтож, давай по новой.")
        return(bot.register_next_step_handler(msg, callback=hand))       
    

bot.polling(none_stop=True, interval=0) 
