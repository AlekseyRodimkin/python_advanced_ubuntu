"""
Консольная утилита lsof (List Open Files) выводит информацию о том, какие файлы используют какие-либо процессы.
Эта команда может рассказать много интересного, так как в Unix-подобных системах всё является файлом.

Но нам пока нужна лишь одна из её возможностей.
Запуск lsof -i :port выдаст список процессов, занимающих введённый порт.
Например, lsof -i :5000.

Как мы с вами выяснили, наш сервер отказывается запускаться, если кто-то занял его порт. Напишите функцию,
которая на вход принимает порт и запускает по нему сервер. Если порт будет занят,
она должна найти процесс по этому порту, завершить его и попытаться запустить сервер ещё раз.
"""
from typing import List
import shlex
import subprocess
from flask import Flask
import os

app = Flask(__name__)


def get_pids(port: int) -> List[int]:
    """
    Возвращает список PID процессов, занимающих переданный порт
    @param port: порт
    @return: список PID процессов, занимающих порт
    """
    if not isinstance(port, int):
        raise ValueError

    command = shlex.split('lsof -i :5000')

    # Get result command
    with subprocess.Popen(command, stdout=subprocess.PIPE, text=True) as process:
        result = process.stdout.read().split()

    # Get int`s from result
    result = [int(word) for word in result if word.isdigit()]

    # Pop all not pids (DEVICE)
    [result.pop(result.index(obj)) for obj in result if result.index(obj) > 0]
    print('PIDS uses port - ', result)
    return result


def free_port(port: int) -> None:
    """
    Завершает процессы, занимающие переданный порт
    @param port: порт
    """
    pids: List[int] = get_pids(port)
    for PID in pids:
        print("Kill {} pid".format(PID))
        os.kill(PID, 9)


def run(port: int) -> None:
    """
    Запускает flask-приложение по переданному порту.
    Если порт занят каким-либо процессом, завершает его.
    @param port: порт
    """
    free_port(port)
    print('Running new app on {}...\n'.format(port))
    app.run(port=port)


if __name__ == '__main__':
    run(5000)
