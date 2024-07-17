"""test mode."""
import logging
import sys
import datetime as dt

from telebot import TeleBot, types  # type: ignore

import functions as func
import messages as msg
import permissions as perm
import meteo as mt

contact_info = 'rmv.msk@mail.ru'


RETRY_PERIOD = 30
RETRY_MODE = False

now = dt.datetime.now()
current_hour = now.time().hour

bot = TeleBot(token=perm.TELEGRAM_BOT_TOKEN)


# TODO: need to do something with logging.
def main():
    """pass."""
    logging.info(msg.CHECKING_TOKENS)
    if perm.check_tokens():
        logging.info(f'Corrupted tokens: {perm.check_tokens()}')
        sys.exit()
    logging.info(msg.END_CHECK)

    @bot.message_handler(commands=['start'])
    def wake_up(message):
        """pass."""
        chat = message.chat
        name = message.chat.first_name
        # Создаём объект клавиатуры:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row(  # Первая строка кнопок.
            types.KeyboardButton('Отправь мне погоду на улице'),  # Первую кнопку в строке.
            types.KeyboardButton('Пришли собачку'),
        )
        keyboard.row(  # Вторая строка кнопок.
            types.KeyboardButton('Покажи параметры'),
            types.KeyboardButton('Пришли котика'),
        )
        bot.send_message(
            chat_id=chat.id,
            text=(
                f'Привет {name}, меня зовут Murphy, я бот-ассистент!\n'
                'Я еще только учусь и пока мои возможносмти ограничены :)\n'
                'Но я уже могу подсказать тебе температуру за окном '
                'или отправить картинки с забавными животными.\n\n'
                'в Параметрах я покажу актуальный режим моей работы '
                'твой id и контакты разработчика\n'
                'В поле chat id будет указан id твоего аккаунта Телеграм\n'
            ),
            reply_markup=keyboard,  # Отправляем клавиатуру в сообщении бота.
        )

    @bot.message_handler(content_types=['text'])
    def react(message):
        """pass."""
        chat = message.chat
        if message.text == 'Пришли котика':
            bot.send_photo(chat.id, func.get_cat())
        elif message.text == 'Пришли собачку':
            bot.send_photo(chat.id, func.get_dog())
        elif message.text == 'Отправь мне погоду на улице':
            bot.send_message(
                chat.id,
                text=(
                    'Сейчас на улице: '
                    f'{int(mt.hourly_temperature_2m[current_hour])} С°'
                )
            )
        elif message.text == 'Покажи параметры':
            bot.send_message(
                chat.id,
                text=(
                    'bot in TEST mode. v1\n'
                    f'retry period: {RETRY_PERIOD} sec.\n'
                    f'retry mode: {RETRY_MODE}\n\n'
                    f'your tg name: {chat.first_name}\n'
                    f'your id: {chat.id}\n\n'
                    f'owner id: {perm.CHAT_ID_MAX}\n'
                    f'contact mail: {contact_info}'
                )
            )


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
    bot.polling()
