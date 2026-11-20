# Computer Helper — система удалённой технической поддержки

Лабораторная работа №1 по дисциплине «Методы и средства проектирования
информационных систем». Проект: Django 4.2 + Gunicorn, контейнер на базе
`python:3.11-slim`, мультиархитектурный образ (`linux/amd64`, `linux/arm64`).

## Запуск

Репозиторий: https://github.com/Roomanovilya/mispisit-lab1
Pull Request: https://github.com/Roomanovilya/mispisit-lab1/pull/1
Образ: https://hub.docker.com/r/romanovilya/mispisit-lab1

docker pull romanovilya/mispisit-lab1:0.0.1
docker run --rm -p 8080:8080 romanovilya/mispisit-lab1:0.0.1

После запуска открыть в браузере: http://localhost:8080

## Сборка (для разработчика)

docker buildx build --platform linux/amd64,linux/arm64 \
  -t romanovilya/mispisit-lab1:0.0.1 --push .

## Структура

- `Dockerfile` — сборка образа
- `requirements.txt` — зависимости (Django 4.2.16, Gunicorn 22.0.0)
- `config/` — настройки Django-проекта
- `core/` — приложение с первой страницей (`core/templates/core/index.html`)
<!-- lab1 -->
