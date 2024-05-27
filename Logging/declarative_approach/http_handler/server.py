import json
from flask import Flask, request


app = Flask(__name__)


@app.route('/log', methods=['POST'])
def log():
    """
    Записываем полученные логи которые пришли к нам на сервер
    return: текстовое сообщение об успешной записи, статус код успешной работы

    """
    log_string = request.get_data(as_text=True)
    with open('http_logs.txt', 'a', encoding='utf-8') as file:
        file.write(f"{log_string}\n")
    return 'Successful logging', 200


@app.route('/logs', methods=['GET'])
def logs():
    """
    Рендерим список полученных логов
    return: список логов обернутый в тег HTML <pre></pre>
    """
    with open('http_logs.txt', 'r', encoding='utf-8') as file:
        html_logs = file.readlines()
    return f'<pre>{html_logs}</pre>'


if __name__ == '__main__':
    app.run()
