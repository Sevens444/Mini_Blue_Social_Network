FROM python:3.12-slim

WORKDIR /app
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app /app

# скрипт начальной настройки
#COPY entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh
#ENTRYPOINT ["/entrypoint.sh"]

CMD [ "python", "__init__.py" ]