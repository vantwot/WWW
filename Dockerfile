FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requirement.txt /code/

RUN python -m pip install -r requirement.txt

COPY . /code/

EXPOSE 8000