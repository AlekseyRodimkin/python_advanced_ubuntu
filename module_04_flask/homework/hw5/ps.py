"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""

from flask import Flask, request
from typing import List
import subprocess
from shlex import quote


app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    args: List[str] = request.args.getlist('arg')
    command = quote(''.join(args))
    output = subprocess.run(['ps', command], capture_output=True, text=True)
    return f"<pre>{output.stdout}</pre>"


if __name__ == "__main__":
    app.run(debug=True)
