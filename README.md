Веб-приложения для взаимодействия с Yandex.Disk

Функционал:

1.Просмотр файлов на Яндекс.Диске по вводу публичной ссылки (public_key)

2.Загрузка определенных файлов.

Технологии:

Python 3.7 Django 3.2.25

Как запустить проект: Клонировать репозиторий и перейти в него в командной строке:

git clone <>

Cоздать и активировать виртуальное окружение:

python -m venv venv && . venv/Scripts/activate

Установить зависимости из файла requirements.txt:

pip install -r requirements.txt

Выполнить миграции:

python manage.py migrate

Запустить проект:

python manage.py runserver

Переходим по адресу http://127.0.0.1:8000/

далее указываем публичную ссылку с Яндекс.Диска
