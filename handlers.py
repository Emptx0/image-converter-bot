from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("<b>Welcome to Image Converter Bot!</b>\n"
                     "Send image or images you want to convert.")
