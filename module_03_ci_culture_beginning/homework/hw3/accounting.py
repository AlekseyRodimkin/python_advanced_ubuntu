from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    """
    Добавляет новый элемент в хранилище.
    год {'average': [ср, сумм, кол], 'мес': [ср, сумм, кол]}
    :param: date: str - дата.
    :param: number: int - число.
    :return: str - дата.
    """
    storage.setdefault(date[:4], {})
    storage[date[:4]].setdefault('sum', 0)
    storage[date[:4]].setdefault(date[4:6], 0)
    storage[date[:4]]['sum'] += float(number)
    storage[date[:4]][date[4:6]] += float(number)
    return f'Дата: {date[:4]}{date[4:6]}{date[6:8]}, добавлена сумма {number}'


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    try:
        return f"{storage[str(year)]['sum']}"
    except KeyError:
        return f'Суммарные затраты за {year} год не существует'


@app.route("/calculate/<int:year>/<string:month>")
def calculate_month(year: int, month: int):
    try:
        return f'{storage[str(year)][str(month)]}'
    except KeyError:
        return f'Суммарные затраты за {month}.{year} не существует'


if __name__ == "__main__":
    app.run(debug=True)
