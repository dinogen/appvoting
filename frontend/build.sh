VER=$1
docker build -t test-microservizi:$VER .

docker run -p 5000:5000 test-microservizi:$VER