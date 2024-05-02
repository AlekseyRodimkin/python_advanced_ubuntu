import shlex
import subprocess
import re
from collections import Counter


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
    return (max(box.items(), key=lambda x: x[1])[0])



task5()