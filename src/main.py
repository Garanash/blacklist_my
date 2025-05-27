from telebot.async_telebot import AsyncTeleBot
from dotenv import dotenv_values
import asyncio
from handlers import commands, messages, callbacks, payments

config = dotenv_values(".env")
bot = AsyncTeleBot(config['TELEGRAM_BOT_TOKEN'])

commands.register_handlers(bot)
callbacks.register_handlers(bot)
messages.register_handlers(bot)
payments.register_handlers(bot)


async def main():
    await bot.polling(non_stop=True, interval=2, timeout=20)

if __name__ == '__main__':
    print("Бот начал работать")
    asyncio.run(main())