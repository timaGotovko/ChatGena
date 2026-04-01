import asyncio
import os

from aiogram import Bot, Dispatcher

from handlers import router

TOKEN = os.getenv("BOT_TOKEN", "8796427868:AAE9jWozjA-sIGADeXU9xdJT2aghpUG0-qw")


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
