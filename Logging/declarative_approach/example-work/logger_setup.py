import logging
import sys

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        }
    },
    "handlers": {
        "screen": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": sys.stdout
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",  # работает также как и обычный логер в файл
            # Но позволет записывать логи с разными интервалами (удалять старые логи)
            "when": "midnight",         # режим работы с файлом (полночь)
#             `'S': Second'
#             'M': Minute'
#             'H': Hour'
#             'D': Day'
#               'W0'-'W6': Weekday (0=Monday, 6=Sunday)
            "backupCount": 5,           # не более 5 файлов
            "formatter": "simple",      # форматер
            "level": "ERROR",           # уровень
            "filename": "skillbox.log"  # имя файла
        }
    },
    "loggers": {
        "skillbox": {
            "level": "DEBUG",
            "handlers": ["screen", "file"],
         }
    },
}
