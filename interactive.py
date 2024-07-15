"""types."""
from telebot import TeleBot, types

import functions as func
from permissions import check_tokens

check_tokens()

bot = TeleBot(token='TOKEN')


# FIXME: failure
@bot.message_handler(commands=['start'])
def wake_up(message):
    """Start menu."""
    chat = message.chat
    name = message.chat.first_name
    # Создаём объект клавиатуры:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(  # Первая строка кнопок.
        types.KeyboardButton('Который час?'),  # Первую кнопку в строке.
        types.KeyboardButton('Определи мой ip'),
    )
    keyboard.row(  # Вторая строка кнопок.
        types.KeyboardButton('/random_digit'),  # Создаём кнопку в строке.
        types.KeyboardButton('/newcat'),
    )

    bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}. Посмотри, какого котика я тебе нашёл',
        # Отправляем клавиатуру в сообщении бота: передаём объект клавиатуры
        # в параметр reply_markup объекта send_message.
        # Telegram-клиент "запомнит" клавиатуру и будет отображать её
        # в интерфейсе бота.
        reply_markup=keyboard,
    )

    bot.send_photo(chat.id, func.get_pic())
