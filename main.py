import asyncio
import logging
import sys
import config
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart , Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold


# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}! Я бот который поможет тебе познакомиться с новыми людьми с твоего учебного заведения. "
                         f"Тут ты сможешь найти друзей и единомышленников. Скорей делай регистрирацию и найди себе друзей и единомышлеников ", reply_markup=config.keyboard.btn_client)

@dp.message(Command("help"))
async def help_message(message: types.Message):
    await message.answer(text="С чем вам помочь ?")



async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())