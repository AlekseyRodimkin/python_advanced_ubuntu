import logging


class CustomFileHandler(logging.Handler):  # наследуемся от обработчика

    def __init__(self, file_name, mode='a'):
        """конструктор"""
        super().__init__()  # вызываем конструктор родительского класса
        self.file_name = file_name
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:  # принимает объект лог записи
        """Метод обработки и отправки сообщений куда-нибудь"""
        message = self.format(record) # форматируем сообщение согласно форматтеру
        with open(self.file_name, mode=self.mode) as f:  # записываем строку в файл
            f.write(message + '\n')


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
        },
        "file": {
            "()": CustomFileHandler,  # так даем понять что у нас кастомный класс и его нужно инициализировать
            "level": "DEBUG",
            "formatter": "base",
            'file_name': 'customlogfile.log',
            'mode': 'a'
        }
    },
    "loggers": {
        # указывается в logger.getLogger('тута')
        "module_logger": {
            "level": "DEBUG",
            "handlers": ["file", "console"],
            # "propagate": False,
        }
    },

    # "filters": {},
    # "root": {} # == "": {}
}
