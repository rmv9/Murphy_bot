"""Pass."""

# contact
contact_info = {
    'MAIL': 'rmv.msk@mail.ru',
    'TG': '@rmv_dev'
    }

# errors
errors = {
    'MAIN_ERROR': 'Ошибка работы программы',
    'SEND_FAILED': 'Не удалось отправить сообщение',
    'RESPONSE_NOT_DICT': 'Ответ от API не является словарем',
    'RESPONSE_NOT_LIST': 'Ответ от API не является списком',
    'RESPONSE_EMPTY': 'Ответ от API пуст',
    'KEY_MISSING': 'Отсутствует ключ',
    'TOKEN_MISSING': 'Отсутствует токен',
    'STATUS_INCORRECT': 'Некорректный статус работы',
    'RESP_CODE_FAILED': 'Некорректный код ответа',
}

# info
info = {
    'SEND': 'Отправка сообщения',
    'SENDED': 'Сообщение отправлено',
    'API_REQUEST': 'Запрос к API',
    'CHECK_RESPONSE': 'Проверка соответствия ответа',
    'STARTING': 'Начало работы',
    'END_CHECK': 'ОК',
    'PARSING': 'Начало парсинга',
    'END_PARSE': 'Завершение парсинга',
    'CHECKING_TOKENS': 'Проверка токенов',
    'WAITS': 'Ожидание обновления',
    'STATUS_CHANGED': 'Статус работы изменился',
}

author = contact_info['MAIL']

functions = (
    '• Погода на сегодня (и в данный момент)\n'
    '• Показания ветра и влажности\n'
    '• Погода на завтра\n'
    '• Прогноз на неделю (не доступен)\n'
    '• Афиша событий в Москве\n'
    '• Случайная фотография (кот или собака)\n'
    '• Добавлена контактная информация для '
    'связи с автором бота\n'
)

# dialogs
direct_messages = {
    'TEST': (
        'test\n'
        'Есть обновления! Оцени навигацию. '
        'Сейчас не работает только погода на неделю, '
        'остальное должно функционировать'

    ),
    'STARTING_MSG': (
        'Функции:\n'
        f'{functions}'

    ),
}
HELLO_SPEECH = (
    'Меня зовут Мёрфи, я бот-помощник! ☺\n'
)
INFO_SPEECH = (
    'Здесь доступна справочная информация, '
    'некоторые параметры текущего сеанса '
    'и гид по функциям данной версии'
)
START_GUIDE = (
    'Что будем смотреть?'
)


# weather react
min_max_temp = '°C ночь - день\n'

optional_reacts = {
    'RAIN': (
        '% вероятность осадков\n'
    ),
    'SNOW': (
        'Возможно, сегодня пойдёт снег\n'
    ),
}
temp_react = {
    'VERY_COLD_TEMP': 'pass',
    'COLD_TEMP': (
        'Прохладно\n'
    ),
    'NORMAL_TEMP': (
        'Комфортная температура\n'
    ),
    'HOT_TEMP': (
        'Тепло и даже жарко!\n'
        'Полезная информация о мерах безопасности:\n'

    ),
    'VERY_HOT_TEMP': (
        'Жарко, повышенная температура!\n'
        'Полезная информация о мерах безопасности:\n'
    ),
}


# afisha menu k

# start menu keyboard
start_keys = {
    'MAIN_MENU': 'На главную',
}

# main menu keyboard
main_keys = {
    'WEATHER_MENU': '/weather',
    'INFO_MENU': '/info',
    'AFISHA_MENU': '/afisha',

}

# info menu keyboard
info_menu = {
    'AUTHOR': 'Автор',
    'PARAMS': 'Параметры',
    'GUIDE': 'Гид по функциям',
}

# weather menu keyboard
weather_keys = {
    'TODAY': 'Сегодня',
    'TOMORROW': 'Завтра',
    'WEEK': 'На неделю',
}
