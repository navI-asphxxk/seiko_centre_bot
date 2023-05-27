import telebot
from telebot import types

from menues import main_menu, feedback_menu, price_menu, level_menu
from config import BOT_TOKEN
from textmsgs import about_school, faq_text, get_free_less_text
from textmsgs import tariff_text, feedback_text, welcome, price_text
from textmsgs import online_course_text, offline_course_text, individual_text, marafon_text

from text_handler import check_text
from call_handler import check_call

import random


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_photo(message.chat.id, open('pictures/welcome.png', 'rb'),
                   caption=welcome, reply_markup=main_menu(), parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_text(message):
    check_text(message)


@bot.callback_query_handler(func=lambda call: True)
def check_callback_data(call):
    # исправляет значок загрузки
    if call.message:
        bot.answer_callback_query(callback_query_id=call.id)

        check_call(call)


bot.polling(none_stop=True)