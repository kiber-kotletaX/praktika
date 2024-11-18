import telebot;
import db
import types
bot = telebot.TeleBot('7729336143:AAFs3fKMgC7PDEhmwSm1-ZChBdg9alfsHcs');  #7729336143:AAFs3fKMgC7PDEhmwSm1-ZChBdg9alfsHcs -1    7792408011:AAEZKlxr5KchQPOhR5O8VPTC7M0prW2uhV4 -2
owner_id = 5426110205

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет, '+ message.from_user.first_name + " я - бот для отправки сообщений")
    bot.register_next_step_handler(message.chat.id, callback=msg_h)
    
def msg_h(message):
    msg = bot.send(message, "Напишите ваше сообщение: ")
    bot.register_next_step_handler(msg, bot_send)

def bot_send(message):
    bot.send(message, "Сообщение отправлено!")
    bot.forward_message(owner_id, message.chat.id, message.message_id)


bot.polling(none_stop=True, interval=0)