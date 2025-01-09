from aiogram.fsm.state import StatesGroup ,State
class DirectorsState(StatesGroup):
    director = State()
    name = State()
    phone = State()