import logging


root_logger = logging.getLogger()  # получаем корневой логгер
logging.basicConfig()              # настраиваем логгер
# все логгеры будут принимать его настройки

module_logger = logging.getLogger('module_logger')  # получаем логгер модуля
module_logger.propagate = False                     # отключаем логгер модуля от логгера корневого

submodule_logger = logging.getLogger('module_logger.submodule_logger')  # получаем логгер подмодуля
submodule_logger.setLevel('DEBUG')  # устанавливаем уровень логгирования логерра

custom_handler = logging.StreamHandler()  # получаем обработчик (выводит все в консоль)
module_logger.addHandler(custom_handler)  # добавляем обработчик в логгер модуля

formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(message)s")  # настраиваем формат логов
custom_handler.setFormatter(formatter)  # добавляем формат в обработчик

# получаем обработчик (записывает в файл)
# filename, mode=default = a, code, delay = ???, errors = ???
file_handler = logging.FileHandler('applog.log', mode='a', encoding='utf-8', delay=False, errors=None)
file_handler.setFormatter(formatter)
module_logger.addHandler(file_handler)


def main():
    print("Root logger:")
    print(root_logger.handlers)

    print("Submodule logger:")
    print(submodule_logger.handlers)

    print("Module logger:")
    print(module_logger.handlers)

    submodule_logger.debug("Hi there!")


if __name__ == '__main__':
    main()

# кстати



# import logging
# import sys
#
# root = logging.getLogger()
# root.setLevel(logging.DEBUG)
#
# handler = logging.StreamHandler(sys.stdout)
# handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# root.addHandler(handler)