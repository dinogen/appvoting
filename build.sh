VER=$1
docker build --build-arg version=$VER -t voting:$VER .
