from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.hendlers.state import DirectorsState
director_router = Router()


@director_router.message(F.text=="Yangi ishchi qushish",DirectorsState.director)
async def director(message: Message,state:FSMContext):
    await message.answer("Ishchi ismini kiriting !")
    await state.set_state(DirectorsState.name)

@director_router.message(DirectorsState.name)
async def director(message: Message,state:FSMContext):
    await message.answer("Ishchi telepon raqamini kiriting !")

