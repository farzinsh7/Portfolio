FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD admin

RUN mkdir /app
WORKDIR /app

RUN apk update
RUN apk add --no-cache gcc python3-dev musl-dev

ADD requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apk del gcc python3-dev musl-dev

CMD gunicorn -b 0.0.0.0:8000 core.wsgi