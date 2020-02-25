FROM python:2.7-alpine

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD flask run --host=$DOMAIN_NAME --port=5000
