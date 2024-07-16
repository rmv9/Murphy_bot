"""functions."""
import requests
import logging

from telebot import apihelper

from endpoints import (
    CAT_PIC_ENDPOINT, DOG_PIC_ENDPOINT,
    )
import permissions as perm


# TODO: lets think about response[0].get('url')
# now we have json collection as dict. whith key - 'url'
# Its may be better use url with picture directly.
def get_cat():
    """Get cat pic from external API."""
    try:
        response = requests.get(CAT_PIC_ENDPOINT)
    except Exception as error:
        logging.error(f'Connection error: {error}')
    response = requests.get(CAT_PIC_ENDPOINT).json()
    return response[0].get('url')


def get_dog():
    """Get dog pic from external API."""
    try:
        response = requests.get(DOG_PIC_ENDPOINT)
    except Exception as error:
        logging.error(f'Connection error: {error}')
    response = requests.get(DOG_PIC_ENDPOINT).json()
    return response[0].get('url')


# TODO: Not boolean now.
def send_message(bot, message):
    """Send message to telegramm chat."""
    try:
        bot.send_message(perm.CHAT_ID_MAX, message)
        logging.info('sended')
    except (
        apihelper.ApiException, requests.RequestException
    ) as error:
        logging.error(error)


def send_photo(bot, photo):
    """Send photo to telegramm chat."""
    try:
        bot.send_photo(perm.CHAT_ID_MAX, photo)
        logging.info('sended')
    except (
        apihelper.ApiException, requests.RequestException
    ) as error:
        logging.error(error)


def get_meteo():
    """Get meteo data from external API."""
    pass