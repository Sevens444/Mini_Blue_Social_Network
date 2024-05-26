# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем зависимости
WORKDIR /app
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Копируем код приложения
COPY app /app

# Добавляем скрипт начальной настройки
#COPY entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh

# Запускаем скрипт начальной настройки
#ENTRYPOINT ["/entrypoint.sh"]
