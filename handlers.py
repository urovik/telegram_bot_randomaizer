from aiogram import F, Router
from aiogram.filters import CommandStart,Command,StateFilter
from aiogram.types import Message,ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from app.randoms import create_num
from app.keyboard import main,resume
from app.qrcode import make_qrcode
from app.translator import translates_text


router = Router()

class Number(StatesGroup):
    low_num = State()
    hign_num = State()

class QR:
    qr_code_link = StateFilter("qr_code_link")

class Text(StatesGroup):
    text = State()


@router.message(CommandStart())
async def start(message:Message):
    await message.answer("Привет,это бот рандомайзер",reply_markup=main)

@router.message(Command('help'))
async def start(message:Message):
    await message.answer(text="об авторе",reply_markup=resume)


@router.message(F.text == "генерировать число")
async def start_randomaizer(message:Message,state:FSMContext):
    await state.set_state(Number.low_num)
    await message.answer('Введите нижний предел')

# создание qr code
@router.message(F.text == "создать qr code")
async def start_create_qr(message: Message, state: FSMContext):
    await state.set_state(QR.qr_code_link)
    await message.answer('Введите ссылку, из которой хотите сделать QR-код')

@router.message(QR.qr_code_link)
async def qr_create(message: Message, state: FSMContext):
    await state.update_data(qr_code_link=message.text)
    data = await state.get_data()
    qr_code_file_path = await make_qrcode(data['qr_code_link'])  # Получаем путь к изображению
    await message.answer_photo(open(qr_code_file_path), caption="Вот ваш QR-код")  # Открываем файл для отправки
    await state.clear()



@router.message(Number.low_num)
async def req_one(message:Message,state:FSMContext):
    await state.update_data(low_num = message.text)
    await state.set_state(Number.hign_num)
    await message.answer('Введите верхний предел')


@router.message(Number.hign_num)
async def req_two(message:Message,state:FSMContext):
    try:
       await state.update_data(hign_num = message.text)
       data = await state.get_data()
       randoms = await create_num(int(data["low_num"]),int(data["hign_num"]))
       await message.reply(f"Ваше число {randoms}") 
       await state.clear()
    except ValueError:
        await message.answer('что то пошло не так')
        await state.clear()

    

@router.message(F.text == "закончить работу")
async def start_randomaizer(message:Message,state:FSMContext):
    await state.clear()
    await message.reply("работа завершена,для продолжения напишите команду /start",reply_markup = ReplyKeyboardRemove())
    
   
@router.message(F.text == "перевести текст")
async def start_translate(message:Message,state:FSMContext):
    await state.set_state(Text.text)
    await message.answer('Введите текст который хотите перевести')


@router.message(Text.text)
async def translate_text(message:Message,state:FSMContext):
    await state.update_data(text = message.text)
    data = await state.get_data()
    transalate_texts = await translates_text(data["text"])
    await message.reply(f"{transalate_texts}")



   
    