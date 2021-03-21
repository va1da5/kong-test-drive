.PHONY: up down restart-kong

up:
	docker-compose up -d

down:
	docker-compose down -v --rmi all --remove-orphans

restart-kong:
	docker-compose rm -sf kong
	docker-compose up -d kong
