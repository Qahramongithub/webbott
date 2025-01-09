from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder,KeyboardButton


def director():
    rkb=ReplyKeyboardBuilder()
    rkb.add(
        # KeyboardButton(text="Uchrashuvlar",web_app=WebAppInfo(url="#")),
        # KeyboardButton(text="Yangi ishchi qushish",web_app=WebAppInfo(url='https://127.0.0.1:8000/admin/')),
    )
    rkb.adjust(1,1)
    return rkb.as_markup(resize_keyboard=True)

def employee():
    rkb=ReplyKeyboardBuilder()
    rkb.add(
        # KeyboardButton(text="Uchrashuvlar",web_app=WebAppInfo(url="#")),
    )
    rkb.adjust(1)
    return rkb.as_markup(resize_keyboard=True)
