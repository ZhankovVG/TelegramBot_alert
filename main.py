from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "6051091753:AAElPDTxvI55ASpSjfzGrMk2zpMATwzQl4g"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def eche(message: types.Message):
    await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp)