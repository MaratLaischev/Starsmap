# Starsmap

## Описание проекта

Starsmap - это система по оценке компетенций сотрудников. Она предоставляет дашборд аналитики по навыкам в команде, который позволяет руководителю увидеть состояние навыков в команде и помогает в развитии команды. Дашборд сокращает время на анализ состояния команды, что позволяет эффективнее планировать развитие команды и найм сотрудников.

## Стек технологий

- Python 3.12
- Django 4.2
- PostgreSQL
- Docker
- Docker Compose

## Запуск проекта

### Локальный запуск

1. Клонируйте репозиторий:
    ```shell
    git clone git@github.com:MaratLaischev/Starsmap.git
    cd backend
    ```

2. Установить и запустить виртуальное окружение:
    ```shell
    python3.12 -m venv venv
    source venv/Scripts/activate
    ```

3. Создайте файл .env, скопируйте в него содержимое .env.example и установите зависимости:
    ```shell
    python -m pip install --upgrade pip && pip install -r requirements.txt
    ```

3. Выполните миграции:
    ```shell
    python manage.py makemigrations && python manage.py migrate
    ```

4. Импортируйте данные:
    ```shell
    python manage.py import_data
    ```

5. Запустите сервер:
    ```shell
    python manage.py runserver
    ```

### Запуск с использованием Makefile

1. Клонируйте репозиторий:
    ```shell
    git clone https://github.com/your-username/starsmap.git
    cd backend
    ```

2. Соберите Docker образы:
    ```shell
    make build
    ```

3. Запустите контейнеры:
    ```shell
    make up
    ```

4. Выполните миграции:
    ```shell
    make migrate
    ```

5. Импортируйте данные:
    ```shell
    make import
    ```

6. Запустите сервер:
    ```shell
    make runserver
    ```

## Команды Makefile

- `make help`: Показать доступные команды.
- `make build`: Собрать Docker образы.
- `make up`: Запустить контейнеры.
- `make down`: Остановить и удалить контейнеры.
- `make migrate`: Применить миграции базы данных.
- `make createsuperuser`: Создать суперпользователя.
- `make collectstatic`: Собрать статические файлы.
- `make makemigrations`: Создать миграции базы данных.
- `make push`: Загрузить Docker образ в Docker Hub.
- `make import`: Импортировать данные в базу данных.
- `make runserver`: Запустить локальный сервер.
- `make lint`: Запустить линтеры.
- `make test`: Запустить тесты.

## Документация API

Документация API генерируется с использованием `drf-spectacular` и доступна по следующим адресам:

- **Swagger UI**: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
- **Redoc**: [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)

- **Проект размещен на сервере, получен домен, настроен SSL-сертификат**:
- [https://rosbank-hackathon.bounceme.net/swagger/](https://rosbank-hackathon.bounceme.net/swagger/)

## Разработчики

[Павел Охрим](https://github.com/d1g-1t)

[Марат Лайшев](https://github.com/MaratLaischev)
