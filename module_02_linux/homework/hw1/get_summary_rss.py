def get_summary_rss(ps_output_file_path: str) -> str:
    """
    Принимает путь до файла с результатом выполнения команды ps aux.
    Возвращает суммарный объём потребляемой памяти в человекочитаемом формате.

    :param ps_output_file_path: str
    :return: total_rss: str
    """
    total_rss = 0
    units: dict = {0: ' B', 1: ' KB', 2: ' MB', 3: ' GB'}
    unit_key: int = 0

    with open(ps_output_file_path, 'r') as output_file:
        lines = output_file.readlines()[1:]
    for line in lines:
        columns = line.split()
        total_rss += float(columns[5])

    new_total = total_rss
    for unit in range(4):
        new_total /= 1024
        if new_total < 1:
            return str(round(total_rss, 1)) + units[unit_key]
        else:
            total_rss /= 1024
            unit_key += 1


if __name__ == '__main__':
    path: str = 'output_file.txt'
    summary_rss: str = get_summary_rss(path)
    print(f"Total rss: {summary_rss}")
