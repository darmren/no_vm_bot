import asyncio
import os
import logging
import aiogram
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


@dp.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Hello!")


@dp.message(F.text)
async def echo_handler(msg: Message):
    text = msg.text
    await msg.answer(text)

if __name__ == "__main__":
    asyncio.run(main())