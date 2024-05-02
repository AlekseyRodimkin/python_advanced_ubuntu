from typing import Dict


def average_time():
    data: Dict = {'sum_time': 0, 'count': 0}
    with open('measure_me.log', 'r') as file:
        lines, start, end = file.readlines(), 0, 0

        for i in range(len(lines)):
            if i % 2 != 0:
                start = int(lines[i][:2]) * 60 + float(lines[i][3:9])
            else:
                end = int(lines[i][:2]) * 60 + float(lines[i][3:9])
                data['sum_time'] += (end - start)
                data['count'] += 1

    return f'Average time:      {round(data["sum_time"] / data["count"], 3)} sec'


print(average_time())
