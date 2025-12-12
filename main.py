# # === CONFIG ===
# BOT_TOKEN = "8436960327:AAHgOyx9T6oqKrNAe40SKEZKZnUW_4qsOCQ"
# ADMIN_PHONE = "991081100"

# # ==========================
# #       IMPORTS
# # ==========================
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from aiogram.types import Message
# from aiogram import F
# from aiogram.fsm.context import FSMContext

# from states import AdminStates, UserStates
# from keyboards import admin_menu_kb, cancel_kb, start_role_kb
# from database import Database

# db = Database("data.db")

# bot = Bot(BOT_TOKEN)
# dp = Dispatcher()

# # ==========================
# #         START
# # ==========================
# @dp.message(Command("start"))
# async def start_cmd(message: Message):
#     await message.answer(
#         "Assalomu alaykum!\nTest tekshirish botiga xush kelibsiz!"
#     )
#     await message.answer(
#         "Rolni tanlang:",
#         reply_markup=start_role_kb()
#     )

# # ==========================
# #     ROLE SELECTION
# # ==========================
# @dp.message(F.text == "Admin")
# async def choose_admin(message: Message, state: FSMContext):
#     await message.answer("Admin telefon raqamini kiriting:", reply_markup=cancel_kb())
#     await state.set_state(AdminStates.enter_phone)

# @dp.message(F.text == "Foydalanuvchi")
# async def choose_user(message: Message, state: FSMContext):
#     await message.answer("Test kodini kiriting:", reply_markup=cancel_kb())
#     await state.set_state(UserStates.enter_test_code)

# # ==========================
# #        ADMIN LOGIN
# # ==========================
# @dp.message(AdminStates.enter_phone)
# async def admin_phone(message: Message, state: FSMContext):
#     if message.text.strip() == ADMIN_PHONE:
#         await message.answer("Raqam tasdiqlandi!\nEndi test kodini kiriting:")
#         await state.set_state(AdminStates.enter_test_code)
#     else:
#         await message.answer("Xato! Bu admin raqami emas!")

# @dp.message(AdminStates.enter_test_code)
# async def admin_test_code(message: Message, state: FSMContext):
#     test_code = message.text.strip().upper()
#     await state.update_data(test_code=test_code)
#     await message.answer("Endi shu test uchun javoblarni kiriting (masalan: ABDBACCBBADC):")
#     await state.set_state(AdminStates.enter_answers)

# @dp.message(AdminStates.enter_answers)
# async def admin_answers(message: Message, state: FSMContext):
#     answers = message.text.strip().upper()
#     data = await state.get_data()
#     test_code = data["test_code"]

#     db.save_test(test_code, answers)

#     await message.answer("Test muvaffaqiyatli saqlandi!", reply_markup=admin_menu_kb())
#     await state.clear()
#     # Rol tanlash menyusiga qaytarish
#     await message.answer(
#         "Rolni tanlang:",
#         reply_markup=start_role_kb()
#     )

# # ==========================
# #       USER TEST
# # ==========================
# @dp.message(UserStates.enter_test_code)
# async def user_enter_test_code(message: Message, state: FSMContext):
#     code = message.text.strip().upper()
#     correct = db.get_answers(code)

#     if correct is None:
#         await message.answer("Bunday test topilmadi!")
#         return

#     await state.update_data(test_code=code)
#     await message.answer("Test javoblaringizni yuboring:\nMasalan: ABBACDBA...")
#     await state.set_state(UserStates.enter_answers)

# @dp.message(UserStates.enter_answers)
# async def user_check(message: Message, state: FSMContext):
#     user_ans = message.text.strip().upper()
#     data = await state.get_data()
#     correct = db.get_answers(data["test_code"])

#     total = len(correct)
#     score = sum(1 for a, b in zip(user_ans, correct) if a == b)
#     percent = round(score / total * 100, 1)

#     await message.answer(
#         f"📊 *Natija:*\n"
#         f"To‘g‘ri javoblar: {score} / {total}\n"
#         f"Foiz: {percent}%",
#         parse_mode="Markdown"
#     )
#     await state.clear()
#     # Rol tanlash menyusiga qaytarish
#     await message.answer(
#         "Rolni tanlang:",
#         reply_markup=start_role_kb()
#     )

# # ==========================
# #         CANCEL
# # ==========================
# @dp.message(F.text == "❌ Bekor qilish")
# async def cancel(message: Message, state: FSMContext):
#     await message.answer("Bekor qilindi.", reply_markup=types.ReplyKeyboardRemove())
#     await state.clear()
#     # Rol tanlash menyusiga qaytarish
#     await message.answer(
#         "Rolni tanlang:",
#         reply_markup=start_role_kb()
#     )

