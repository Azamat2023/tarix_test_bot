# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# def cancel_kb():
#     return ReplyKeyboardMarkup(
#         keyboard=[[KeyboardButton(text="❌ Bekor qilish")]],
#         resize_keyboard=True
#     )

# def admin_menu_kb():
#     return ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="Yana test qo‘shish")],
#             [KeyboardButton(text="❌ Bekor qilish")]
#         ],
#         resize_keyboard=True
#     )

# def start_role_kb():
#     """ /start bosilganda rol tanlash tugmalari """
#     return ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="Admin")],
#             [KeyboardButton(text="Foydalanuvchi")]
#         ],
#         resize_keyboard=True
#     )


# === keyboards.py ===

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def cancel_kb():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="❌ Bekor qilish")]],
        resize_keyboard=True
    )

def admin_menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Yana test qo‘shish")],
            [KeyboardButton(text="❌ Bekor qilish")]
        ],
        resize_keyboard=True
    )

def start_role_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Admin")],
            [KeyboardButton(text="Foydalanuvchi")]
        ],
        resize_keyboard=True
    )
