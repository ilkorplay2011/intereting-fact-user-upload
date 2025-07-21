# Interesting Fact User Upload

Простое Flask-приложение, позволяющее пользователям добавлять интересные факты и просматривать их.

---

## Описание

Пользователи могут отправлять факты через форму на странице `/post`, а на главной странице `/` отображается список всех добавленных фактов. Факты хранятся в текстовом файле `database.txt`.

---

## Запуск проекта локально

### Требования

- Python 3.7+
- Flask

### Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ilkorplay2011/intereting-fact-user-upload.git
cd intereting-fact-user-upload

Создайте виртуальное окружение и активируйте его:

Linux/macOS:

python3 -m venv venv
source venv/bin/activate

Windows CMD:

python -m venv venv
venv\Scripts\activate
Установите зависимости:
pip install flask
Запустите приложение:
python app.py
