"""Pass."""

# contact
contact_info = {
    'MAIL': 'rmv.msk@mail.ru',
    'TG': '@rmv_dev'
    }

# errors
sys_err = {
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
sys_info = {
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
    '• Погода на завтра\n'
    '• Афиша событий в Москве\n'
    '• Случайная фотография (кот или собака)\n'
    '• Контактная информация разработчика\n'
)

# dialogs
direct_messages = {
    'TEST': (
        'test\n'

    ),
    'STARTING_MSG': (
        'Функции:\n'
        f'{functions}'

    ),
}
HELLO_SPEECH = (
    'Меня зовут Мёрфи, я бот-помощник! ☺'
)

TO_MAIN = (
    'Главное меню'
)


# weather
min_max_temp = '°C ночь - день'

weather = {
    'WIND': 'Ветер',
    'W_SPEED': 'м/с',
    'HUMID': 'Влажность',
    'RAIN': '% вероятность осадков'
}

opt_react = {
    'RAIN': (
        '% вероятность осадков'
    ),
    'SNOW': (
        'Возможно, сегодня пойдёт снег'
    ),
}

# afisha menu keyboard
afisha_btns = {
    'BALT': 'Кино-Балтика',
    'OTRADA': 'Кино-Отрада',
    'EVENTS': 'События',
    'BACK': 'Другую афишу',
}

# start menu keyboard
main_btns = {
    'MAIN_MENU': 'На главную',
    'PICS': 'Картинки',
    'WEATH': 'Погода',
    'INFO': 'Инфо',
    'AFISHA': 'Афиша',
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
weather_btns = {
    'TODAY': 'Сегодня',
    'TOMORROW': 'Завтра',
    'WEEK': 'На неделю',
}

# short descript
menu_brief = {
    'WEATHER': 'Погода в Москве',
    'INFO': 'Информация',
    'AFISHA': 'Афиша',
    'PICS': 'Фотографии котов и собак',
}
