import logging
import os
import sys
import time
# from http import HTTPStatus

# import requests
from dotenv import load_dotenv
from telebot import TeleBot  # type: ignore

from my_pet_bot import exceptions as exc
from my_pet_bot import messages as msg

load_dotenv()

CATS_API_KEY = os.getenv('CATS_API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID_MAX = os.getenv('CHAT_ID')

CAT_PIC_ENDPOINT = 'https://api.thecatapi.com/v1/images/search'


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
            logging.info(f'{user} is not added')


# TODO:  do messages func
def send_message(bot, message):
    """Send message to telegramm chat."""
    bot.send_message(CHAT_ID_MAX, message)
    logging.info(msg.SENDED)


# FIXME:
def main():
    """pass."""
    logging.info(msg.CHECKING_TOKENS)
    check_tokens()
    logging.info(msg.END_CHECK)

    bot = TeleBot(TELEGRAM_BOT_TOKEN)

    timestamp = int(time.time())

    # while True:
    #     try:


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
