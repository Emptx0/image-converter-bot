from aiogram import types, F, Router
from aiogram.client import bot
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ChatAction

import os
import shutil

from converter import convert_to_pdf, convert_to_jpg


router = Router()
img_ids = []


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("<b>Welcome to Image Converter Bot!</b>\n"
                     "Send images you want to convert.")


@router.message(F.photo)
async def img_handler(msg: Message):
    if not os.path.exists("temp"):
        os.makedirs("temp")

    # add ids to list and download images to temporary folder
    img_ids.append(msg.photo[-1].file_id)
    await msg.bot.download(file=msg.photo[-1].file_id, destination=f"temp/{msg.photo[-1].file_id}.png")

    await msg.answer("<b>Upload successful!</b>\n"
                     "Type /convert to convert images")


@router.message(Command("convert"))
async def select_to_conv_type(message: types.Message):
    if not img_ids:
        await message.answer("Please upload images first!")
        return

    kb = [
        [
            types.KeyboardButton(text="pdf"),
            types.KeyboardButton(text="jpg")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    await message.answer("Select result file type.", reply_markup=keyboard)

    @router.message(F.text.lower() == "pdf")
    async def to_pdf(msg: types.Message):
        await message.answer("Converting to PDF...", reply_markup=types.ReplyKeyboardRemove())

        # generate file in "file_path"
        file_path = convert_to_pdf(img_ids)

        # send document
        await msg.bot.send_chat_action(
            chat_id=msg.chat.id,
            action=ChatAction.UPLOAD_DOCUMENT
        )
        await message.answer_document(
            document=types.FSInputFile(
                path=file_path
            )
        )

        # clear temporary folder and list
        if os.path.exists("temp"):
            shutil.rmtree("temp")
        img_ids.clear()

    @router.message(F.text.lower() == "jpg")
    async def to_jpg(msg: types.Message):
        await message.answer("Converting to JPG...", reply_markup=types.ReplyKeyboardRemove())
        convert_to_jpg(img_ids)

        # send document
        await msg.bot.send_chat_action(
            chat_id=msg.chat.id,
            action=ChatAction.UPLOAD_DOCUMENT
        )
        for img_id in img_ids:
            await message.answer_document(
                document=types.FSInputFile(
                    path=f"temp/{img_id}.jpg"
                )
            )

        # clear temporary folder and list
        if os.path.exists("temp"):
            shutil.rmtree("temp")
        img_ids.clear()
