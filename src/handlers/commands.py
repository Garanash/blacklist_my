from telebot.async_telebot import AsyncTeleBot
from src.utils.keyboards import inline_menu


def register_handlers(bot: AsyncTeleBot):
    @bot.message_handler(commands=['start'])
    async def start_cmd(message):
        with open('img/logo.png', 'rb') as photo:
            await bot.send_photo(
            message.chat.id,
            photo,
            ""
            "🌟 <b>Добро пожаловать в бот отзывов!</b>\n\n"
            "Вы можете оставить отзыв о заведении или услуге в любом удобном формате:\n\n"
            "🎥 <b>Кружок (видео заметка)</b>\n"
            "🎙 <b>Голосовое сообщение</b>\n"
            "📸 <b>Фото</b>\n"
            "📄 <b>Документ</b>\n"
            "💬 <b>Или просто текстом</b>\n\n"
            "📌 Ваше сообщение будет отправлено на модерацию, и вскоре вы увидите его в канале.\n\n"
            "❗ <b>Важно:</b>\n\n"
            "При написании отзывов просим воздержаться от:\n"
            "🚫 <b>Ненормативной лексики</b>\n"
            "🚫 <b>Неприличных жестов (ну мы же культурные... почти 😉)</b>\n\n"
            "<b>Спасибо за ваши отзывы! 💙</b>",
            parse_mode='HTML',
            reply_markup=inline_menu()
        )

    @bot.message_handler(commands=['help'])
    async def help_cmd(message):
        await bot.send_message(message.chat.id, "Это помощь!")