from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

MANAGER_USERNAME = "sup_FB_shop"

def main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👤 Аккаунты FB", callback_data="section_1")],
        [InlineKeyboardButton(text="💳 Виртуальные карты", callback_data="section_2")],
        [InlineKeyboardButton(text="🌐 Прокси", callback_data="section_3")],
        [InlineKeyboardButton(text="📦 Комплекс для начинающего баера", callback_data="section_4")],
        [InlineKeyboardButton(text="🛒 Перейти к покупке !!!", callback_data="section_5")],
    ])

def section_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📩 Связь с менеджером", url=f"https://t.me/{MANAGER_USERNAME}")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")],
    ])
