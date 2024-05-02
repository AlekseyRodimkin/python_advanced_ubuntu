"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""
import re
from typing import Dict, Tuple
import subprocess
import shlex


def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """
    levels: Tuple = ('DEBUG', 'INFO', 'WARNING', 'CRITICAL', 'ERROR')
    stat: Dict[str, int] = {}
    for level in levels:
        command = shlex.split(f'grep -c \'\"level\": \"{level}\"\' skillbox_json_messages.log')
        with subprocess.Popen(command, stdout=subprocess.PIPE, text=True) as process:
            result = process.stdout.read().strip()
            stat[level] = int(result)
    return stat


def task2() -> int:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    hard_hour: Tuple = (0, 0)
    hours: Tuple = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
                    '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
    for hour in hours:
        command = shlex.split(f'grep -c \'\"time\": \"{hour}\' skillbox_json_messages.log')
        with subprocess.Popen(command, stdout=subprocess.PIPE, text=True) as process:
            result = process.stdout.read().strip()
            if int(result) > hard_hour[1]:
                hard_hour = (int(hour), int(result))
    return hard_hour[0]


def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    command = shlex.split('grep \'"time": "05\' skillbox_json_messages.log')
    with subprocess.Popen(command, stdout=subprocess.PIPE, text=True) as process:
        result = process.stdout.read()
    five_clock_logs = re.findall(r'.*05:[0-2][0-9]:[0-9][0-9]", "level": "CRITICAL.*', result)
    good_logs = [line for line in five_clock_logs if int(line[13]) <= 1 or line[13] == '2' and line[14] == '0']
    return len(good_logs)


def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """
    command = shlex.split('grep -c \'dog\' skillbox_json_messages.log')
    with subprocess.Popen(command, stdout=subprocess.PIPE, text=True) as process:
        result = process.stdout.read()
        return int(result)


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    command = shlex.split('grep "WARNING" skillbox_json_messages.log')
    box = {}
    with subprocess.Popen(command, stdout=subprocess.PIPE, text=True) as process:
        result = process.stdout.read()
    messages_warn = re.findall(r'"message".*', result)
    for message in messages_warn:
        for word in message[12:-2].split(' '):
            box[word] = box.get(word, 0) + 1
    return max(box.items(), key=lambda x: x[1])[0]


if __name__ == '__main__':
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')
