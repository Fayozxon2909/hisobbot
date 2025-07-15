from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "/help")
async def help_command(message: Message):
    await message.answer(
        "🆘 Bot buyruqlari:\n\n"
        "/start – Botni ishga tushurish\n"
        "/help – Yordam va qo‘llanma\n\n"
        "Guruhga odam qo‘shganlarni avtomatik aniqlash uchun botga admin huquqi bering!"
    )
