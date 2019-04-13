FROM python:3.7-alpine

ENV APP_PATH /app
RUN mkdir -p ${APP_PATH}

WORKDIR ${APP_PATH}
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
CMD gunicorn -b 0.0.0.0:5000 --access-logfile - "app:create_app()"