import logging

logger = logging.getLogger()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)  # обязательная конфигурация логгера
    # ей и направляются логи
    logger.info("Started divider server")
    app.config[""]
    WTF_CSRE_ENABLED = False
    app.run()

    # ERROR - произошла ошибка
    # WARNING - что - то плохое но работаем
    # INFO - произошло что - то важное но не ошибка
    # DEBUG - используется для отладки

# под логеры (дочерние)
module_loger = logging.getloger('first_loger_name') # допустим это первый
submodule_loger = logging.getloger('first_loger_name.second_logger_name') # допустим это первый
