import logging.config
from custom_file_handler import dict_config
# from logging_utilities.log_record import LogRecordIgnoreMissing  # для игнорирования отсутствующих полей
# from logging_utilities.log_record import set_log_record_ignore_missing_factory  # default отсутствующих полей
from custom_file_handler import dict_config  # import our config

# logging.setLogRecordFactory(LogRecordIgnoreMissing)  # для игнорирования отсутствующих полей
# set_log_record_ignore_missing_factory('default')  # default отсутствующих полей

logging.config.dictConfig(dict_config)  # применение настроек из конфига

# создание нужного нам модуля
submodule_logger = logging.getLogger("module_logger.submodule_logger")
submodule_logger.setLevel("DEBUG")


def main():
    submodule_logger.debug("Hi there!")
    submodule_logger.debug('msg', extra={"extra_comment": 'Comment here'})
    print(vars(submodule_logger))


if __name__ == '__main__':
    main()
