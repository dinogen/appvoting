#FROM ubuntu:latest
# come da http://containertutorials.com/docker-compose/flask-simple-app.html
FROM python:3.6

MAINTAINER Reinhard Spisser "reinhard@spisser.it"
RUN apt-get update -y
#RUN apt-get install -y python python-pip python-dev build-essential sqlite3
RUN apt-get install -y sqlite3

RUN mkdir /app
RUN mkdir /app/database

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY web/ /app/
COPY database/ /app/database
#COPY database/ /opt/voting
VOLUME /opt/voting
ENTRYPOINT ["python"]
CMD ["index.py"]
