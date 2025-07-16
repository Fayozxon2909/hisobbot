from aiogram import Router
from aiogram.types import Message
from aiogram.types import ChatMemberUpdated

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
@router.chat_member()
async def user_left_or_kicked(event: ChatMemberUpdated):
    old_status = event.old_chat_member.status
    new_status = event.new_chat_member.status

    if old_status in ("member", "administrator") and new_status == "left":
        user = event.old_chat_member.user.full_name
        by_who = event.from_user.full_name

        if event.from_user.id == event.old_chat_member.user.id:
            await event.answer(f"❌ {user} guruhdan o‘zi chiqib ketdi.")
        else:
            await event.answer(f"❌ {by_who} {user} ni guruhdan chiqazdi.")
