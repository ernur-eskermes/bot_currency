import telebot

URL_USD = 'https://banki24.by/minsk/kurs/usd'
URL_EUR = 'https://banki24.by/minsk/kurs/eur'
URL_RUB = 'https://banki24.by/minsk/kurs/rub'
TOKEN = '1381834710:AAHYbqw20OyLmr32fkNIoVYFUtATTHO-AHA'

BOT = telebot.TeleBot(TOKEN)

BUTTON_START = 'В начало'

BUTTON_USD = 'USD'
BUTTON_EUR = 'EUR'
BUTTON_RUB = 'RUB'

BUTTON_GET_ALL_LIST = 'Весь список банков'
BUTTON_BEST_BUY_VALUE = 'Лучший курс для покупки'
BUTTON_BEST_SELL_VALUE = 'Лучший курс для продажи'

def create_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    return keyboard

KEYBOARD_START = create_keyboard()
KEYBOARD_START.row(BUTTON_USD, BUTTON_EUR)
KEYBOARD_START.row(BUTTON_RUB)

KEYBOARD_CHOICE = create_keyboard()
KEYBOARD_CHOICE.row(BUTTON_GET_ALL_LIST)
KEYBOARD_CHOICE.row(BUTTON_BEST_BUY_VALUE, BUTTON_BEST_SELL_VALUE)
KEYBOARD_CHOICE.row(BUTTON_START)