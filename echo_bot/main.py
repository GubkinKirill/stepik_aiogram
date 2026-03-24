from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = 'token'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer('Hello world')

@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши что нибудь, я пришлю твое сообщение'
    )

@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

if __name__ == '__main__':
    dp.run_polling(bot)
