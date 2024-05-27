import string
import requests
from utils import string_to_operator
import logging.config
import logging_tree

from logging_config import dict_config

logging.config.dictConfig(dict_config)


class ASCIIFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> int:
        return not any(symb not in string.printable for symb in record.msg)


class HttpHandler(logging.Handler):
    def __init__(self, host, port, url, method='POST', headers=None, secure=False):
        super().__init__()
        self.host = host
        self.port = port
        self.url = url
        self.method = method
        self.headers = headers
        self.secure = secure

    def emit(self, record):
        log_entry = self.format(record)
        address = f"http://{self.host}:{self.port}{self.url}"
        try:
            if self.secure:
                response = requests.post(address, data=log_entry, headers=self.headers, verify=True)
            else:
                response = requests.post(address, data=log_entry, headers=self.headers, verify=False)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при отправке записи журнала: {e}")


http_handler = HttpHandler(host="127.0.0.1", port="5000", url="/log", method="POST")
app_logger = logging.getLogger("app")
app_logger.addHandler(http_handler)
app_logger.setLevel("DEBUG")
app_logger.addFilter(ASCIIFilter())


def calc(args):
    app_logger.debug("Строка на кириллице для проверки фильтра (calc_debug.log)")
    app_logger.debug(f"Arguments: {args}")
    # print("Arguments: ", args)

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        # print("Error while converting number 1")
        # print(e)
        app_logger.exception(e)
        app_logger.error("Error while converting number 1")

    try:
        num_2 = float(num_2)
    except ValueError as e:
        # print("Error while converting number 1")
        # print(e)
        app_logger.exception(e)
        app_logger.debug("Error while converting number 1")

    operator_func = string_to_operator(operator)

    result = operator_func(num_1, num_2)

    # print("Result: ", result)
    # print(f"{num_1} {operator} {num_2} = {result}")
    app_logger.debug(f"Result:  {result}")
    app_logger.debug(f"{num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    with open("logging_tree.txt", "w") as file:
        file.write(logging_tree.format.build_description())

    # calc(sys.argv[1:])
    calc('2+3')
