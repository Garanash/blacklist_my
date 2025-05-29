import json

from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("/help")
    return keyboard

def inline_menu(message):
    sender_data = {
        'u_id': message.from_user.id,
        'un': message.from_user.username or '',
        'btn': 'button1'
    }
    callback_data_str = json.dumps(sender_data)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Помощь", callback_data=callback_data_str))
    return markup

def inline_menu_moderator(message):
    markup = InlineKeyboardMarkup()
    sender_data = {
        'u_id': message.from_user.id,
        'un': message.from_user.username or '',
    }
    b2 = sender_data
    b2["btn"] = 'button2'
    callback_data_str2 = json.dumps(b2)

    markup.add(InlineKeyboardButton("✅ Постим", callback_data=callback_data_str2))

    b3 = sender_data
    b3["btn"] = 'button3'
    callback_data_str3 = json.dumps(b3)

    markup.add(InlineKeyboardButton("⛔️ Не постим", callback_data=callback_data_str3))
    return markup