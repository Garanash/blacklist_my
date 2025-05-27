from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("/help", 'second')
    return keyboard

def inline_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Помощь", callback_data="button1"))
    return markup

def inline_menu_moderator():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("✅ Постим", callback_data="button2"))
    markup.add(InlineKeyboardButton("⛔️ Не постим", callback_data="button3"))
    return markup