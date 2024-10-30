FROM python:3.12-slim

WORKDIR /app

COPY requirements_meteo.txt .

RUN pip install -r requirements_meteo.txt --no-cache-dir

COPY . .

CMD ["python", "main_bot.py", "run"]
