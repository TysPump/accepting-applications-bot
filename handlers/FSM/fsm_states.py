from aiogram.fsm.state import StatesGroup, State

"""
FSM Class

"""

class Form(StatesGroup):
    first_question = State()
    
    second_question = State()
    thrid_question = State()

    last_question = State()
