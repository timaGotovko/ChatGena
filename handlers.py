from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards import main_keyboard, section_keyboard

router = Router()

MAIN_TEXT = (
    "👋 Добро пожаловать!\n\n"
    "Выберите интересующий раздел:"
)

SECTIONS = {
    "section_1": "📌 <b>Раздел 1</b>\n\nЗдесь информация раздела 1.",
    "section_2": "📌 <b>Раздел 2</b>\n\nЗдесь информация раздела 2.",
    "section_3": "📌 <b>Раздел 3</b>\n\nЗдесь информация раздела 3.",
    "section_4": "📌 <b>Раздел 4</b>\n\nЗдесь информация раздела 4.",
    "section_5": "📌 <b>Раздел 5</b>\n\nЗдесь информация раздела 5.",
}


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(MAIN_TEXT, reply_markup=main_keyboard())


@router.callback_query(F.data.startswith("section_"))
async def show_section(callback: CallbackQuery):
    text = SECTIONS.get(callback.data, "Раздел не найден.")
    await callback.message.edit_text(text, reply_markup=section_keyboard(), parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(MAIN_TEXT, reply_markup=main_keyboard())
    await callback.answer()
