import logging

"""Программа проверяет пароль пользователя и возвращает 0 или 1"""

# creating logger
logger = logging.getLogger("password_checker")  # имя логера в скобках

# errors
try:
    pass
except Exception as ex:
    logger.exception("Вы ввели некорректный символ", exc_info=ex)
    raise ValueError("Вы ввели некорректный символ")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)  # обязательная конфигурация логгера

# под логеры (дочерние)
module_loger = logging.getloger('first_loger_name') # допустим это первый
submodule_loger = logging.getloger('first_loger_name.second_logger_name') # допустим это первый