# # ==========================
# #         RUN BOT
# # ==========================
# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(dp.start_polling(bot))

# === main.py ===

# # === CONFIG ===
# BOT_TOKEN = "8436960327:AAHgOyx9T6oqKrNAe40SKEZKZnUW_4qsOCQ"
# ADMIN_PHONE = "991081100"

# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from aiogram.types import Message
# from aiogram import F
# from aiogram.fsm.context import FSMContext

# from states import AdminStates, UserStates
# from keyboards import admin_menu_kb, cancel_kb, start_role_kb
# from database import Database

# db = Database("data.db")

# bot = Bot(BOT_TOKEN)
# dp = Dispatcher()

# # ==========================
# #         START
# # ==========================
# @dp.message(Command("start"))
# async def start_cmd(message: Message):
#     await message.answer(
#         "Assalomu alaykum!\nTest tekshirish botiga xush kelibsiz!"
#     )
#     await message.answer(
#         "Rolni tanlang:",
#         reply_markup=start_role_kb()
#     )

# # ==========================
# #     ROLE SELECTION
# # ==========================
# @dp.message(F.text == "Admin")
# async def choose_admin(message: Message, state: FSMContext):
#     await message.answer("Admin telefon raqamini kiriting:", reply_markup=cancel_kb())
#     await state.set_state(AdminStates.enter_phone)

# @dp.message(F.text == "Foydalanuvchi")
# async def choose_user(message: Message, state: FSMContext):
#     await message.answer("Test kodini kiriting:", reply_markup=cancel_kb())
#     await state.set_state(UserStates.enter_test_code)

# # ==========================
# #       ADMIN LOGIN
# # ==========================
# @dp.message(AdminStates.enter_phone)
# async def admin_phone(message: Message, state: FSMContext):
#     if message.text.strip() == ADMIN_PHONE:
#         await message.answer("Raqam tasdiqlandi!\nEndi test kodini kiriting:")
#         await state.set_state(AdminStates.enter_test_code)
#     else:
#         await message.answer("Xato! Bu admin raqami emas!")

# @dp.message(AdminStates.enter_test_code)
# async def admin_test_code(message: Message, state: FSMContext):
#     test_code = message.text.strip().upper()
#     await state.update_data(test_code=test_code)
#     await message.answer("Endi shu test uchun javoblarni kiriting (masalan: ABDBACCBBADC):")
#     await state.set_state(AdminStates.enter_answers)

# @dp.message(AdminStates.enter_answers)
# async def admin_answers(message: Message, state: FSMContext):
#     answers = message.text.strip().upper()
#     data = await state.get_data()
#     test_code = data["test_code"]

#     db.save_test(test_code, answers)

#     await message.answer("Test muvaffaqiyatli saqlandi!", reply_markup=admin_menu_kb())
#     await state.clear()
#     await message.answer("Rolni tanlang:", reply_markup=start_role_kb())

# # ==========================
# #     USER TEST PROCESS
# # ==========================
# @dp.message(UserStates.enter_test_code)
# async def user_enter_test_code(message: Message, state: FSMContext):
#     code = message.text.strip().upper()
#     correct = db.get_answers(code)

#     if correct is None:
#         await message.answer("Bunday test topilmadi!")
#         return

#     await state.update_data(test_code=code)
#     await message.answer("Test javoblaringizni yuboring:\nMasalan: ABBACDBA...")
#     await state.set_state(UserStates.enter_answers)

# @dp.message(UserStates.enter_answers)
# async def user_check(message: Message, state: FSMContext):
#     user_ans = message.text.strip().upper()
#     data = await state.get_data()
#     correct = db.get_answers(data["test_code"])

#     total = len(correct)
#     score = sum(1 for a, b in zip(user_ans, correct) if a == b)
#     percent = round(score / total * 100, 1)

#     await message.answer(
#         f"📊 *Natija:*\nTo‘g‘ri javoblar: {score} / {total}\nFoiz: {percent}%",
#         parse_mode="Markdown"
#     )

#     text = (
#         f"🧑‍🎓 *Yangi natija!*\n"
#         f"Test kodi: {data['test_code']}\n"
#         f"Foydalanuvchi javobi: {user_ans}\n"
#         f"Natija: {score}/{total} ({percent}%)"
#     )
#     await bot.send_message(ADMIN_PHONE, text, parse_mode="Markdown")

#     await state.clear()
#     await message.answer("Rolni tanlang:", reply_markup=start_role_kb())

# # ==========================
# #         CANCEL
# # ==========================
# @dp.message(F.text == "❌ Bekor qilish")
# async def cancel(message: Message, state: FSMContext):
#     await message.answer("Bekor qilindi.", reply_markup=types.ReplyKeyboardRemove())
#     await state.clear()
#     await message.answer("Rolni tanlang:", reply_markup=start_role_kb())

