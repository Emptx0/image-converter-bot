import asyncio
import logging
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Update,
                      InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (Application, CallbackQueryHandler, CommandHandler,
                          ContextTypes, ConversationHandler, MessageHandler, filters)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define states
IMAGE, INPUT, OUTPUT, CONVERTED = range(4)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [['png', 'jpg']]

    await update.message.reply_text(
        '<b>Welcome to the Image Converter Bot!\n'
        'Select input image type.\n',
        parse_mode='HTML',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True),
    )

    return INPUT

async def input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:


def main() -> None:
    application = Application.builder().token("7077457101:AAG87klb9mmM4tPHSecC8HW3pUelh2L3ThA").build()


if __name__ == '__main__':
    main()
