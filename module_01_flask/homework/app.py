import datetime
from flask import Flask
import random
from pathlib import Path


app = Flask(__name__)
cars_names = "Chevrolet, Renault, Ford, Lada"
breeds_cats = ['Корниш-рекс', 'Русская голубая', 'Шотландская вислоухая', 'Мейн-кун', 'Манчкин']
words_war_and_peace = [word for word in Path('war_and_peace.txt').read_text(encoding="utf-8").replace("\n", " ").split()]
counter_visits = 0


@app.route('/hello_world')
def hello_world():
    return f"Привет, мир!"


@app.route('/cars')
def cars():
    return cars_names


@app.route('/cats')
def cats():
    return random.choice(breeds_cats)


@app.route('/get_time/now')
def get_time_now():
    time_now = datetime.datetime.now()
    return "Точное время: {current_time}".format(current_time=time_now)


@app.route('/get_time/future')
def get_time_future():
    time_future = datetime.datetime.now() + datetime.timedelta(hours=1)
    return "Точное время через час будет {current_time_after_hour}".format(
        current_time_after_hour=time_future)


@app.route('/get_random_word')
def get_random_word():
    return random.choice(words_war_and_peace)


@app.route('/counter')
def counter():
    global counter_visits
    counter_visits += 1
    return 'Запуск номер {num}'.format(num=counter_visits)


if __name__ == '__main__':
    app.run(debug=True)
