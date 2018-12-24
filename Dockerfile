FROM tiangolo/uwsgi-nginx-flask:python3.6

MAINTAINER Reinhard Spisser "reinhard@spisser.it"
RUN apt-get update -y
RUN apt-get install -y sqlite3
RUN apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
RUN mkdir -p /opt/voting

RUN mkdir -p /opt/voting/bin
RUN mkdir -p /opt/voting/database

RUN rm -fr /opt/voting/elections
RUN mkdir -p /opt/voting/elections
run mkdir -p /var/www/voting/frontend/web

COPY backend/ /opt/voting/bin
RUN chmod +x /opt/voting/bin/*
COPY requirements.txt /
RUN pip install -r /requirements.txt
WORKDIR /var/www/voting/frontend/web
COPY frontend/web/ /var/www/voting/frontend/web/
COPY frontend/web/ /app
COPY frontend/web/index.py /app/main.py
COPY frontend/database/ /opt/voting/database
ARG version
ENV voting_version=$version
VOLUME /opt/voting/database
