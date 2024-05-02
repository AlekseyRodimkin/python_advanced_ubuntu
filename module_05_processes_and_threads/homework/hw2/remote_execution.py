"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""
import shlex
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange
import subprocess
from subprocess import Popen, PIPE, TimeoutExpired

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField()
    timeout = IntegerField(validators=[InputRequired('Empty timeout'), NumberRange(min=1, max=30)])


def run_python_code_in_subproccess(code: str, timeout: int):
    code = shlex.split(code)
    try:
        proc = subprocess.run(code, stdout=PIPE, stderr=PIPE, timeout=timeout, text=True)
        return proc.stdout
    except TimeoutExpired as er:
        return '{}'.format(er)


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()

    if form.validate_on_submit():
        code, timeout = form.code.data, form.timeout.data
        return run_python_code_in_subproccess(code, timeout)

    return f"Invalid input, {form.errors}", 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
