VER=$1
docker build -t voting:$VER .

docker run -d -p 5000:5000 -v /opt/voting:/opt/voting voting:$VER
