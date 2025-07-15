from aiogram import Router, F
from aiogram.types import Message
from keyboards.inline import start_buttons

router = Router()

@router.message(F.text == "/start")
async def start_command(message: Message):
    user = message.from_user.first_name
    await message.answer(
        f"""🤖 Botga xush kelibsiz, {user}

📊Men Guruhga kim qancha odam qo'shganligini aytib beruvchi botman. 

Bot orqali Guruhingizga istagancha odam yigʻib olasiz vedio qoʻllanmada koʻrsatilgan Botni ishlatish. 

/help  -  buyrug'i orqali bot buyruqlari haqida ma'lumot olishingiz mumkin☑️

⚠️ Bot to'g'ri ishlashi uchun ADMIN huquqini berishingiz kerak""",
        reply_markup=start_buttons
    )
