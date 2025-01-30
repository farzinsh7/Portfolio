FROM python:3.10-slim-buster

LABEL maintainer="farzinnater@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y build-essential libpq-dev
RUN rm -rf /var/lib/apt/lists/*

ADD requirements.txt .

COPY ./volumes/app .

RUN pip install --upgrade pip && pip install -r requirements.txt