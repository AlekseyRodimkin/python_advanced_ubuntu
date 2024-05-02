import datetime
from flask import Flask

app = Flask(__name__)
starts_count = 0


@app.route('/test')
def test_function():
    now = datetime.datetime.now().utcnow()
    return f'Это тестовая страничка, ответ сгенерирован в {now}'


@app.route('/hello_world')
def hello_world():
    now = datetime.datetime.now().utcnow()
    return f'Hello World, ответ сгенерирован в {now}'


@app.route('/counter')
def counter():
    now = datetime.datetime.now().utcnow()
    global starts_count
    starts_count += 1
    return f'Запуск номер {starts_count}, ответ сгенерирован в {now}'
