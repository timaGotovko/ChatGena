from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

MANAGER_USERNAME = "manager_username"  # Замени на реальный username менеджера

def main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1️⃣ Раздел 1", callback_data="section_1")],
        [InlineKeyboardButton(text="2️⃣ Раздел 2", callback_data="section_2")],
        [InlineKeyboardButton(text="3️⃣ Раздел 3", callback_data="section_3")],
        [InlineKeyboardButton(text="4️⃣ Раздел 4", callback_data="section_4")],
        [InlineKeyboardButton(text="5️⃣ Раздел 5", callback_data="section_5")],
    ])

def section_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📩 Связь с менеджером", url=f"https://t.me/{MANAGER_USERNAME}")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")],
    ])
