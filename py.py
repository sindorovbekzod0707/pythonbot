import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '5098872013:AAEuwJQ0jrxHUfiNaVEkdYgWGZLuRsJp1tQ'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   Keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton("📙1-sinf kitoblari📚"),
        KeyboardButton("📙2-sinf kitoblari📚"),
        KeyboardButton("📙3-sinf kitoblari📚"),
        KeyboardButton("📙4-sinf kitoblari📚"),
        KeyboardButton("📙5-sinf kitoblari📚"),
        KeyboardButton("📙6-sinf kitoblari📚"),
        KeyboardButton("📙7-sinf kitoblari📚"),
        KeyboardButton("📙8-sinf kitoblari📚"),
        KeyboardButton("📙9-sinf kitoblari📚"),
        KeyboardButton("📙10-sinf kitoblari📚"),
        KeyboardButton("📙11-sinf kitoblari📚"),
        KeyboardButton("📙Python kitoblar📚")
        )

   await message.reply("Salom!\nBu botda 1-sinfdan 11- sinfgacha maktab darsliklari bor!\nNechinchi sinf kitob kerak."
                        , reply_markup=Keyboard)

@dp.message_handler(text='📙1-sinf kitoblari📚')
async def test(msg: types.Message):
    link1 = 'https://t.me/Maktab_darsliklari_Bekzod/34'
    link2 = 'https://t.me/Maktab_darsliklari_Bekzod/35'
    link3 = 'https://t.me/Maktab_darsliklari_Bekzod/36'
    link4 = 'https://t.me/Maktab_darsliklari_Bekzod/37'
    link5 = 'https://t.me/Maktab_darsliklari_Bekzod/38'
    link6 = 'https://t.me/Maktab_darsliklari_Bekzod/39'
    link7 = 'https://t.me/Maktab_darsliklari_Bekzod/40'
    link8 = 'https://t.me/Maktab_darsliklari_Bekzod/41'
    link9 = 'https://t.me/Maktab_darsliklari_Bekzod/42'
    link10 = 'https://t.me/Maktab_darsliklari_Bekzod/43'
    await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

    
@dp.message_handler(text='📙2-sinf kitoblari📚')
async def test(msg: types.Message):
    link1= 'https://t.me/Maktab_darsliklari_Bekzod/46'
    link2 = 'https://t.me/Maktab_darsliklari_Bekzod/47'
    link3 = 'https://t.me/Maktab_darsliklari_Bekzod/48'
    link4 = 'https://t.me/Maktab_darsliklari_Bekzod/49'
    link5 = 'https://t.me/Maktab_darsliklari_Bekzod/50'
    link6 = 'https://t.me/Maktab_darsliklari_Bekzod/51'
    link7 = 'https://t.me/Maktab_darsliklari_Bekzod/52'
    link8 = 'https://t.me/Maktab_darsliklari_Bekzod/53'
    link9 = 'https://t.me/Maktab_darsliklari_Bekzod/54'
    link10 = 'https://t.me/Maktab_darsliklari_Bekzod/55'
    await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

@dp.message_handler(text='📙3-sinf kitoblari📚')
async def test(msg: types.Message):
    link1= 'https://t.me/Maktab_darsliklari_Bekzod/58'
    link2 = 'https://t.me/Maktab_darsliklari_Bekzod/59'
    link3 = 'https://t.me/Maktab_darsliklari_Bekzod/60'
    link4 = 'https://t.me/Maktab_darsliklari_Bekzod/61'
    link5 = 'https://t.me/Maktab_darsliklari_Bekzod/62'
    link6 = 'https://t.me/Maktab_darsliklari_Bekzod/63'
    link7 = 'https://t.me/Maktab_darsliklari_Bekzod/64'
    link8 = 'https://t.me/Maktab_darsliklari_Bekzod/65'
    link9 = 'https://t.me/Maktab_darsliklari_Bekzod/66'
    link10 = 'https://t.me/Maktab_darsliklari_Bekzod/67'
    await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

