import getpass
import hashlib
import logging

"""Программа проверяет пароль пользователя и возвращает 0 или 1"""

# его имя будет отображаться в логах
logger = logging.getLogger("password_checker")  # умеет писать сообщения, в том числе ошибки


def check_password(password: str):
    digits = '1234567890'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '!@#$%^&*()-+'
    acceptable = digits + upper_letters + lower_letters + symbols

    passwd = set(password)
    if any(char not in acceptable for char in passwd):
        logger.warning('Ошибка. Запрещенный спецсимвол')
        return False
    elif len(passwd) < 8:
        logger.warning('Короткий пароль')
        return False
    else:
        return True


def input_and_check_password():
    logger.debug("Начало -> input_and_check_password")
    password: str = getpass.getpass()
    if not check_password(password):
        exit(1)

    if not password:
        logger.warning("Вы ввели пустой пароль")  # выводится при любом по счету пустом пароле
        return False

    try:
        hasher = hashlib.md5()
        logger.debug(f"Создание объекта hasher {hasher!r}")

        hasher.update(password.encode("latin-1"))
        logger.debug(f"hasher.update()")

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            logger.debug(f"if hasher.hexdigest()...")
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ", exc_info=ex)

    return False


# tests
for test in ("qwety", "Qwert_Y", "Q123wer123tY", "A^B@C*D", "@PowerRangers123@"):
    print("Password:", test)
    check_password(test)
    print()


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)  # выводит все сообщения уровня дебаг и выше
    logger.info("Вы пытаетесь войти в Программу")
    count_number: int = int(input("Сколько попыток ввода пароля вам необходимо: "))
    if not 2 <= count_number <= 9:
        logger.error("Кол-во попыток должно быть от 2 до 9.")
        exit(1)
    logger.info(f"У вас есть {count_number} попыток")

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    # выводит ошибку в конце
    logger.error("Пользователь 3 раза ввел не правильный пароль")
    exit(1)
