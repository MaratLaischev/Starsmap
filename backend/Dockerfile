FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Создание пользователя и настройка прав
ARG GID=1000
ARG UID=1000

RUN groupadd -g "${GID}" -r web \
  && useradd -d '/code' -g web -l -r -u "${UID}" web \
  && mkdir -p '/code/staticfiles' '/code/media' \
  && chown -R web:web /code \
  && chmod -R 777 /code

COPY --chown=web:web . /code

USER web

ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    gunicorn --chdir /code --bind 0.0.0.0:8000 config.wsgi:application"]