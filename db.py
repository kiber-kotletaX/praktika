import sqlite3
import telebot


API_TOKEN = '7729336143:AAFs3fKMgC7PDEhmwSm1-ZChBdg9alfsHcs'
DB_FILE_NAME = 'db.sqlite'


def create_connect():
    return sqlite3.connect('tgbot_db')


def init_db():
    # Создание базы и таблицы
    with create_connect() as connect:
        connect.execute('''
            CREATE TABLE IF NOT EXISTS Message (
                id      INTEGER  PRIMARY KEY,
                text    TEXT  NOT NULL   
            );
        ''')

        connect.commit()


def add_message(user_id, message):
    with create_connect() as connect:
        connect.execute(
            'INSERT INTO Message (text) VALUES (?, ?)', (user_id, message)
        )
        connect.commit()