DOCKER_COMPOSE_FILE=docker-compose.yml
DOCKER_COMPOSE=docker-compose -f $(DOCKER_COMPOSE_FILE)
ENV_FILE=.env

include $(ENV_FILE)
export $(shell sed 's/=.*//' $(ENV_FILE))

# Команды
.PHONY: help build up down migrate createsuperuser collectstatic makemigrations push import runserver lint test

help: ## Показать доступные команды
	@echo "Использование: make [команда]"
	@echo ""
	@echo "Доступные команды:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}' | sort

build: ## Собирает Docker образы
	$(DOCKER_COMPOSE) build

up: ## Запускает контейнеры
	$(DOCKER_COMPOSE) up -d

down: ## Останавливает и удаляет контейнеры
	$(DOCKER_COMPOSE) down

migrate: ## Применяет миграции базы данных
	$(DOCKER_COMPOSE) exec web python manage.py migrate

createsuperuser: ## Создает суперпользователя
	$(DOCKER_COMPOSE) exec web python manage.py createsuperuser

collectstatic: ## Собирает статические файлы
	$(DOCKER_COMPOSE) exec web python manage.py collectstatic --noinput

makemigrations: ## Создает миграции базы данных
	$(DOCKER_COMPOSE) exec web python manage.py makemigrations

push: ## Загружает Docker образ в Docker Hub
	docker build -t $(DOCKERHUB_USERNAME)/rosbank_backend:latest .
	docker push $(DOCKERHUB_USERNAME)/rosbank_backend:latest

import: ## Импортирует данные в базу данных
	python manage.py import_data

runserver: ## Запускает локальный сервер
	python manage.py runserver

lint: ## Запускает линтеры
	flake8 . && black --check .

test: ## Запускает тесты
	python manage.py test

pre-commit: ## Запускает pre-commit
	pre-commit run --all-files
