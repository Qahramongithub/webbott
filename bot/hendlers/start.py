from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from bot.button.button import director, employee
from aiogram.fsm.context import FSMContext
from bot.hendlers.state import DirectorsState

start_router = Router()

@start_router.message(CommandStart())
async def start_bot(message: Message, state: FSMContext):
    await message.answer("#")
