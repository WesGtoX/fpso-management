build:
	@docker-compose build

bash:
	@docker-compose run --rm api bash

run:
	@docker-compose up

test:
	@docker-compose run --rm api pytest

user:
	@docker-compose run --rm api ./manage.py createsuperuser

down:
	@docker-compose down -v
