1)Install Docker
	https://docs.docker.com/engine/install/

2)Commands to run

docker network create microservices 
docker build . -f client/dockerfile -t client
docker build . -f server/dockerfile -t server

terminal-1: 
	docker run -ti --name server --net microservices -p 127.0.0.1:50051:50051/tcp server 
terminal-2:
	docker run -ti --net microservices -e SERVER_HOST=server client