@dp.message_handler(text='📙4-sinf kitoblari📚')
async def test(msg: types.Message):
    link1= 'https://t.me/Maktab_darsliklari_Bekzod/70'
    link2 = 'https://t.me/Maktab_darsliklari_Bekzod/71'
    link3 = 'https://t.me/Maktab_darsliklari_Bekzod/72'
    link4 = 'https://t.me/Maktab_darsliklari_Bekzod/73'
    link5 = 'https://t.me/Maktab_darsliklari_Bekzod/74'
    link6 = 'https://t.me/Maktab_darsliklari_Bekzod/75'
    link7 = 'https://t.me/Maktab_darsliklari_Bekzod/76'
    link8 = 'https://t.me/Maktab_darsliklari_Bekzod/77'
    link9 = 'https://t.me/Maktab_darsliklari_Bekzod/78'
    link10 = 'https://t.me/Maktab_darsliklari_Bekzod/79'
    await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

@dp.message_handler(text='📙5-sinf kitoblari📚')
async def test(msg: types.Message):
    link1= 'https://t.me/Maktab_darsliklari_Bekzod/82'
    link2 = 'https://t.me/Maktab_darsliklari_Bekzod/83'
    link3 = 'https://t.me/Maktab_darsliklari_Bekzod/84'
    link4 = 'https://t.me/Maktab_darsliklari_Bekzod/85'
    link5 = 'https://t.me/Maktab_darsliklari_Bekzod/86'
    link6 = 'https://t.me/Maktab_darsliklari_Bekzod/87'
    link7 = 'https://t.me/Maktab_darsliklari_Bekzod/88'
    link8 = 'https://t.me/Maktab_darsliklari_Bekzod/89'
    link9 = 'https://t.me/Maktab_darsliklari_Bekzod/90'
    link10 = 'https://t.me/Maktab_darsliklari_Bekzod/91'
    await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

@dp.message_handler(text='📙6-sinf kitoblari📚')
async def test(msg: types.Message):
    link1= 'https://t.me/Maktab_darsliklari_Bekzod/94'
    link2 = 'https://t.me/Maktab_darsliklari_Bekzod/95'
    link3 = 'https://t.me/Maktab_darsliklari_Bekzod/96'
    link4 = 'https://t.me/Maktab_darsliklari_Bekzod/97'
    link5 = 'https://t.me/Maktab_darsliklari_Bekzod/98'
    link6 = 'https://t.me/Maktab_darsliklari_Bekzod/99'
    link7 = 'https://t.me/Maktab_darsliklari_Bekzod/100'
    link8 = 'https://t.me/Maktab_darsliklari_Bekzod/101'
    link9 = 'https://t.me/Maktab_darsliklari_Bekzod/102'
    link10 = 'https://t.me/Maktab_darsliklari_Bekzod/103'
    await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

@dp.message_handler(text='📙7-sinf kitoblari📚')
async def test(msg: types.Message):
    link1= 'https://t.me/Maktab_darsliklari_Bekzod/106'
    link2 = 'https://t.me/Maktab_darsliklari_Bekzod/107'
    link3 = 'https://t.me/Maktab_darsliklari_Bekzod/108'
    link4 = 'https://t.me/Maktab_darsliklari_Bekzod/109'
    link5 = 'https://t.me/Maktab_darsliklari_Bekzod/110'
    link6 = 'https://t.me/Maktab_darsliklari_Bekzod/111'
    link7 = 'https://t.me/Maktab_darsliklari_Bekzod/112'
    link8 = 'https://t.me/Maktab_darsliklari_Bekzod/113'
    link9 = 'https://t.me/Maktab_darsliklari_Bekzod/114'
    link10 = 'https://t.me/Maktab_darsliklari_Bekzod/115'
    await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

