"""конфигурация логгера на декларативном подходе"""
import sys

dict_config = {
    # стандартная конфигурация
    "version": 1,  # версия конфигурации (единственная)
    "disable_existing_loggers": False,  # отключает логгирование всех существующих логгеров вне этого файла
    # default = True
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(message)s"
        }
    },

    "handlers": {
        "console": {  # имя хендлера
            "class": "logging.StreamHandler",  # ДЛЯ ВЫВОДА В КОНСОЛЬ
            "level": "DEBUG",  # уровень логгирования для хендлера
            "formatter": "base",  # имя форматтера для хендлера
            "stream": sys.stdout  # поток вывода для хендлера
        },
        "file": {  # имя хендлера
            "class": "logging.FileHandler",  # ДЛЯ ВЫВОДА В ФАЙЛ
            "level": "DEBUG",  # уровень логгирования для хендлера
            "formatter": "base",  # имя форматтера для хендлера
            "filename": "logfile.log",  # имя файла для писания логов
            "mode": "a"  # режим работы с файлом
        }
    },
    "loggers": {
        "module_logger": {  # должен быть родительским для всех других в приложении
            # указывается в logger.getLogger('тута')

            "level": "DEBUG",  # level
            "handlers": ["file", "console"],  # имена хендлеров
            # "propagate": False,               # не нужно для высшего логгера
        }
    },

    # "filters": {},
    # "root": {} # == "": {}
}
