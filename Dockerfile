FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /django_demo

RUN apt-get update

COPY  . .
RUN pip3 install -r requirements.txt



