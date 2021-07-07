# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y cron

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab && \
    crontab /etc/cron.d/crontab

COPY . /code/
