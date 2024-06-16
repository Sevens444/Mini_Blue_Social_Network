FROM python:3.12-slim

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

ENV FLASK_APP="main"

CMD ["flask", "run", "--host=0.0.0.0"]