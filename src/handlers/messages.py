from telebot.async_telebot import AsyncTeleBot
from dotenv import dotenv_values
from utils.keyboards import inline_menu_moderator

# config = dotenv_values(".env")
config = {"TELEGRAM_BOT_TOKEN":'8078634784:AAEA526n7O1yGaIRYNDDGr0o0yIsaPcT7jU',
            "TARGET_USER_ID" : 476409056,
            "GROUP_ID" : -1002531170702}


def register_handlers(bot: AsyncTeleBot):
    @bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'voice', 'video_note'])
    async def handle_message(message):
        # Формируем информацию об отправителе
        sender_info = (
            f"Отправитель: {message.from_user.first_name or ''} "
            f"{message.from_user.last_name or ''} "
            f"(@{message.from_user.username or 'нет username'})\n"
            f"ID: {message.from_user.id}\n\n"
        )

        if message.text:
            await bot.send_message(
                chat_id=config['TARGET_USER_ID'],
                text=message.text,
                reply_markup=inline_menu_moderator(message)
            )
        elif message.photo:
            await bot.send_photo(
                chat_id=config['TARGET_USER_ID'],
                photo=message.photo[-1].file_id,
                caption=(message.caption or ''),
                reply_markup=inline_menu_moderator(message)
            )
        elif message.video:
            await bot.send_video(
                chat_id=config['TARGET_USER_ID'],
                video=message.video.file_id,
                caption=(message.caption or ''),
                reply_markup=inline_menu_moderator(message)
            )
        elif message.document:
            await bot.send_document(
                chat_id=config['TARGET_USER_ID'],
                document=message.document.file_id,
                caption=(message.caption or ''),
                reply_markup=inline_menu_moderator(message)
            )
        elif message.voice:
            await bot.send_voice(
                chat_id=config['TARGET_USER_ID'],
                voice=message.voice.file_id,
                reply_markup=inline_menu_moderator(message)
            )
        elif message.video_note:
            await bot.send_video_note(
                chat_id=config['TARGET_USER_ID'],
                data=message.video_note.file_id,
                reply_markup=inline_menu_moderator(message)
            )
            # Для video_note отправляем отдельное текстовое сообщение с информацией
            await bot.send_message(
                chat_id=config['TARGET_USER_ID'],

                reply_markup=inline_menu_moderator(message)
            )

        await bot.reply_to(message, "Ваше сообщение отправлено на модерацию")
