"""test mode."""
import logging
import os
import sys
import time
# from http import HTTPStatus

import requests
from dotenv import load_dotenv  # type: ignore
from telebot import TeleBot, apihelper  # type: ignore

import exceptions as exc
import messages as msg

load_dotenv()

RETRY_PERIOD = 30

# CATS_API_KEY = os.getenv('CATS_API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID_MAX = os.getenv('CHAT_ID_MAX')

CAT_PIC_ENDPOINT = 'https://api.thecatapi.com/v1/images/search'
DOG_PIC_ENDPOINT = 'https://api.thedogapi.com/v1/images/search'


# TODO: We need to refactor this function.
# May be we can check and tokens and users in one.
def check_tokens():
    """Check that all necessary envs are present."""
    tokens = {
        # 'CATS_API_KEY': CATS_API_KEY,
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


# TODO: As i say this function need to refactoring.
def check_users():
    """Check added users."""
    logging.info('start checking users')
    users = {
        'CHAT_ID_MAX': CHAT_ID_MAX,
    }
    for user, token in users.items():
        if not token:
            logging.info(f'{user} not available')


# TODO: This func returns boolean. why.
def send_message(bot, message) -> bool:
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


# TODO: lets think about response[0].get('url')
# now we have json collection as dict. whith key - 'url'
# Its may be better use url with picture directly.
def get_pic():
    """Get cat or dog pic from external API."""
    try:
        response = requests.get(DOG_PIC_ENDPOINT)
    except Exception as error:
        logging.error(f'request failur:{error}')
    response = requests.get(DOG_PIC_ENDPOINT).json()
    return response[0].get('url')


# TODO: need to do something with logging.
def main():
    """pass."""
    logging.info(msg.CHECKING_TOKENS)
    check_tokens()
    check_users()
    logging.info(msg.END_CHECK)

    bot = TeleBot(token=TELEGRAM_BOT_TOKEN)

    # timestamp = int(time.time())

    send_message(
        bot,
        (
            'Bot is working. TEST mode\n'
            f'Retry period is {RETRY_PERIOD} sec.'
        )
    )

    while True:
        bot.send_photo(CHAT_ID_MAX, get_pic())
        # bot.send_message(CHAT_ID_MAX, 'this is a CAT/DOG PIC')
        time.sleep(RETRY_PERIOD)


# TODO: Lets cut log settings out of there
# be better do separate logg file in this directory.
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
