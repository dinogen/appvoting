FROM ubuntu:latest
# come da http://containertutorials.com/docker-compose/flask-simple-app.html

MAINTAINER Reinhard Spisser "reinhard@spisser.it"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential sqlite3

RUN mkdir /app
RUN mkdir /app/database

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY web/ /app/
COPY database/ /app/database
VOLUME /opt/voting
ENTRYPOINT ["python"]
CMD ["index.py"]
