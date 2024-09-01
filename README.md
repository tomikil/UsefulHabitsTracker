Проект "Трекер полезных привычек". Данный проект испозуеться с Docker для контейнеризации, Django REST Framework для создания API, Celery для асинхронной обработки задач и Celery-beat для периодических задач

Запуск проекта:
1. Создайте файл .env в корневой директории и заполните необходимые переменные окружения наоснове файла .env.sample/
2. Примените миграции:
    python3 manage.py migrate

3. Запустите сервер:
    python3 manage.py runserver

4. Запустите Celery для обработки отложенных задач:
    celery -A config worker -l INFO
    celery -A config beat -l INFO

5. Используйте команду csu для создания тестового суперпользователя
    python manage.py csu

6. Подготовьте телеграм бота для отправки данных
    Запустите бота командой /start

Для запуска проекта через Docker необходимо:
1. docker compose build - сборка образа
2. docker compose up - запуск контейнера

Документация API

Документация API доступна после запуска сервера по адресу: http://localhost:8000/redoc/ или http://localhost:8000/swagger/
