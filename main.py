import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import URLInputFile

from bot_auth import token_id  # you should create bot_auth.py file and enter your api there
import rand_img

TOKEN = token_id
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode='HTML')

logger = logging.getLogger(__name__)


@dp.message(Command(commands=['start']))
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Привет, <b>{message.from_user.full_name}! </b>')


@dp.message(Command(commands=['surprize']))
async def surprize(message: Message) -> None:
    image = URLInputFile(
        rand_img.random_image(),
        filename='random_gift.png'
    )
    await bot.send_photo(message.chat.id, image)


def main() -> None:
    dp.run_polling(bot)


if __name__ == '__main__':
    main()
