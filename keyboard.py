from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup


main = ReplyKeyboardMarkup (keyboard=[
    [KeyboardButton(text='генерировать число'),KeyboardButton(text='закончить работу')],
    [KeyboardButton(text="создать qr code"),KeyboardButton(text="перевести текст")]
],resize_keyboard=True)


resume = InlineKeyboardMarkup (inline_keyboard=[
    [InlineKeyboardButton(text="Автор",url="https://t.me/Kilaaaaaakod")]
])



