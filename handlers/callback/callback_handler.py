from aiogram import types
from aiogram.fsm.context import FSMContext

from handlers.FSM.fsm_states import Form

from config import first_question_text, complite_text, admin_id, admin_req_text, \
                   start_message_text, welcome_text, main_bot_link, info_channel_link, \
                   chat_join_link, admin_confirm_text, cancle_user_text

from handlers.keyboards.admin_panel import admin_req_menu
from handlers.keyboards.user_keyboard import main_request_menu
from handlers.scripts.text_handlers import generate_finish_req_message


"""
Хендлер callback'ов

"""

async def call_back(callback: types.CallbackQuery, state: FSMContext):
    chat_id = callback.from_user.id
    name = callback.from_user.username
    bot = callback.bot
    msg = callback.message.message_id

    if callback.data == "start_req":
        await callback.message.answer(text=first_question_text)
        await state.set_state(Form.first_question)

    elif callback.data == "complite":
        await callback.bot.edit_message_text(chat_id=chat_id, text=complite_text, message_id=msg)

        data = await state.get_data()

        msg = generate_finish_req_message(data.items())  

        #     ^^^  фунция генерирующая текст итоговой анкеты состоящий из ответов пользователей
        
        await bot.send_message(admin_id, text=admin_req_text.format(name, chat_id, msg), reply_markup=admin_req_menu(chat_id))

        await state.clear()

    elif callback.data == "cancle":
        await state.clear()
        await callback.message.answer(text=start_message_text, reply_markup=main_request_menu())


    elif "admin_cancle_user_" in callback.data:
        user_id  = callback.data.split('_')[3]

        #           ^^^ получение id юзера из callback'а для отправки ответа на анкету

        await bot.send_message(chat_id=user_id, text=cancle_user_text)

        await bot.delete_message(chat_id, msg)

    elif "admin_confirm_user" in callback.data:
        user_id  = callback.data.split('_')[3]

        await bot.send_message(chat_id=user_id, text=welcome_text.format(chat_join_link, main_bot_link, info_channel_link))
        await callback.answer(text=admin_confirm_text)

        await bot.delete_message(chat_id, msg)


