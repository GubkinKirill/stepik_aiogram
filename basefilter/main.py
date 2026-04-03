from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart, BaseFilter
from aiogram.types import Message

BOT_TOKEN = 'BOT_TOKEN'

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

admin_ids: list[int] = ['ID']

class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids

@dp.message(IsAdmin(admin_ids))
async def answer_if_admin_update(message: Message):
    await message.answer('Admin')

@dp.message()
async def answer_if_not_admin_update(message: Message):
    await message.answer('Not admin')



if __name__ == '__main__':
    dp.run_polling(bot)