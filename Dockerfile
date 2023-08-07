FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /django_demo

RUN apt-get update && apt-get install -y default-libmysqlclient-dev

COPY  requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


