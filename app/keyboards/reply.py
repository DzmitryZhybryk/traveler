from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


select_language = types.ReplyKeyboardMarkup(keyboard=[
    [
        types.KeyboardButton(
            text="ru"
        ),
        types.KeyboardButton(
            text="en"
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Select language")


transport_type = types.ReplyKeyboardMarkup(keyboard=[
    [
        types.KeyboardButton(
            text='Air'
        ),
        types.KeyboardButton(
            text='Ground'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Select transport type")


def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text="location", request_location=True)
    keyboard_builder.button(text="contact", request_contact=True)
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True,
                                      input_field_placeholder="Send location or phone number")
