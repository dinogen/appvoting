FROM tiangolo/uwsgi-nginx-flask:python3.6

MAINTAINER Reinhard Spisser "reinhard@spisser.it"
RUN apt-get update -y
RUN apt-get install -y sqlite3

RUN mkdir -p /opt/voting
RUN mkdir -p /opt/voting/backend
run mkdir -p /var/www/voting/frontend/web

COPY backend/ /opt/voting/backend
RUN chmod +x /opt/voting/backend/*
COPY requirements.txt /
RUN pip install -r /requirements.txt
WORKDIR /var/www/voting/frontend/web
COPY frontend/web/ /var/www/voting/frontend/web/
COPY frontend/web/ /app
COPY frontend/web/index.py /app/main.py
COPY frontend/database/ /opt/voting
ARG version
ENV voting_version=version
VOLUME /opt/voting
