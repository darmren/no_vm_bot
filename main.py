import asyncio
import os
import logging
import aiogram
from aiogram import html
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types.voice import Voice
from aiogram.enums import ParseMode
from aiogram.types import chat_administrator_rights
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"), parse_mode=ParseMode.MARKDOWN)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


@dp.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        f"Hello, {html.bold(html.quote(msg.from_user.full_name))}",
        parse_mode=ParseMode.HTML
    )


@dp.message(F.voice)
async def voice_handler(msg: Message):
    #chat_info = await bot.get_chat(msg.chat.id)
    #chat_info.
    #if bot.get_chat()
    await msg.delete()
    await msg.answer("_Voice message was deleted_")


@dp.message(F.text)
async def echo_handler(msg: Message):
    text = msg.text
    await msg.answer(text)


if __name__ == "__main__":
    asyncio.run(main())
