from aiogram import types
from aiogram.fsm.context import FSMContext

from app.keyboards.reply import transport_type
from app.utils.statesform import LoadTrip


async def load_new_trip(message: types.Message, state: FSMContext):
    await message.answer(f"Send start town")
    await state.set_state(LoadTrip.FIRST_PLACE)


async def get_first_place(message: types.Message, state: FSMContext):
    await message.answer(f"The first place is '{message.text}'\r\nSend finish town")
    await state.update_data(start_place=message.text)
    await state.set_state(LoadTrip.LAST_PLACE)


async def get_last_place(message: types.Message, state: FSMContext):
    await message.answer(f"The last place is '{message.text}'\r\nSelect type of transport", reply_markup=transport_type)
    await state.update_data(finish_place=message.text)
    await state.set_state(LoadTrip.TRANSPORT_TYPE)


async def get_transport_type(message: types.Message, state: FSMContext):
    await message.answer(f"Type of transport is '{message.text}'")
    await state.update_data(transport_type=message.text)
    context_data = await state.get_data()
    await message.answer(f"This data will be added:\r\n{str(context_data)}")
    await state.clear()
