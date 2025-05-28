from telebot.async_telebot import AsyncTeleBot
from telebot.types import CallbackQuery
from utils.keyboards import inline_menu_moderator, inline_menu
from dotenv import dotenv_values

config = dotenv_values(".env")

def register_handlers(bot: AsyncTeleBot):
    @bot.callback_query_handler(func=lambda call: True)
    async def handle_callback(call: CallbackQuery):
        text_rep = ("ℹ️ Как оставить отзыв\n\n"
                "<b>Ты можешь отправить отзыв в любом удобном формате:\n\n"
                "🎥 Видео-кружок\n🎙 Голосовое сообщение\n📸 Фото\n📄 Документ\n💬 Текст</b>\n\n"
                "Все отзывы проходят модерацию и появляются в канале после проверки.\n\n"
                "❗️Пожалуйста, не используй:<b>\n"
                "🚫 Ненормативную лексику\n"
                "🚫 Неприличные жесты\n\n"
                "Спасибо, что делишься своим мнением! 💙</b>")
        if call.data == 'button1':
            await bot.send_message(chat_id=call.message.chat.id, text=text_rep, parse_mode='HTML',reply_markup=inline_menu())
        elif call.data == 'button2':
            if call.message.text:
                await bot.send_photo(
                    chat_id=config['GROUP_ID'],
                    photo=call.message.photo[-1].file_id,
                    caption=call.message.caption,
                    reply_markup=inline_menu_moderator()
                )
            elif call.message.photo:
                await bot.send_photo(
                    chat_id=config['GROUP_ID'],
                    photo=call.message.photo[-1].file_id,
                    caption=call.message.caption,
                )
            elif call.message.video:
                await bot.send_video(
                    chat_id=config['GROUP_ID'],
                    video=call.message.video.file_id,
                    caption=call.message.caption,
                )
            elif call.message.document:
                await bot.send_document(
                    chat_id=config['GROUP_ID'],
                    document=call.message.document.file_id,
                    caption=call.message.caption,
                )
            elif call.message.voice:
                await bot.send_voice(
                    chat_id=config['GROUP_ID'],
                    voice=call.message.voice.file_id,
                )
            elif call.message.video_note:
                await bot.send_video_note(
                    chat_id=config['GROUP_ID'],
                    video_note=call.message.video_note.file_id,
                )
            # обычный комментарий



        elif call.data == 'button3':
            await bot.send_message(
                chat_id=call.message.chat.id,
                text='Ваше сообщение не прошло модерацию, пожалуйста придерживайтесь правил группы(нет мата и нет неприличным жестам)',
                parse_mode='Markdown'  # Опционально: для форматирования
            )

        # Также можно ответить на callback, чтобы убрать часики у кнопки
        await bot.answer_callback_query(call.id)