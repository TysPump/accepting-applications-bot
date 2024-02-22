from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import request_btm_text, complite_btm_text, cancle_btm_text

"""
Хендлер пользовательских клавиатур.

confirm_req_menu() --> Клавиатура подтверждения заявки

main_request_menu() --> Кнопка "заполнить заявку"

"""

def main_request_menu():
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton (
        text = request_btm_text,
        callback_data = "start_req"
        )
    )

    return builder.as_markup()


def confirm_req_menu():
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton (
        text = complite_btm_text,
        callback_data="complite"

        )           
    )

    builder.add(types.InlineKeyboardButton (
        text = cancle_btm_text,
        callback_data="cancle"

        )           
    )

    return builder.as_markup()