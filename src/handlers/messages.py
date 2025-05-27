from telebot.async_telebot import AsyncTeleBot
from dotenv import dotenv_values
from src.utils.keyboards import inline_menu_moderator

config = dotenv_values(".env")

def register_handlers(bot: AsyncTeleBot):
    @bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'voice', 'video_note'])
    async def handle_message(message):
        if message.text:
            await bot.send_message(
                chat_id=config['TARGET_USER_ID'],
                text=message.text,
                reply_markup=inline_menu_moderator()
            )
        elif message.photo:
            await bot.send_photo(
                chat_id=config['TARGET_USER_ID'],
                photo=message.photo[-1].file_id,
                caption=message.caption,
                reply_markup=inline_menu_moderator()
            )
        elif message.video:
            await bot.send_video(
                chat_id=config['TARGET_USER_ID'],
                video=message.video.file_id,
                caption=message.caption,
                reply_markup=inline_menu_moderator()
            )
        elif message.document:
            await bot.send_document(
                chat_id=config['TARGET_USER_ID'],
                document=message.document.file_id,
                caption=message.caption,
                reply_markup=inline_menu_moderator()
            )
        elif message.voice:
            await bot.send_voice(
                chat_id=config['TARGET_USER_ID'],
                voice=message.voice.file_id,
                reply_markup=inline_menu_moderator()
            )
        elif message.video_note:
            await bot.send_video_note(
                chat_id=config['TARGET_USER_ID'],
                video_note=message.video_note.file_id,
                reply_markup=inline_menu_moderator()
            )

        await bot.reply_to(message, "Ваше сообщение отправлено на модерацию")

