"""functions."""
import requests
import logging
import datetime as dt
import os

from dotenv import load_dotenv
from telebot import TeleBot, types

import constants as cons
import endpoints as endp
import messages as msg
import meteo_full as mt
import permissions as perm

load_dotenv()

bot_v1 = TeleBot(token=perm.TELEGRAM_BOT_TOKEN)

now = dt.datetime.now()
current_hour = now.time().hour
contact_info = 'rmv.msk@mail.ru'


# TODO: bot writing to selected user
def direct_initialization(CHAT_ID: str):
    """pass."""
    chat_id = os.getenv(CHAT_ID)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(
        types.KeyboardButton('/start'),
    )
    bot_v1.send_message(
        chat_id=chat_id,
        text=(
            'Проверь, работает ли погода на сейчас, '
            'завтра и на 5 дней. '
            'походи по меню в погоду и обратно '
            'по командам снизу. '
            'Отпишись по итогу Максу.'
        ),
        reply_markup=keyboard,
    )


def main_menu(message):
    """pass."""
    chat = message.chat
    # Создаём объект клавиатуры:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(  # Первая строка кнопок.
        # Первую кнопку в строке.
        types.KeyboardButton('Что ты умеешь?'),
        types.KeyboardButton('Покажи параметры'),
    )
    keyboard.row(  # Вторая строка кнопок.
        types.KeyboardButton('Пришли собачку'),
        types.KeyboardButton('Пришли котика'),
    )
    keyboard.row(  # Третья строка кнопок.
        types.KeyboardButton('/weather'),
    )
    bot_v1.send_message(
        chat_id=chat.id,
        text='Выбери, что ты хочешь узнать',
        reply_markup=keyboard,  # Отправляем клавиатуру в сообщении бота.
    )


def weather_menu(message):
    """pass."""
    chat = message.chat
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(
        types.KeyboardButton('Сейчас'),
        types.KeyboardButton('Завтра'),
    )
    keyboard.row(
        types.KeyboardButton('На 5 дней'),
    )
    keyboard.row(
        types.KeyboardButton(
            '/menu'
        )
    )
    bot_v1.send_message(
        chat_id=chat.id,
        text=('Погода на какое время интересует?'),
        reply_markup=keyboard,
    )


# TODO: location in meteo requests (? optional)
# 5 days meteo data (priority)
def react(message):
    """pass."""
    chat = message.chat
    if message.text == 'Пришли котика':
        bot_v1.send_photo(chat.id, get_cat())
    elif message.text == 'Пришли собачку':
        bot_v1.send_photo(chat.id, get_dog())
    elif message.text == 'Что ты умеешь?':
        bot_v1.send_message(
            chat.id,
            text=msg.INFO_SPEECH
        )
    elif message.text == 'Сейчас':
        report = get_meteo(
            mt.current_temperature,
            None,
            mt.today_shower
        )
        bot_v1.send_message(
            chat.id,
            text=f'Сейчас {report}'
        )
    elif message.text == 'Завтра':
        report = get_meteo(
            mt.tomorrow_temperature_max,
            mt.tomorrow_temperature_min,
            mt.tomorrow_shower
        )
        bot_v1.send_message(
            chat.id,
            text=f'Завтра днем {report}'
        )
    elif message.text == 'Покажи параметры':
        logging.info(
            f'user name: {chat.first_name}'
            f'user id: {chat.id}'
            )
        bot_v1.send_message(
            chat.id,
            text=(
                'TEST mode. v1\n'
                f'retry period: {cons.RETRY_PERIOD} sec.\n'
                f'retry mode: {cons.RETRY_MODE}\n\n'
                f'your tg name: {chat.first_name}\n'
                f'your id: {chat.id}\n\n'
                f'owner id: {perm.CHAT_ID_MAX}\n'
                f'contact mail: {contact_info}'
            )
        )


# TODO: think about response[0].get('url')
# now we have json collection as dict. whith key-'url'
# maybe better use url with picture directly
def get_cat():
    """Get cat pic from external API."""
    try:
        response = requests.get(endp.CAT_PIC_ENDPOINT)
    except Exception as error:
        logging.error(f'Connection error: {error}')
    response = requests.get(endp.CAT_PIC_ENDPOINT).json()
    return response[0].get('url')


def get_dog():
    """Get dog pic from external API."""
    try:
        response = requests.get(endp.DOG_PIC_ENDPOINT)
    except Exception as error:
        logging.error(f'Connection error: {error}')
    response = requests.get(endp.DOG_PIC_ENDPOINT).json()
    return response[0].get('url')


def get_meteo(max_temp: float, min_temp: float | None,
              showers: float) -> str:
    """Get meteo data from external API."""
    max_temp = int(max_temp)
    shower_float = showers
    # hyperlink = endp.HEAT_MCHS

    report = 'not available'

    if max_temp > 14 and max_temp <= 18:
        report = (
            f'{max_temp}{msg.summery_info['COLD_TEMP']}'
            )
    elif max_temp > 18 and max_temp < 26:
        report = (
            f'{max_temp}{msg.summery_info['NORMAL_TEMP']}'
            )
    elif max_temp in (26, 27, 28, 29, 30):
        report = (
            f'{max_temp}{msg.summery_info['HOT_TEMP']}'
            )
    elif max_temp > 30:
        report = (
            f'{max_temp}{msg.summery_info['VERY_HOT_TEMP']}'
            )
    if shower_float:
        report += msg.optional_reacts['RAIN']
    if min_temp:
        report += f'\nНочью: {int(min_temp)} °C'
    report += f'\ntest mode {mt.today_date}'

    return report


def say_hello(message) -> str:
    """Say hello to user."""
    chat = message.chat
    name = message.from_user.first_name

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(
        types.KeyboardButton('/menu'),
    )

    bot_v1.send_message(
        chat_id=chat.id,
        text=(
            f'Привет, {name}!\n' +
            msg.HELLO_SPEECH
        ),
        reply_markup=keyboard,
    )
