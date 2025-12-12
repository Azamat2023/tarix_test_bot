# from aiogram.fsm.state import StatesGroup, State

# class AdminStates(StatesGroup):
#     enter_phone = State()
#     enter_test_code = State()
#     enter_answers = State()

# class UserStates(StatesGroup):
#     enter_test_code = State()
#     enter_answers = State()

# === states.py ===

from aiogram.fsm.state import StatesGroup, State

class AdminStates(StatesGroup):
    enter_phone = State()
    enter_test_code = State()
    enter_answers = State()

class UserStates(StatesGroup):
    enter_test_code = State()
    enter_answers = State()
