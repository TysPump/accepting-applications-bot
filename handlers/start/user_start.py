from aiogram import types

from config import start_message_text
from handlers.keyboards.user_keyboard import main_request_menu

"""
Хендлер обрабатывающий команду start

"""

async def get_start(message: types.Message):
    user_id = message.from_user.id

    await message.answer(start_message_text, reply_markup=main_request_menu())