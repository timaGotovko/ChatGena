from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards import main_keyboard, section_keyboard

router = Router()

MAIN_TEXT = (
    "👋 Тебя приветсвует Твой помощник в мире баинга!\n\n"
    "Магазин качественных расходников с гарантией! Мы команда которая помогает начинающим баерам уже несколько лет! С нами твой залив пройдет максимально качественно и быстро "
)

SECTIONS = {
    "section_1": (
        "👤 <b>Аккаунты FB</b>\n\n"
        "1. ⚡️ <b>КИНГ UA</b> | ТОП фарм 9-12+ месяцев | Аккаунт Facebook УКР | Ручной фарм | Интересы | Друзья | Пройдено видеоселфи | FULL комплект | 2ФА+ | ФП+ | БМ+ | ✅ Отличный аккаунт для работы в долгую — <b>25$</b>\n\n"
        "2. ⚡️ <b>КИНГ USA</b> | ТОП фарм 9-12+ месяцев | Аккаунт Facebook США | Ручной фарм | Пройдено видео селфи | FULL комплект | 2-5 ФП | 2 БМ | ✅ Топовый аккаунт для работы в долгую — <b>25$</b>\n\n"
        "3. ⚡️ <b>СЕТАП | KING USA</b> | Аккаунт FB USA + 9 USA личек | Фарм 6+ месяцев | Лимит 450$+ | 2FA+ | 1-3 Fan Page | Пройден селфи — <b>35$</b>\n\n"
        "4. ⚡️ <b>СЕТАП | KING UA (МАМКА)</b> | Аккаунт FB UA + 9 UA личек | 2FA+ | Fan Page+ | 12+ месяцев | Лимит 450$+ | Пройден селфи — <b>35$</b>\n\n"
        "5. ⚡️ <b>ВЕРИФ Бизнес Менеджер | BM</b> | Гео Европа/США | Подключен вотсап | Выдача: ссылка + почта — <b>40$</b>\n\n"
        "6. ⚡️ <b>ВЕРИФ Бизнес Менеджер | BM</b> | Гео Европа/США | Выдача: ссылка + почта — <b>40$</b>\n\n"
        "7. ⚡️ <b>КИНГ UK</b> ⭐ Гео Англия | Ручной фарм с ФП | Возраст 1 год+ | 2ФА | Почта с доступом — <b>40$</b>\n\n"
        "8. ⚡️ <b>КИНГ IT</b> ⭐ Гео Италия | Ручной фарм с ФП | Возраст 1 год+ | 2ФА | Почта с доступом — <b>40$</b>\n\n"
        "9. ⚡️ <b>КИНГ PL</b> ⭐ Гео Польша | Ручной фарм с ФП | Возраст 1 год+ | 2ФА | Почта с доступом — <b>40$</b>"
    ),
    "section_2": (
        "💳 <b>Виртуальные карты</b>\n\n"
        "1. Виртуальная карта банка — <b>Crédit Agricole</b> — <b>100$</b>\n\n"
        "2. Виртуальная карта банка — <b>Bank of America</b> — <b>120$</b>\n\n"
        "3. Виртуальная карта банка — <b>JPMorgan Chase</b> — <b>100$</b>\n\n"
        "4. Виртуальная карта банка — <b>American Express</b> — <b>90$</b>\n\n"
        "5. Виртуальная карта банка — <b>Deutsche Bank</b> — <b>80$</b>\n\n"
        "6. Виртуальная карта банка — <b>Sparkasse</b> — <b>80$</b>\n\n"
        "7. Виртуальная карта банка — <b>La Banque Postale</b> — <b>100$</b>\n\n"
        "8. Виртуальная карта — <b>BlackCatCard</b> — <b>90$</b>\n\n"
        "9. Виртуальная карта — <b>Revolut</b> — <b>100$</b>"
    ),
    "section_3": (
        "🌐 <b>Прокси</b>\n\n"
        "Раздел в разработке. Свяжитесь с менеджером для уточнения наличия."
    ),
    "section_4": (
        "📦 <b>Комплекс для начинающего баера</b>\n\n"
        "Полный пакет нужных инструментов: <b>Аккаунт FB + Виртуальная карта</b>\n\n"
        "Свяжитесь с менеджером для уточнения состава и цены."
    ),
    "section_5": (
        "🛒 <b>Перейти к покупке</b>\n\n"
        "Для оформления заказа свяжитесь с нашим менеджером — он поможет подобрать нужный товар и оформить сделку."
    ),
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
