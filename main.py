
import sqlite3


import telebot
from telebot import types

bot = telebot.TeleBot('5764317978:AAHGYsPsCziPutNohfL2DZNclSDgQlA-8gU');


bot.send_message(1060639508,"Это спам от Лиса. Хихихи.")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        conn = sqlite3.connect('UsersDb.db')

        cur = conn.cursor()
        cur.execute("SELECT NAME FROM USERS WHERE ID= ? ", (message.from_user.id,))

        one_result = cur.fetchone()

        if one_result is None:
            bot.send_message(message.from_user.id, "Привет, . Как тебя зовут?")
            test_button(message.from_user.id)
            bot.register_next_step_handler(message, get_name)
        else:
            bot.send_message(message.from_user.id, "Привет "+str(one_result[0]))
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def get_name(message):
    conn = sqlite3.connect('UsersDb.db')

    name = message.text
    cur2 = conn.cursor()

    user = (message.from_user.id,name)
    cur2.execute('INSERT INTO USERS VALUES(?,?)', user)
    conn.commit()
    bot.send_message(message.from_user.id, "Привет, "+str(message.text))

def test_button(userId):
    keyboard = types.InlineKeyboardMarkup()
    testButton = types.InlineKeyboardButton('Сделай тык', url='https://www.instagram.com/kkkkkkkkkkkkklkkkkklk/')
    keyboard.add(testButton)
    bot.send_message(userId, 'фыр фыр', reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)