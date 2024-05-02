import sys
from os.path import getsize


def get_mean_size(ls_output: list[str]) -> float:
    """
    Возвращает средний размер файла в каталоге.
    :param: ls_output: list[str] - результат выполнения команды ls -l.
    :return: float, средний размер файла в каталоге.
    """
    total_size: float = 0.0
    file_count: int = 0
    for line in ls_output:
        file_count += 1
        total_size += getsize(line.split()[8])
    try:
        return round(total_size / file_count, 1)
    except ZeroDivisionError:
        return 0.0


if __name__ == '__main__':
    lines: list[str] = sys.stdin.readlines()[1:]
    mean_size: float = get_mean_size(lines)
    print(mean_size)
