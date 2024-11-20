import telebot
from telebot import types
token = '7792408011:AAEZKlxr5KchQPOhR5O8VPTC7M0prW2uhV4';
bot = telebot.TeleBot(token);  


#7729336143:AAFs3fKMgC7PDEhmwSm1-ZChBdg9alfsHcs -1    7792408011:AAEZKlxr5KchQPOhR5O8VPTC7M0prW2uhV4 -2
#Приветсвие
@bot.message_handler(commands=['start', 'button'])
def welcome(message):
    chat_id = message.chat.id
    text = message.text
    msg = bot.send_message(message.chat.id, "Привет, я бот, нажми кнопку, чтобы ввести своё сообщение")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Ввести сообщение")
    markup.add(item1)
    if message.text == 'Ввести сообщение':
        bot.register_next_step_handler(msg, callback=send)

@bot.message_handler(commands=['button'])
def send(message):
        owner_id = 5426110205
        chat_id = message.chat.id
        text = message.text
        msg =  bot.send_message(message.chat.id, "Стоит ли отправить Твоё сообщение ?")
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Да")
        item2=types.KeyboardButton("Нет")
        markup.add(item1, item2)	
def reply(message):

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Да")
        item2=types.KeyboardButton("Нет")
        markup.add(item1, item2)
        owner_id = 5426110205
        chat_id = message.chat.id
        text = message.text
        if message.text =="Да":
            bot.reply_to(message.chat.id, "Хорошо! Сообщение отправлено!")
            bot.forward_message(text, chat_id, owner_id)
        elif message.text == "Нет":
            bot.reply_to(message.chat.id, "Плохо! Чтож, давай по новой.")
            return(bot.register_next_step_handler(message.text, next))
        

bot.polling(none_stop=True, interval=0) 
