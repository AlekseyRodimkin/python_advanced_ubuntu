"""
Заменим сообщение "The requested URL was not found on the server" на что-то более информативное.
Например, выведем список всех доступных страниц с возможностью перехода по ним.

Создайте Flask Error Handler, который при отсутствии запрашиваемой страницы будет выводить
список всех доступных страниц на сайте с возможностью перехода на них.
"""
from flask import Flask, url_for


app = Flask(__name__)


def has_no_empty_params(rule):
    """Функция используется для обработки 404"""
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route('/dogs')
def dogs():
    return 'Страница с пёсиками'


@app.route('/cats')
def cats():
    return 'Страница с котиками'


@app.route('/cats/<int:cat_id>')
def cat_page(cat_id: int):
    return f'Страница с котиком {cat_id}'


@app.route('/index')
def index():
    return 'Главная страница'


@app.errorhandler(404)
def site_map(error):
    """
    Обработчик для 404. Собирает список всех доступных страниц.
    """
    links = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))

    ok_return_page = 'Page is not found.(((\nAvailable pages:\n'
    for box in links:
        ok_return_page += f"{box[1]}\nhttp://localhost:5000{box[0]}\n"
    return ok_return_page


if __name__ == '__main__':
    app.run(debug=True)
