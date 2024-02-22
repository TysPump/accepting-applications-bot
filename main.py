import asyncio
import logging
from aiogram import Bot, types, Dispatcher, F
from aiogram.filters.command import Command, CommandObject

from config import bot_token
from handlers.start.user_start import get_start
from handlers.callback.callback_handler import call_back
from handlers.FSM.user_states import state_one, state_thr, state_two
from handlers.FSM.fsm_states import Form


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s -"
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        
                        )

    bot = Bot(token=bot_token, parse_mode='HTML')


    dp = Dispatcher()

    dp.message.register(get_start, Command(commands=['start']))

    dp.callback_query.register(call_back)

    dp.message.register(state_one, Form.first_question)
    dp.message.register(state_two, Form.second_question)
    dp.message.register(state_thr, Form.thrid_question)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ in "__main__":
    asyncio.run(start())