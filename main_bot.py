import logging
import os
import sys
import time
# from http import HTTPStatus

import requests
from dotenv import load_dotenv  # type: ignore
from telebot import TeleBot, apihelper  # type: ignore

from my_pet_bot import exceptions as exc  # type: ignore
from my_pet_bot import messages as msg  # type: ignore

load_dotenv()

RETRY_PERIOD = 30

CATS_API_KEY = os.getenv('CATS_API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID_MAX = os.getenv('CHAT_ID')

CAT_PIC_ENDPOINT = os.getenv('CAT_PIC_ENDPOINT')
DOG_PIC_ENDPOINT = os.getenv('DOG_PIC_ENDPOINT')


def check_tokens():
    """Check that all necessary envs are present."""
    tokens = {
        'CATS_API_KEY': CATS_API_KEY,
        'TELEGRAM_BOT_TOKEN': TELEGRAM_BOT_TOKEN,
    }

    report_list = []

    for name, token in tokens.items():
        if not token:
            report_list.append(name)
    if report_list:
        logging.critical(
            f'Please add the following envs tokens: {report_list}'
        )
        raise exc.CheckTokensEnvFailure(msg.TOKEN_MISSING)


def check_users():
    """Check added users."""
    logging.info('start checking users')
    users = {
        'CHAT_ID_MAX': CHAT_ID_MAX,
    }
    for user, token in users.items():
        if not token:
            logging.info(f'{user} not available')


def send_message(bot, message):
    """Send message to telegramm chat."""
    try:
        bot.send_message(CHAT_ID_MAX, message)
        logging.info('sended')
        return True
    except (
        apihelper.ApiException, requests.RequestException
    ) as error:
        logging.error(error)
        return False


def get_pic():
    """Get cat or dog pic from external API."""
    try:
        response = requests.get(CAT_PIC_ENDPOINT)
    except Exception as error:
        logging.error(f'Cat request failur:{error}')
        response = requests.get(DOG_PIC_ENDPOINT)

    random_pic = response.json().get('file')

    return random_pic


# FIXME:
def main():
    """pass."""
    logging.info(msg.CHECKING_TOKENS)
    check_tokens()
    check_users()
    logging.info(msg.END_CHECK)

    bot = TeleBot(TELEGRAM_BOT_TOKEN)

    # timestamp = int(time.time())

    send_message(bot, 'Bot is working. TEST mode')

    while True:
        bot.send_photo(CHAT_ID_MAX, get_pic())
        time.sleep(RETRY_PERIOD)


if __name__ == '__main__':
    log_format = (
        '%(asctime)s [%(levelname)s]'
        '(%(filename)s).%(funcName)s:%(lineno)d - %(message)s'
    )
    logging.basicConfig(
        format=log_format,
        level=logging.DEBUG,
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    main()
