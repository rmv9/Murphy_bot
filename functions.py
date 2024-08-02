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
afisha = 'https://www.mos.ru/afisha/'


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
        text=msg.direct_messages['STARTING_MSG'],
        reply_markup=keyboard,
    )


def start_menu(message) -> str:
    """Say hello to user."""
    chat = message.chat
    name = message.from_user.first_name

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(
        types.KeyboardButton(msg.start_keys['MAIN_MENU']),
    )

    bot_v1.send_message(
        chat_id=chat.id,
        text=(
            f'Привет, {name}!\n' +
            msg.HELLO_SPEECH
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
        types.KeyboardButton('/info'),
        types.KeyboardButton('/weather'),
    )
    keyboard.row(  # Вторая строка кнопок.
        types.KeyboardButton('Пришли собачку'),
        types.KeyboardButton('Пришли котика'),
    )
    # keyboard.row(  # Третья строка кнопок.
    #     types.KeyboardButton('/weather'),
    # )
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
        types.KeyboardButton(msg.weather_keys['TODAY']),
        types.KeyboardButton(msg.weather_keys['TOMORROW']),
    )
    keyboard.row(
        types.KeyboardButton(msg.weather_keys['WEEK']),
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


def info_menu(message):
    """pass."""
    chat = message.chat
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(
        types.KeyboardButton(msg.info_keys['PARAMS']),
        types.KeyboardButton(msg.info_keys['AUTHOR']),
    )
    keyboard.row(
        types.KeyboardButton('/menu'),
    )
    bot_v1.send_message(
        chat_id=chat.id,
        text='Доступны параметры работы и контакты разработчика',
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
    elif message.text == 'Сегодня':
        report = get_meteo(
            mt.today_temperature_max,
            mt.today_temperature_min,
            mt.today_shower,
            today=True
        )
        bot_v1.send_message(
            chat.id,
            text=f'{report}'
        )
        bot_v1.send_message(
            chat.id,
            text=f'Сейчас {int(mt.current_temperature_2m)} °C'
        )
        bot_v1.send_message(
            chat.id,
            text=f'Ветер {int(mt.current_wind_speed_10m)} м/с'
        )
        bot_v1.send_message(
            chat.id,
            text=f'Влажность {int(mt.current_relative_humidity_2m)} %'
        )
        bot_v1.send_message(
            chat.id,
            text=f'Куда можно сходить сегодня\n{afisha}'
        )
    elif message.text == 'Завтра':
        report = get_meteo(
            mt.tomorrow_temperature_max,
            mt.tomorrow_temperature_min,
            mt.tomorrow_shower,
        )
        bot_v1.send_message(
            chat.id,
            text=f'{report}'
        )
    elif message.text == 'Параметры':
        logging.info(
            f'user name: {chat.first_name}'
            f'user id: {chat.id}'
            )
        bot_v1.send_message(
            chat.id,
            text=(
                'TEST mode. v1\n'
                f'retry period: {cons.RETRY_PERIOD} sec.\n'
                f'meteo_api: True\n'
                f'retry mode: {cons.RETRY_MODE}\n\n'
                f'your tg name: {chat.first_name}\n'
                f'your id: {chat.id}\n\n'
                f'owner id: {perm.CHAT_ID_MAX}\n'
                f'contact mail: {contact_info}'
            )
        )
    elif message.text == 'Автор':
        bot_v1.send_message(
            chat.id,
            text=f'{msg.contact_info['TG']}',
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
              showers: float, today=False) -> str:
    """Get meteo data from external API."""
    max_temp = int(max_temp)
    if min_temp:
        min_temp = int(min_temp)
    shower_float = showers

    report = (
        f'{max_temp}-{min_temp} {msg.min_max_temp}'
        )
    if shower_float:
        report += msg.optional_reacts['RAIN']

    if not today:
        return report

    if max_temp > 14 and max_temp <= 18:
        report += (
            f'{msg.temp_react['COLD_TEMP']}'
            )
    elif max_temp > 18 and max_temp < 26:
        report += (
            f'{msg.temp_react['NORMAL_TEMP']}'
            )
    elif max_temp in (26, 27, 28, 29, 30):
        report += (
            f'{msg.temp_react['HOT_TEMP']}'
            )
    elif max_temp > 30:
        report += (
            f'{msg.temp_react['VERY_HOT_TEMP']}'
            )

    return report
