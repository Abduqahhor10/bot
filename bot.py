from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "7866544180:AAHuupbBqrspYxCXtrZuk47D8zdLxZZ-YH8"
CHANNEL_ID = -1002306035491

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    waiting_for_number = State()

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Salom! Iltimos, biror son kiriting.")
    await UserState.waiting_for_number.set()

@dp.message_handler(state=UserState.waiting_for_number)
async def send_number_to_channel(message: types.Message, state: FSMContext):
    if message.text.isdigit():  
        user_number = message.text
        await bot.send_message(CHANNEL_ID, f"#{user_number}") 
        await message.answer(f"#{user_number} kanalda e'lon qilindi ✅")
        await state.finish()  
    else:
        await message.answer("Iltimos, faqat son kiriting!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
