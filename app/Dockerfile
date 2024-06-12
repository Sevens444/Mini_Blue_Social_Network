FROM python:3.12-slim

WORKDIR /root

COPY . /root
RUN pip install -r requirements.txt

# скрипт начальной настройки
#COPY entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh
#ENTRYPOINT ["/entrypoint.sh"]
ENV FLASK_APP="main"

CMD ["flask", "run", "--host=0.0.0.0"]