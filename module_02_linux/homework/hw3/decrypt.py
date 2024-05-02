import sys


def decrypt(encryption: str) -> str:
    """
    Возвращает расшифрованную строку.
    :param: encryption: str - строка, которую нужно расшифровать.
    :return: str - расшифрованная строка.
    """
    result: list = []
    for symbol in encryption:
        result.append(symbol)

        if len(result) > 2 and (result[-1], result[-2]) == ('.', '.'):
            result.pop()
            result.pop()
            if result:
                result.pop()

    return ''.join(num for num in result if num != '.')


if __name__ == '__main__':
    data: str = sys.stdin.read()
    decryption: str = decrypt(data)
    print(decryption)
