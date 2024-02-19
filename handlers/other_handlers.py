from aiogram import Router
from aiogram.types import Message

router = Router()


# This handler will respond to any messages from the user, outside the bot's logic
@router.message()
async def send_echo(message: Message):
    await message.answer(f'Это эхо! {message.text}')
