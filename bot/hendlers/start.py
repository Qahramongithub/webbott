from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from bot.button.button import director, employee
from aiogram.fsm.context import FSMContext
from bot.hendlers.state import DirectorsState

start_router = Router()


@start_router.message(CommandStart())
async def start_bot(message: Message, state: FSMContext):
    qr_id = message.text.split()[-1]
    if qr_id in 'admin':
        await message.answer("Menu !", reply_markup=director())
        await state.set_state(DirectorsState.directors)
    elif qr_id in 'employees':
        await message.answer("Menu !", reply_markup=employee())
    else:
        await message.answer("Error")
