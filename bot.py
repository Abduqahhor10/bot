from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

TOKEN = "7866544180:AAHuupbBqrspYxCXtrZuk47D8zdLxZZ-YH8"

CHANNELS = [
    "@hgfddddfs",
    "@bf34dqdfdfsrr",
    "@kanalnoooo1",
    "@awsdfghnfx"
]

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def is_user_subscribed(user_id):
    not_subscribed = []  
    for channel in CHANNELS:
        try:
            member = await bot.get_chat_member(channel, user_id)
            if member.status not in ["member", "administrator", "creator"]:
                not_subscribed.append(channel)
        except Exception as e:
            print(f"{channel} kanalida xatolik: {e}")
            not_subscribed.append(channel)
    return not_subscribed 
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    user_id = message.from_user.id
    not_subscribed_channels = await is_user_subscribed(user_id)

    if not_subscribed_channels:
        keyboard = InlineKeyboardMarkup()
        for channel in not_subscribed_channels:
            keyboard.add(InlineKeyboardButton(f"🔗 {channel} ga obuna bo‘lish", url=f"https://t.me/{channel[1:]}"))
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=keyboard)
    else:
        await message.answer("Siz barcha kanallarga obuna bo‘lgansiz! Xush kelibsiz! 🎉")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
