"""test mode."""
import logging
import sys

import functions as func
import messages as msg
import permissions as perm


# TODO: need to do something with logging.
def main():
    """pass."""
    logging.info(msg.info['CHECKING_TOKENS'])
    if perm.check_tokens():
        logging.info(f'Corrupted tokens: {perm.check_tokens()}')
        sys.exit()
    logging.info(msg.info['END_CHECK'])

    # func.direct_initialization('CHAT_ID_DARYA')
    func.bot_v1.message_handler(commands=['start'])(func.say_hello)
    func.bot_v1.message_handler(commands=['menu'])(func.main_menu)
    func.bot_v1.message_handler(commands=['weather'])(func.weather_menu)
    func.bot_v1.message_handler(content_types=['text'])(func.react)


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
