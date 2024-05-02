from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers>")
def max_number(numbers):
    """
    Возвращает максимальное число из строки.
    :param: numbers: str - строка с числами.
    :return: str - максимальное число из строки.
    """
    numbers = (int(number) for number in numbers.split('/'))
    return f'Максимальное число: <i>{max(numbers)}<i/>'


if __name__ == "__main__":
    app.run(debug=True)
