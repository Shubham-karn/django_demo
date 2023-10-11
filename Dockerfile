FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /django_demo

RUN apt-get update 

COPY  requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
RUN pip3 install psycopg2-binary

EXPOSE 8000

CMD [ "gunicorn", "-c", "gunicorn.py", "hello.wsgi:application" ]

