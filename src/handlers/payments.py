from telebot.async_telebot import AsyncTeleBot

def register_handlers(bot: AsyncTeleBot):
    pass
    # @bot.message_handler(commands=['buy'])
    # async def buy_command(message):
    #     await bot.send_invoice(
    #         chat_id=message.chat.id,
    #         title="Покупка",
    #         description="Тестовый товар",
    #         invoice_payload="test",
    #         provider_token="PAYMENT_TOKEN",
    #         currency="RUB",
    #         prices=[{"label": "Руб", "amount": 10000}]
    #     )
    #
    # @bot.pre_checkout_query_handler(func=lambda query: True)
    # async def pre_checkout(pre_checkout_query):
    #     await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)