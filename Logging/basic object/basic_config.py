import logging


# info+
# http://grep.cs.msu.ru/python3.8_RU/digitology.tech/docs/python_3/howto/logging-cookbook.html

root_logger = logging.getLogger()  # получаем корневой логгер
logging.basicConfig()  # настраиваем логгер
# все логгеры будут принимать его настройки

# пользовательский логгер
module_logger = logging.getLogger('loger_name_1')  # получаем логгер модуля (первый или можно рут если один нужен)
module_logger.propagate = False  # отключаем логгер модуля от логгера корневого

submodule_logger = logging.getLogger('loger_name_1.submodule_logger')  # получаем логгер подмодуля
submodule_logger.setLevel('DEBUG')  # устанавливаем уровень логгирования логерра

custom_handler = logging.StreamHandler()  # получаем обработчик (выводит все в консоль)
# handler = logging.StreamHandler(sys.stdout)
module_logger.addHandler(custom_handler)  # добавляем обработчик в логгер модуля

formatter_1 = logging.Formatter(fmt="%(levelname)s | %(name)s | %(message)s")  # настраиваем формат логов
custom_handler.setFormatter(formatter_1)  # добавляем формат в обработчик

# создаем обработчик для записи в файл
    # filename,
    # mode = default = a,
    # delay = default = False, файл не будет сразу же открыт (откр при вызове emit())
    # errors = default = False -
file_handler = logging.FileHandler('applog.log', mode='a', encoding='utf-8', delay=False, errors=None)

# применяем настройки к обработчику
    # level
file_handler.setLevel(logging.DEBUG)
    # create formatter
formatter_2 = logging.Formatter(fmt="%(asctime)s | %(name)s | %(levelname)s | %(message)s")
    # set formatter
file_handler.setFormatter(formatter_2)
    # add handler to logger
module_logger.addHandler(file_handler)


# ротация лог-файлов
    # name - имя лог-файла
    # maxBytes - максимальный размер лог-файла
    # backupCount - максимальное количество лог-файлов
file_handler = logging.handlers.RotatingFileHandler('applog.log', maxBytes=100000, backupCount=10)



def main():
    try:
        1 / 0
    except ZeroDivisionError as error:\
        module_logger.error('ZeroDivisionError', exc_info=True)  # подробнее об ошибке
        # or   module_logger.exception("exception")

    submodule_logger.debug("Hi there!")


if __name__ == '__main__':
    main()
