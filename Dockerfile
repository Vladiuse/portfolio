# Dockerfile
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

CMD python manage.py migrate \
    && python3 manage.py init_superuser \
    && python manage.py collectstatic --no-input \
    && gunicorn config.wsgi:application --bind 0.0.0.0:8000
