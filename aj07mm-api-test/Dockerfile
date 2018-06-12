FROM python:3.6

WORKDIR /app

ENV PYTHONPATH '.'
ENV APPLICATION_ROOT '.'

ADD requirements.txt $APPLICATION_ROOT

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD pytest tests && python web/api.py

EXPOSE 8080
EXPOSE 27017

ADD . /app
