"""test mode."""
import logging
import sys
import time

from telebot import TeleBot, types  # type: ignore

import functions as func
import messages as msg
import permissions as perm

RETRY_PERIOD = 30


# TODO: need to do something with logging.
def main():
    """pass."""
    logging.info(msg.CHECKING_TOKENS)
    if perm.check_tokens():
        logging.info(f'Corrupted tokens: {perm.check_tokens()}')
        sys.exit()
    logging.info(msg.END_CHECK)

    bot = TeleBot(token=perm.TELEGRAM_BOT_TOKEN)

    func.send_message(
        bot,
        (
            'Bot is working. TEST mode\n'
            f'Retry period is {RETRY_PERIOD} sec.'
        )
    )

    while True:
        # send_message(bot, 'a simple test message')
        func.send_photo(bot, func.get_pic())
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
