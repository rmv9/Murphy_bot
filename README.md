# project "Murphy"
Murphy - это интерактивный Телеграм бот-ассистент  

### Возможности
* Предоставляет развлекательный контент с открытых api источников.  
* Сообщает о погоде (open-meteo api) на разные временные интервалы, согласно запроса.  
* Предоставляет афишу по предустановленным кинотеатрам (hyperlink)  

### Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/rmv9/Murphy_bot.git
```

```
cd Murphy_bot
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

В проекте предусмотрено несколько файлов с зависимостями  
Установить зависимости из файла requirements_meteo.txt:

```
pip install --upgrade pip
pip install setuptools
```

```
pip install requirements_meteo.txt
```

Используйте .env для хранения токенов:
<img src=""/>

Запустить проект:

```
python main_bot.py
```

## Пример работы:
<img src="https://i.postimg.cc/jSGFGFnd/Screenshot-2024-09-01-12-48-37-823-org-telegram-messenger-edit.jpg">
<img src=""/>
<img src=""/>
<img src=""/>



## Автор проекта
Максим Раздорожный  
[Электронная почта](mailto:rmv_93@mail.ru)   
[Telegram](https://t.me/rmv_dev)
