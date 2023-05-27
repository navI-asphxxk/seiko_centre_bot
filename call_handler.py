import json
import telebot
from telebot import types

from menues import main_menu, feedback_menu, level_menu, price_menu, tariff_menu
from config import BOT_TOKEN
from textmsgs import about_school, faq_text, get_free_less_text, tariff_offline_text, error_text
from textmsgs import tariff_text, feedback_text, welcome, price_text, tariff_online_text
from textmsgs import online_course_text, offline_course_text, individual_text, marafon_text

import random


bot = telebot.TeleBot(BOT_TOKEN)


class CheckCall:
    def __init__(self, call):
        self.data = call.data
        self.chat_id = call.message.chat.id
        self.message_id = call.message.message_id

    def callback_pages(self, callback_string):
        req = self.data.split('_')
        # Обработка кнопки - скрыть
        if req[0] == 'unseen':
            try:
                bot.delete_message(self.chat_id, self.message_id)
                bot.send_message(self.chat_id, text='back', reply_markup=main_menu())
            except Exception as ex:
                print(ex)
        # Обработка кнопок - вперед и назад
        elif callback_string in req[0]:
            json_string = json.loads(req[0])
            count = json_string['CountPage']
            page = json_string['NumberPage']

            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text='Скрыть', callback_data='unseen'))

            # callback в формате json
            j_data_up = {"method": callback_string,
                         "NumberPage": page + 1,
                         "CountPage": count
                         }
            j_data_down = {"method": callback_string,
                           "NumberPage": page - 1,
                           "CountPage": count
                           }

            # markup для первой страницы
            if page == 1:
                markup.add(types.InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                           types.InlineKeyboardButton(text=f'▶️',
                                                      callback_data=json.dumps(j_data_up)))

            # markup для последнейстраницы
            elif page == count:

                markup.add(types.InlineKeyboardButton(text=f'◀️',
                                                      callback_data=json.dumps(j_data_down)),
                           types.InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))

            # markup для остальных страниц
            else:

                markup.add(types.InlineKeyboardButton(text=f'◀️',
                                                      callback_data=json.dumps(j_data_down)),
                           types.InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                           types.InlineKeyboardButton(text=f'▶️',
                                                      callback_data=json.dumps(j_data_up)))

            try:
                bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                      media=open(f'pictures/aboutStudy/{page}.jpg',
                                                                                 'rb'),
                                                                      caption=f'Страница {page} из {count}'),
                                       reply_markup=markup,
                                       chat_id=self.chat_id, message_id=self.message_id)
            except Exception as ex:
                print(ex)

    def call_back(self):
        if self.data == "back":
            try:
                bot.delete_message(self.chat_id, self.message_id)
                bot.send_message(self.chat_id, text='back', reply_markup=main_menu())
            except Exception as ex:
                print(ex)


    def call_presentation(self):
        if self.data == "presentation":
            try:
                bot.send_document(self.chat_id, open("description.pdf", "rb"), timeout=30)
            except:
                bot.send_message(self.chat_id, text=error_text)

    def call_getLevel(self):
        if self.data == "getLevel":
            bot.send_photo(self.chat_id, open("pictures/levelInfo.jpg", "rb"), reply_markup=level_menu())

    def call_back_to_levels(self):
        if self.data == "backToLevels":
            try:
                bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                      media=open('pictures/levelInfo.jpg', 'rb')),
                                       reply_markup=level_menu(),
                                       chat_id=self.chat_id, message_id=self.message_id)
            except Exception as ex:
                print(ex)

    def call_check_level(self):
        markup = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton("🔙Назад", callback_data="backToLevels")
        markup.add(b1)

        if self.data == "n5":
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                              media=open('pictures/levels/n5.jpg', 'rb')),
                                   reply_markup=markup,
                                   chat_id=self.chat_id, message_id=self.message_id)

        if self.data == "n5Plus":
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                  media=open('pictures/levels/n5+.jpg', 'rb')),
                                   reply_markup=markup,
                                   chat_id=self.chat_id, message_id=self.message_id)

        if self.data == "n4":
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                  media=open('pictures/levels/n4.jpg', 'rb')),
                                   reply_markup=markup,
                                   chat_id=self.chat_id, message_id=self.message_id)

        if self.data == "n4Plus":
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                  media=open('pictures/levels/n4+.jpg', 'rb')),
                                   reply_markup=markup,
                                   chat_id=self.chat_id, message_id=self.message_id)

        if self.data == "n3":
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                  media=open('pictures/levels/n3.jpg', 'rb')),
                                   reply_markup=markup,
                                   chat_id=self.chat_id, message_id=self.message_id)

        if self.data == "n3Plus":
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                  media=open('pictures/levels/n3+.jpg', 'rb')),
                                   reply_markup=markup,
                                   chat_id=self.chat_id, message_id=self.message_id)

        if self.data == "n2":
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                  media=open('pictures/levels/n2.jpg', 'rb')),
                                   reply_markup=markup,
                                   chat_id=self.chat_id, message_id=self.message_id)

        if self.data == "n2Plus":
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                  media=open('pictures/levels/n2+.jpg', 'rb')),
                                   reply_markup=markup,
                                   chat_id=self.chat_id, message_id=self.message_id)

    def call_back_to_price(self):
        if self.data == "backToPrice":
            try:
                bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                      media=open('pictures/price_info.jpg', 'rb'),
                                                                      caption=price_text, parse_mode='MarkdownV2'),
                                       reply_markup=price_menu(),
                                       chat_id=self.chat_id, message_id=self.message_id)
            except Exception as ex:
                print(ex)

    def call_check_price(self):
        markup = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton("🔙Назад", callback_data="backToPrice")
        markup.add(b1)

        if self.data == "onlineCourse":
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                              media=open('pictures/prices/online.jpg', 'rb'),
                                                              caption=online_course_text, parse_mode='MarkdownV2'),
                                   reply_markup=markup,
                                   chat_id=self.chat_id, message_id=self.message_id)

        if self.data == "offlineCourse":
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                  media=open('pictures/prices/offline.jpg', 'rb'),
                                                                  caption=offline_course_text, parse_mode='MarkdownV2'),
                                   reply_markup=markup,
                                   chat_id=self.chat_id, message_id=self.message_id)

        if self.data == "individual":
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                  media=open('pictures/prices/individual.jpg', 'rb'),
                                                                  caption=individual_text, parse_mode='MarkdownV2'),
                                   reply_markup=markup,
                                   chat_id=self.chat_id, message_id=self.message_id)

        if self.data == "marafon":
            bot.edit_message_media(media=telebot.types.InputMedia(type='photo',
                                                                  media=open('pictures/prices/marafon.jpg', 'rb'),
                                                                  caption=marafon_text, parse_mode='MarkdownV2'),
                                   reply_markup=markup,
                                   chat_id=self.chat_id, message_id=self.message_id)

    def call_back_to_tariff(self):
        if self.data == "backToTariff":
            try:
                bot.edit_message_text(text=tariff_text, parse_mode='MarkdownV2', reply_markup=tariff_menu(),
                                      chat_id=self.chat_id, message_id=self.message_id)
            except Exception as ex:
                print(ex)

    def call_online_offline_tariff(self):
        markup = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton("🔙Назад", callback_data="backToTariff")
        markup.add(b1)

        if self.data == "onlineTariff":
            bot.edit_message_text(text=tariff_online_text, parse_mode='MarkdownV2', reply_markup=markup,
                                  chat_id=self.chat_id, message_id=self.message_id)

        if self.data == "offlineTariff":
            bot.edit_message_text(text=tariff_offline_text, parse_mode='MarkdownV2', reply_markup=markup,
                                  chat_id=self.chat_id, message_id=self.message_id)


def check_call(call):
    m = CheckCall(call)
    m.callback_pages('aboutStudy')
    m.call_back()
    m.call_presentation()
    m.call_getLevel()
    m.call_back_to_levels()
    m.call_check_level()
    m.call_back_to_price()
    m.call_check_price()
    m.call_online_offline_tariff()
    m.call_back_to_tariff()
