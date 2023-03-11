from aiogram import types

from app.keyboards.reply import get_reply_keyboard


async def get_start(message: types.Message):
    await message.answer("Hello!")


async def personal_data(message: types.Message):
    await message.answer(f"What do you want to get?", reply_markup=get_reply_keyboard())
