import json
import telebot
from telebot import types

from menues import main_menu, feedback_menu, price_menu, level_menu, get_level_and_back_buttons, tariff_menu
from config import BOT_TOKEN
from textmsgs import about_school, faq_text, get_free_less_text
from textmsgs import tariff_online_text, feedback_text, welcome, certificat_text, network_text, price_text
from textmsgs import online_course_text, offline_course_text, individual_text, marafon_text, tariff_text

import random


bot = telebot.TeleBot(BOT_TOKEN)


class CheckText:
    def __init__(self, message):
        self.text = message.text
        self.chat_id = message.chat.id

    # count - кол-во фотографий, callback_string - каталог с фото
    def text_pages(self, callback_string, count):
        page = 1
        markup = types.InlineKeyboardMarkup()

        # callback в формате json
        j_data_up = {"method": callback_string,
                     "NumberPage": page + 1,
                     "CountPage": count
                     }

        markup.add(types.InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
        markup.add(types.InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                   types.InlineKeyboardButton(text=f'▶️',
                                              callback_data=json.dumps(j_data_up)))

        bot.send_photo(self.chat_id, open(f'pictures/aboutStudy/{page}.jpg', 'rb'),
                       caption=f'Страница {page} из {count}', reply_markup=markup)

    def check_school_text(self):
        if self.text == '🎓Узнать про обучение и школу SEIKO':
            markup = types.InlineKeyboardMarkup(row_width=1)
            b1 = types.InlineKeyboardButton("💾Скачать презентацию о школе", callback_data="presentation")
            b2 = types.InlineKeyboardButton("💬Задать вопрос", url='https://t.me/yana_seiko_centre')
            b3 = types.InlineKeyboardButton("🔙Назад", callback_data="back")
            markup.add(b1, b2, b3)

            bot.send_message(self.chat_id, text=about_school, parse_mode='MarkdownV2',
                             reply_markup=markup)
            #bot.send_document(self.chat_id, open("description.pdf", "rb"))

    def check_faq_text(self):
        if self.text == '️❓FAQ':
            bot.send_message(self.chat_id, text=faq_text, parse_mode='MarkdownV2',
                             reply_markup=feedback_menu())

    def check_tariff_text(self):
        if self.text == '💎Тарифы':
            bot.send_message(self.chat_id, text=tariff_text, parse_mode='MarkdownV2',
                             reply_markup=tariff_menu())

    def check_price_text(self):
        if self.text == '💰Цены':
            bot.send_photo(self.chat_id,open('pictures/price_info.jpg', 'rb'),
                           caption=price_text, parse_mode="MarkdownV2", reply_markup=price_menu())

    def check_get_free_less(self):
        if self.text == '📅Записаться на пробное занятие':
            bot.send_message(self.chat_id, text=get_free_less_text, parse_mode='html',
                             reply_markup=get_level_and_back_buttons())

    def check_feedback_text(self):
        if self.text == '📢Связаться':
            bot.send_message(self.chat_id, text=feedback_text, parse_mode='MarkdownV2',
                             reply_markup=get_level_and_back_buttons())

    def check_certificat_text(self):
        if self.text == '📝Сертификаты и справки о часах':
            bot.send_photo(self.chat_id, open("pictures/150hourCertificate.JPG", "rb"),
                           caption=certificat_text, parse_mode='MarkdownV2',
                           reply_markup=main_menu())

    def check_network_text(self):
        if self.text == '🔗Соц. сети':
            bot.send_message(self.chat_id, text=network_text, parse_mode='html',
                             reply_markup=main_menu())

def check_text(message):
    m = CheckText(message)
    m.check_school_text()
    m.check_faq_text()
    m.check_price_text()
    m.check_get_free_less()
    m.check_feedback_text()
    m.check_certificat_text()
    m.check_network_text()
    m.check_tariff_text()


