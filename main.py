import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
import collections
from datetime import datetime

TOKEN = "YOUR_BOT_TOKEN_HERE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

db = []

class UserHabits:
    __user_id: str
    _habits: list[Habit]

    def get_user(self) -> str:
        return self.__user_id
    
    def set_user(self, user_id: str):
        self.__user_id = user_id
    
    def get_habits(self) -> list[Habit]:
        return _habits

class Habit:
    _start_date: datetime.date
    _text: str

    def __str__(self):
        return _text

@dp.message(CommandStart())
async def cmd_start(message: Message):
    builder = InlineKeyboardBuilder()
    
    builder.button(text="Добавить привычку", callback_data="btn_add")
    
    builder.adjust(1)

    await message.answer(f"Здоров! Буду отслеживать твои новые привычки", reply_keyboard=builde.as_markup())


async def send_periodic_message(user_id: str):
    msg = ""
    for i in range(len(db)):
        if db[i].get_user() == user_id:
            msg += "\n".join([str(i) for i in db[i].get_habits()])
            break

    await bot.send_message(chat_id=CHAT_ID, text=msg)

@dp.message()
async def echo_handler(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice message!")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
