import logging

logging.basicConfig(filename='app.log', filemode='a')
module_logger = logging.getLogger('module_logger')
module_logger.setLevel(logging.DEBUG)


class CustomFileHandler(logging.Handler):  # наследуемся от обработчика

    def __init__(self, file_name, mode='a'):
        """конструктор"""
        super().__init__()  # вызываем конструктор родительского класса
        self.file_name = file_name
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:  # принимает объект лог записи
        """Метод обработки и отправки сообщений куда-нибудь"""
        message = self.format(record)  # форматируем сообщение согласно форматтеру
        with open(self.file_name, mode=self.mode) as f:  # записываем строку в файл
            f.write(message + '\n')


module_logger.addHandler(CustomFileHandler('logfile.log', mode='a'))
