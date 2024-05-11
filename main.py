import asyncio
import ctypes
import os
import logging
from io import BytesIO
import io
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
from aiogram.exceptions import TelegramBadRequest
from aiogram.methods import GetFile
from ctypes import *
import whisper
import numpy as np
from pathlib import Path
from pydub import AudioSegment
import os, sys

load_dotenv()
dp = Dispatcher()


async def main():
    bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"), parse_mode=ParseMode.MARKDOWN)

    model = whisper.load_model('base')
    await dp.start_polling(
        bot,
        model=model
    )


@dp.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        f"Hello, {html.bold(html.quote(msg.from_user.full_name))}",
        parse_mode=ParseMode.HTML
    )


@dp.message(F.voice)
async def voice_handler(msg: Message, model):
    bot = msg.bot
    downloaded = f"C:/Users/darmren/Downloads/Voices/{msg.voice.file_id}.wav"
    await bot.download(msg.voice, destination=downloaded)
    try:
        result = model.transcribe(downloaded)
        await msg.delete()
        # await msg.answer("_Voice message was deleted_")
        await msg.answer(result["text"])
    except TelegramBadRequest:
        await msg.answer('_Not enough rights to delete message_')


@dp.message(F.text)
async def echo_handler(msg: Message):
    text = msg.text
    await msg.answer(text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
