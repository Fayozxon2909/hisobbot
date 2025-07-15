from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def handle_new_members(message: Message):
    if message.new_chat_members:
        for new_member in message.new_chat_members:
            await message.answer(
                f"✅ Muhammad Amin guruhga {new_member.full_name} ni qo‘shdi."
            )

    if message.left_chat_member:
        await message.answer(
            f"❌ <{message.left_chat_member.full_name} guruhdan chiqib ketdi."
        )
