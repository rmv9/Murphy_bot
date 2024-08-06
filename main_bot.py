"""test mode."""
import logging
import sys
import os

from dotenv import load_dotenv

import core.functions as func
import helpers.messages as msg
import core.permissions as perm

load_dotenv()

CHAT_ID_DARYA = os.getenv('CHAT_ID_DARYA')
CHAT_ID_MAX = os.getenv('CHAT_ID_MAX')
CHAT_ID_ALEX = os.getenv('CHAT_ID_ALEX')

weather_list = ['today', 'tomorrow']
pic_list = ['cat', 'dog']
info_list = ['functions', 'params', 'author']
afisha_list = ['mos_afisha', 'cinema_balt', 'cinema_otrada']


# TODO: need to do something with logging.
def main():
    """pass."""
    logging.info(msg.info['CHECKING_TOKENS'])
    if perm.check_tokens():
        logging.info(f'Corrupted tokens: {perm.check_tokens()}')
        sys.exit()
    logging.info(msg.info['END_CHECK'])
    # func.direct_initialization(CHAT_ID_DARYA)
    # func.direct_initialization(CHAT_ID_MAX)
    # func.direct_initialization(CHAT_ID_ALEX)

    func.bot_v1.message_handler(commands=['start'])(func.init_cmd)
    func.bot_v1.callback_query_handler(
        func=lambda call: call.data == 'start')(func.start_menu)
    func.bot_v1.callback_query_handler(
        func=lambda call: call.data == 'pictures')(func.pics_menu)
    func.bot_v1.callback_query_handler(
        func=lambda call: call.data == 'afisha')(func.afisha_menu)
    func.bot_v1.callback_query_handler(
        func=lambda call: call.data == 'weather')(func.weather_menu)
    func.bot_v1.callback_query_handler(
        func=lambda call: call.data == 'info')(func.info_menu)
    func.bot_v1.callback_query_handler(
        func=lambda call: call.data in weather_list)(func.weather_react)
    func.bot_v1.callback_query_handler(
        func=lambda call: call.data in pic_list)(func.picture_react)
    func.bot_v1.callback_query_handler(
        func=lambda call: call.data in info_list)(func.info_react)
    func.bot_v1.callback_query_handler(
        func=lambda call: call.data in afisha_list)(func.afisha_react)


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
    func.bot_v1.polling()
