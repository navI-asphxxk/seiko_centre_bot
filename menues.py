from telebot import types


def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    b1 = types.KeyboardButton(text='🎓Узнать про обучение и школу SEIKO')
    b2 = types.KeyboardButton(text='👩🏻‍🏫Узнать про школу SEIKO')
    b3 = types.KeyboardButton(text='️❓FAQ')
    b4 = types.KeyboardButton(text='💎Тарифы')
    b9 = types.KeyboardButton(text='💰Цены')
    b5 = types.KeyboardButton(text='📝Сертификаты и справки о часах')
    b6 = types.KeyboardButton(text='📅Записаться на пробное занятие')
    b7 = types.KeyboardButton(text='📢Связаться')
    b8 = types.KeyboardButton(text='🔗Соц. сети')


    markup.add(b1)
    #markup.add(b2)
    markup.add(b3, b4, b9)
    markup.add(b5)
    markup.add(b7, b8)

    return markup

def feedback_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton("📅Записаться на пробное занятие", url="https://t.me/yana_seiko_centre")
    b2 = types.InlineKeyboardButton("🥇Узнать свой уровень", callback_data="getLevel")
    b3 = types.InlineKeyboardButton("💬Задать вопрос", url='https://t.me/yana_seiko_centre')
    b4 = types.InlineKeyboardButton("🔙Назад", callback_data="back")

    markup.add(b1, b2, b3, b4)
    
    return markup

def get_level_and_back_buttons():
    markup = types.InlineKeyboardMarkup(row_width=1)
    b2 = types.InlineKeyboardButton("🥇Узнать свой уровень", callback_data="getLevel")
    b4 = types.InlineKeyboardButton("🔙Назад", callback_data="back")

    markup.add(b2, b4)

    return markup

def level_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    b1 = types.InlineKeyboardButton("N5", callback_data="n5")
    b2 = types.InlineKeyboardButton("N5+++", callback_data="n5Plus")
    b3 = types.InlineKeyboardButton("N4", callback_data="n4")
    b4 = types.InlineKeyboardButton("N4++", callback_data="n4Plus")
    b5 = types.InlineKeyboardButton("N3", callback_data="n3")
    b6 = types.InlineKeyboardButton("N3++", callback_data="n3Plus")
    b7 = types.InlineKeyboardButton("N2", callback_data="n2")
    b8 = types.InlineKeyboardButton("N2+++", callback_data="n2Plus")
    b9 = types.InlineKeyboardButton("🔙Назад", callback_data="back")

    markup.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)

    return markup


def price_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    b1 = types.InlineKeyboardButton("Online Курсы", callback_data="onlineCourse")
    b2 = types.InlineKeyboardButton("Offline Курсы в Казани", callback_data="offlineCourse")
    b3 = types.InlineKeyboardButton("Индивидуальные занятия", callback_data="individual")
    b5 = types.InlineKeyboardButton("Марафоны", callback_data="marafon")
    b6 = types.InlineKeyboardButton("🔙Назад", callback_data="back")

    markup.add(b1, b2)
    markup.add(b3, b5, b6)

    return markup

def tariff_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton("Online тарифы", callback_data="onlineTariff")
    b2 = types.InlineKeyboardButton("Offline тарифы", callback_data="offlineTariff")
    b3 = types.InlineKeyboardButton("🔙Назад", callback_data="back")

    markup.add(b1, b2, b3)

    return markup