# # ==========================
# #         RUN BOT
# # ==========================
# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(dp.start_polling(bot))







# === main.py ===

# === CONFIG ===
BOT_TOKEN = "8436960327:AAHgOyx9T6oqKrNAe40SKEZKZnUW_4qsOCQ"
ADMIN_CHAT_ID = 841086112  # Adminning Telegram chat ID si

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
from aiogram.fsm.context import FSMContext

from states import AdminStates, UserStates
from keyboards import admin_menu_kb, cancel_kb, start_role_kb
from database import Database

db = Database("data.db")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# ==========================
#         START
# ==========================
@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        "Assalomu alaykum!\nTest tekshirish botiga xush kelibsiz!"
    )
    await message.answer(
        "Rolni tanlang:",
        reply_markup=start_role_kb()
    )

# ==========================
#     ROLE SELECTION
# ==========================
@dp.message(F.text == "Admin")
async def choose_admin(message: Message, state: FSMContext):
    # Faqat admin chat ID tekshiruvi
    if message.from_user.id != ADMIN_CHAT_ID:
        await message.answer("❌ Siz admin emassiz!")
        return

    await message.answer("Admin rejimiga kirish tasdiqlandi!\nEndi test kodini kiriting.", reply_markup=cancel_kb())
    await state.set_state(AdminStates.enter_test_code)

@dp.message(F.text == "Foydalanuvchi")
async def choose_user(message: Message, state: FSMContext):
    await message.answer("Test kodini kiriting:", reply_markup=cancel_kb())
    await state.set_state(UserStates.enter_test_code)

# ==========================
#       ADMIN PROCESS
# ==========================
@dp.message(AdminStates.enter_test_code)
async def admin_test_code(message: Message, state: FSMContext):
    test_code = message.text.strip().upper()
    await state.update_data(test_code=test_code)
    await message.answer("Endi shu test uchun javoblarni kiriting (masalan: ABDBACCBBADC):")
    await state.set_state(AdminStates.enter_answers)

@dp.message(AdminStates.enter_answers)
async def admin_answers(message: Message, state: FSMContext):
    answers = message.text.strip().upper()
    data = await state.get_data()
    test_code = data["test_code"]

    db.save_test(test_code, answers)

    await message.answer("Test muvaffaqiyatli saqlandi!", reply_markup=admin_menu_kb())
    await state.clear()
    await message.answer("Rolni tanlang:", reply_markup=start_role_kb())

# ==========================
#     USER TEST PROCESS
# ==========================
@dp.message(UserStates.enter_test_code)
async def user_enter_test_code(message: Message, state: FSMContext):
    code = message.text.strip().upper()
    correct = db.get_answers(code)

    if correct is None:
        await message.answer("Bunday test topilmadi!")
        return

    await state.update_data(test_code=code)
    await message.answer("Test javoblaringizni yuboring:\nMasalan: ABBACDBA...")
    await state.set_state(UserStates.enter_answers)

@dp.message(UserStates.enter_answers)
async def user_check(message: Message, state: FSMContext):
    user_ans = message.text.strip().upper()
    data = await state.get_data()
    correct = db.get_answers(data["test_code"])

    total = len(correct)
    score = sum(1 for a, b in zip(user_ans, correct) if a == b)
    percent = round(score / total * 100, 1)

    await message.answer(
        f"📊 *Natija:*\nTo‘g‘ri javoblar: {score} / {total}\nFoiz: {percent}%",
        parse_mode="Markdown"
    )

    # Adminga yuborish (username yoki fullname bilan)
    username = message.from_user.username or message.from_user.full_name
    text = (
        f"🧑‍🎓 *Yangi natija!*\n"
        f"Foydalanuvchi: @{username}\n"
        f"Test kodi: {data['test_code']}\n"
        f"Foydalanuvchi javobi: {user_ans}\n"
        f"Natija: {score}/{total} ({percent}%)"
    )
    await bot.send_message(ADMIN_CHAT_ID, text, parse_mode="Markdown")

    await state.clear()
    await message.answer("Rolni tanlang:", reply_markup=start_role_kb())

# ==========================
#         CANCEL
# ==========================
@dp.message(F.text == "❌ Bekor qilish")
async def cancel(message: Message, state: FSMContext):
    await message.answer("Bekor qilindi.", reply_markup=types.ReplyKeyboardRemove())
    await state.clear()
    await message.answer("Rolni tanlang:", reply_markup=start_role_kb())

# ==========================
#         RUN BOT
# ==========================
if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
