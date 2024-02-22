from aiogram import types
from aiogram.fsm.context import FSMContext

from handlers.FSM.fsm_states import Form
from config import second_question_text, thrid_question, last_step_text
from handlers.scripts.text_handlers import generate_finish_req_message
from handlers.keyboards.user_keyboard import confirm_req_menu


"""
Хендлер обрабатывающий fsm_states

"""

async def state_one(message: types.Message, state: FSMContext):
    await state.update_data(first_q = message.text)
    await message.answer(
        text=second_question_text
    )

    await state.set_state(Form.second_question)


async def state_two(message: types.Message, state: FSMContext):
    await state.update_data(second_q = message.text)
    await message.answer(
        text=thrid_question
    )

    await state.set_state(Form.thrid_question)



async def state_thr(message: types.Message, state: FSMContext):
    await state.update_data(thr_q = message.text)

    data = await state.get_data()

    await message.answer(
        text=last_step_text.format(generate_finish_req_message(data.items())),
        reply_markup=confirm_req_menu()
    )