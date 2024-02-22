from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import confirm_user_btm, cancle_user_btm

"""
Хендлер админской клавиатуры

admin_req_menu(id) --> Клавиатура обработки заявки  " принять / отклонить "

в функцию передается id пользователя создавшего анкету для образования callback даты с user_id
для последующей отправки ответа пользователю  " заявка принята / отклонен "

"""

def admin_req_menu(id):
    builder = InlineKeyboardBuilder()

    builder.add(types.InlineKeyboardButton (
        text=confirm_user_btm,
        callback_data=f"admin_confirm_user_{id}"
        )           
    )

    builder.add(types.InlineKeyboardButton (
        text=cancle_user_btm,
        callback_data=f"admin_cancle_user_{id}"
        )           
    )

    return builder.as_markup()