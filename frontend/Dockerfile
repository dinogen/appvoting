FROM ubuntu:latest
# come da http://containertutorials.com/docker-compose/flask-simple-app.html

MAINTAINER Reinhard Spisser "reinhard@spisser.it"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]
