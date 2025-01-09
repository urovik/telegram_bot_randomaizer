import asyncio
from aiogram import Bot,Dispatcher
from app.handlers import router as route_hand
from config import TOKEN


bot = Bot(token=TOKEN)

dp = Dispatcher()

async def main():
    dp.include_router(router = route_hand)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())