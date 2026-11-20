# Computer Helper — система удалённой технической поддержки

Лабораторная работа №2 по дисциплине «Методы и средства проектирования
информационных систем». В проекте реализованы три главные функции: 
создание заявки, просмотр списка заявок и обработка ошибочного сценария.
Платформа: Django 4.2 + Gunicorn. Данные хранятся в оперативной памяти.

## Запуск

Репозиторий: https://github.com/Roomanovilya/mispisit-lab1
Pull Request: https://github.com/Roomanovilya/mispisit-lab1/pull/2
Образ: https://hub.docker.com/r/romanovilya/mispisit-lab1

docker pull romanovilya/mispisit-lab1:0.0.2
docker run --rm -p 8080:8080 romanovilya/mispisit-lab1:0.0.2

После запуска открыть в браузере: http://localhost:8080

## Реализованные страницы

- `/` — Главная страница
- `/tickets` — Список всех заявок (просмотр)
- `/tickets/new` — Создание новой заявки (изменение данных)
- `/tickets/1` — Карточка конкретной заявки
- Ошибочный сценарий: при попытке создать заявку с пустой темой выводится страница с ошибкой.

## Структура

- `Dockerfile` — сборка образа
- `requirements.txt` — зависимости (Django 4.2.16, Gunicorn 22.0.0)
- `config/` — настройки Django-проекта и маршруты (`urls.py`)
- `core/views.py` — три главные функции (обработчики)
- `core/store.py` — демо-данные 
- `core/templates/core/` — HTML-шаблоны страниц
