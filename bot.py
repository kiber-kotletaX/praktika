from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from db import Database

# Указываем токен (лучше хранить в переменной окружения)
TOKEN = '7813027632:AAFk2lYkys_jbWznEhSB8tCWGSTMI08Xpao'  # Замените на ваш токен
application = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Используйте команду /znak для выбора знака.")

async def znak(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = Database()
    statias = db.get_znak()

    keyboard = []
    if statias:  # Проверка на наличие статей
        for statia in statias:
            keyboard.append([InlineKeyboardButton(statia['name'], callback_data=f"statia_{statia['id']}")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Выберите знак:", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Нет доступных знаков.")

async def statia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query:
        await query.answer()
        znak_id = int(query.data.split('_')[1]) # Извлекаем ID из callback_data
        db = Database()
        statia = db.get_statia(znak_id)

        if statia:
            await query.message.reply_text(statia['name']) # Изменяем сообщение вместо отправки нового
        else:
            await query.message.reply_text("Статья не найдена.") # Изменяем сообщение
        


def main():
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("znak", znak))
    application.add_handler(CallbackQueryHandler(statia))

    application.run_polling()

if __name__ == '__main__':
    main()