@dp.message_handler(text='📙8-sinf kitoblari📚')
async def test(msg: types.Message):
    link1= 'https://t.me/Maktab_darsliklari_Bekzod/118'
    link2 = 'https://t.me/Maktab_darsliklari_Bekzod/119'
    link3 = 'https://t.me/Maktab_darsliklari_Bekzod/120'
    link4 = 'https://t.me/Maktab_darsliklari_Bekzod/121'
    link5 = 'https://t.me/Maktab_darsliklari_Bekzod/122'
    link6 = 'https://t.me/Maktab_darsliklari_Bekzod/123'
    link7 = 'https://t.me/Maktab_darsliklari_Bekzod/124'
    link8 = 'https://t.me/Maktab_darsliklari_Bekzod/125'
    link9 = 'https://t.me/Maktab_darsliklari_Bekzod/126'
    link10 = 'https://t.me/Maktab_darsliklari_Bekzod/127'
    await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

@dp.message_handler(text='📙9-sinf kitoblari📚')
async def test(msg: types.Message):
    link1= 'https://t.me/Maktab_darsliklari_Bekzod/130'
    link2 = 'https://t.me/Maktab_darsliklari_Bekzod/131'
    link3 = 'https://t.me/Maktab_darsliklari_Bekzod/132'
    link4 = 'https://t.me/Maktab_darsliklari_Bekzod/133'
    link5 = 'https://t.me/Maktab_darsliklari_Bekzod/134'
    link6 = 'https://t.me/Maktab_darsliklari_Bekzod/135'
    link7 = 'https://t.me/Maktab_darsliklari_Bekzod/136'
    link8 = 'https://t.me/Maktab_darsliklari_Bekzod/137'
    link9 = 'https://t.me/Maktab_darsliklari_Bekzod/138'
    link10 = 'https://t.me/Maktab_darsliklari_Bekzod/139'
    await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

@dp.message_handler(text='📙10-sinf kitoblari📚')
async def test(msg: types.Message):
    link1= 'https://t.me/Maktab_darsliklari_Bekzod/142'
    link2 = 'https://t.me/Maktab_darsliklari_Bekzod/119'
    link3 = 'https://t.me/Maktab_darsliklari_Bekzod/120'
    link4 = 'https://t.me/Maktab_darsliklari_Bekzod/121'
    link5 = 'https://t.me/Maktab_darsliklari_Bekzod/122'
    link6 = 'https://t.me/Maktab_darsliklari_Bekzod/123'
    link7 = 'https://t.me/Maktab_darsliklari_Bekzod/124'
    link8 = 'https://t.me/Maktab_darsliklari_Bekzod/125'
    link9 = 'https://t.me/Maktab_darsliklari_Bekzod/126'
    link10 = 'https://t.me/Maktab_darsliklari_Bekzod/127'
    await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

@dp.message_handler(text='📙11-sinf kitoblari📚')
async def test(msg: types.Message):
    link1= 'https://t.me/Maktab_darsliklari_Bekzod/154'
    link2 = 'https://t.me/Maktab_darsliklari_Bekzod/155'
    link3 = 'https://t.me/Maktab_darsliklari_Bekzod/156'
    link4 = 'https://t.me/Maktab_darsliklari_Bekzod/157'
    link5 = 'https://t.me/Maktab_darsliklari_Bekzod/158'
    link6 = 'https://t.me/Maktab_darsliklari_Bekzod/159'
    link7 = 'https://t.me/Maktab_darsliklari_Bekzod/160'
    link8 = 'https://t.me/Maktab_darsliklari_Bekzod/161'
    link9 = 'https://t.me/Maktab_darsliklari_Bekzod/162'
    link10 = 'https://t.me/Maktab_darsliklari_Bekzod/163'
    await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

@dp.message_handler(text='📙Python kitoblar📚')
async def test(msg: types.Message):
    link1 = 'https://t.me/Maktab_darsliklari_Bekzod/165'
    link2 = 'https://t.me/Maktab_darsliklari_Bekzod/166'
    link3 = 'https://t.me/Maktab_darsliklari_Bekzod/168?single'
    link4 = 'https://t.me/Maktab_darsliklari_Bekzod/169'
    link5 = 'https://t.me/Maktab_darsliklari_Bekzod/176'
    await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
    await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


executor.start_polling(dp, skip_updates=True)
