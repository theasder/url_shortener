
build:
	docker-compose build
up:
	docker-compose up -d
down:
	docker-compose down
test:
	docker-compose exec server /bin/sh | python3 -m unittest discover tests/
