"""test mode."""
import sys
import os

from dotenv import load_dotenv

import core.functions as func
import core.logging as log
import core.permissions as perm
import helpers.messages as msg

load_dotenv()

CHAT_ID_DARYA = os.getenv('CHAT_ID_DARYA')
CHAT_ID_MAX = os.getenv('CHAT_ID_MAX')
CHAT_ID_ALEX = os.getenv('CHAT_ID_ALEX')

weather_list = ['today', 'tomorrow']
pic_list = ['cat', 'dog']
info_list = ['functions', 'params', 'author']
afisha_list = ['mos_afisha', 'cinema_balt', 'cinema_otrada']


# TODO: need to do something with logging in main.
# mb replace to classes
def main():
    """pass."""
    log.logging.info(msg.info['CHECKING_TOKENS'])
    if perm.check_tokens():
        log.logging.critical(f'Corrupted tokens: {perm.check_tokens()}')
        sys.exit()
    log.logging.info(msg.info['END_CHECK'])
    # func.direct_initializator(CHAT_ID_DARYA)
    # func.direct_initializator(CHAT_ID_MAX)
    # func.direct_initializator(CHAT_ID_ALEX)

    func.bot_v1.message_handler(commands=['start'])(func.init_cmd)
    func.bot_v1.callback_query_handler(
        lambda call: call.data == 'start')(func.start.menu)
    func.bot_v1.callback_query_handler(
        lambda call: call.data == 'pictures')(func.pics.menu)
    func.bot_v1.callback_query_handler(
        lambda call: call.data == 'afisha')(func.afisha.menu)
    func.bot_v1.callback_query_handler(
        lambda call: call.data == 'weather')(func.weather.menu)
    func.bot_v1.callback_query_handler(
        lambda call: call.data == 'info')(func.info.menu)
    func.bot_v1.callback_query_handler(
        lambda call: call.data in weather_list)(func.weather_react)
    func.bot_v1.callback_query_handler(
        lambda call: call.data in pic_list)(func.picture_react)
    func.bot_v1.callback_query_handler(
        lambda call: call.data in info_list)(func.info_react)
    func.bot_v1.callback_query_handler(
        lambda call: call.data in afisha_list)(func.afisha_react)


# TODO: Lets cut log settings out of there
# be better do separate logg file in core directory.
if __name__ == '__main__':
    main()
    func.bot_v1.polling()
