from flask import Flask
from datetime import datetime


app = Flask(__name__)


@app.route('/hello-world/<username>')
def hello_world(username: str):
    """
    Приветствие пользователя.
    :param: username: str - имя пользователя.
    :return: str - приветствие пользователя.
    """
    weekday: int = datetime.today().weekday()
    days: tuple = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')
    if weekday == 0 or weekday == 1 or weekday == 3 or weekday == 6:
        return f'Привет, {username}. Хорошего {days[weekday]}!'
    else:
        return f'Привет, {username}. Хорошей {days[weekday]}!'


if __name__ == '__main__':
    app.run(debug=True)
