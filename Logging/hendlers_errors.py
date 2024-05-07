from flask import flask
from flask_wtf import FlaskForm
from wtforms import INtegerField
from wtforms.validator import InputRequired

app = Flask(__name__)


logger = logging.getLogger("divider")

class DivideForm(FlaskForm):
    a = INtegerField(validators=[InputRequired])
    b = IntegerField(validators=[InputRequired()])

    logger.debug(f"Form is valid. a={a}, b={b}")


# если передать a=1&b=2 - вернет 500 (сервер столкнулся с неизвестной ошибкой)
# обраюботать ошибку можно через try/exept в каждом действии обрабатывая каждую ошибку,
# но это не правильно
"""Эндпоинт деления одного числа на другое"""
@app.route("/divide/", methods=["POST"])
def divide():
    form = DivideForm()

    if form.validate_on_submit():
        a, b = form.a.data, form.b.data
        return f"a / b = {a / b:.2f}"  # вернет 200

    logger.error(f"Form is not valid, error={form.errors}")
    return f"Bad request. Error = {form.errors}", 400  # вернет 400







# для обработки одной и той же ошибки в 2 эндпоинтах неудобно будет писать try
# ниже создан эндпоинт обработчик

# curl -X POST http://localhost:5000/formula1/ --data "x=1"
# >>> вернет то что нужно
# curl -X POST http://localhost:5000/formula1/ --data "x=0"
# >>> вернет "На ноль делить нельзя", 400 status code
@app.route("/formula1/", methods=["POST"])
def formula1():
    form = DivideForm()

    if form.validate_on_submit():
        x: float = form.x.data

        result = math.sin(x) / x

        return f"six({x}) / {x} = {result}"
    return f"Bad request. Error = {form.errors}", 400  # вернет 400


@app.route("/formula2/", methods=["POST"])
def formula2():
    form = DivideForm()

    if form.validate_on_submit():
        x, n = form.x.data, form.n.data

        result: float = 0.0

        for i in range(1, n + 1):
            result += 1.0 / (i * x)

        return f"Your result is {result}"
    return f"Bad request. Error = {form.errors}", 400  # вернет 400

@app.errorhandler()
# Обработчик ошибки деления на ноль, принимает класс ошибки
def handler_exeption(e: ZeroDivisionError):
    logger.exception("We are unable to divide by zero!", exc_info=e)
    return "We are unable to divide by zero!", 400






# ниже реализован поинт обработчик универсальный, возвращающий любую ошибку
"""Эндпоинт принимает отдел банка и id worker, ищет в файле чела и отдает его"""
@app.route("/bank_api/<branch>/<int:person_id>")
def bank_api(branch: str, person_id: int):
   branch_card_filename = f"bank_data/{branch}.csv" # название файла с сотрудниками конкретного отделения

   with open(branch_card_filename, "r") as file:
       csv_reader = csv.DictReader(file, delimiter-",")

       for record in csv_reader:
           if int(record["id"]) == person_id: # если сотрудник есть, вернет его имя
               return record["name"]

       else:
           return "Person not found", 404 # если нет чела такого то вернет 404

@app.errorhandler(InternalServerError)
# Обработчик любых исключений с логированием в файл, принимает класс ошибки и обрабатывает ее
def handle_exeption(e: InternalServerError):
    original: Optional[Exeption] = getattr(e, "original_exeption", None)


# первым будет обрабатываться FileNotFoundError, потому что он является дочерним OSError. ВВерх по дереву ошибок
    if isinstance(original, FileNotFoundError):
        with open("invalid_error.log", "a") as fo:
            fo.write(
                f"Tried to access a card. Exeption info: {original.strerror}\n"
            )

    # Обрабатывает исключениие при медленном сетевом диске
    elif isinstance (original, OSError):
        with open("invalid_error.log", "a") as fo:
            fo.write(f"Unable to access a card. Exeption info: {original.strerror}\n")

    return "Internal server error", 500


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)  # обязательная конфигурация логгера
    logger.info("Started divider server")
    app.config[""]
    WTF_CSRE_ENABLED = False
    app.run()
