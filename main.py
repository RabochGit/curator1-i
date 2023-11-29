"""Строка для докуметации, согласно PEP8"""
import telebot
from telebot import types
from datetime import datetime

bot = telebot.TeleBot("6708916713:AAEFQ8z9ni7pzm90-3Ru-xq1gbxsbdMIVn4")
all_commands = ['start', 'hahaha', 'buy', 'add_name', "help"]


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Доступные команд в нашем боте:")
    for command in all_commands:
        bot.send_message(message.chat.id, f"/{command}")


@bot.message_handler(commands=['start'])
def func1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    btn3 = types.KeyboardButton("😀 Сделать заказ")
    btn4 = types.KeyboardButton("⏰ Узнать текущую дату и время")
    btn5 = types.KeyboardButton("Посмотреть команды, которые есть у бота")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id,
                     text="Приветствуем в нашем магазине!".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def process(message):
    if message.text == "👋 Поздороваться":
        bot.send_message(message.chat.id, text=f"Привет! {message.chat.first_name}")
    elif message.text == "❓ Задать вопрос":
        bot.send_message(message.chat.id, text="Эта опция пока что не доступна")
    elif message.text == "😀 Сделать заказ":
        bot.send_message(message.chat.id, text="Эта опция пока что не работает")
    elif message.text == "⏰ Узнать текущую дату и время":
        bot.send_message(message.chat.id, f"{datetime.now()}")
    elif message.text == "Вывести все комнды бота на экран":
        print("Ниже представлены доступные команды")
        for command in all_commands:
            bot.send_message(message.chat.id, f"{command}")


@bot.message_handler(commands=['hahaha'])
def func2(message):
    bot.send_message(message.chat.id, "Вывод текста на комнаду hahaha")


@bot.message_handler(commands=['buy'])
def func3(message):
    bot.send_message(message.chat.id, "Вывод текста на комнаду buy")


@bot.message_handler(commands=['add_name'])
def func4(message):
    name = input("Введите ваше имя: ")
    bot.send_message(message.chat.id, name)


bot.polling()
