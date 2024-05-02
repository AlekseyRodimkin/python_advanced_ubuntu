"""
У нас есть кнопочный телефон (например, знаменитая Nokia 3310), и мы хотим,
чтобы пользователь мог проще отправлять СМС. Реализуем своего собственного клавиатурного помощника.

Каждой цифре телефона соответствует набор букв:
* 2 — a, b, c;
* 3 — d, e, f;
* 4 — g, h, i;
* 5 — j, k, l;
* 6 — m, n, o;
* 7 — p, q, r, s;
* 8 — t, u, v;
* 9 — w, x, y, z.

Пользователь нажимает на клавиши, например 22736368, после чего на экране печатается basement.

Напишите функцию my_t9, которая принимает на вход строку, состоящую из цифр 2–9,
и возвращает список слов английского языка, которые можно получить из этой последовательности цифр.
"""
import re
from typing import List, Dict


keyboard: Dict = {
    1: "\\.\\!\\?", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs",
    8: "tuv", 9: "wxyz"
}


def my_t9(input_numbers: str) -> List[str]:
    with open("/usr/share/dict/words", 'r') as file:
        words_ = list(filter(lambda x: x, file))                                         # получаем список слов
    letters = map(lambda c: "[" + keyboard[int(c)] + "]", input_numbers)     # получаем список возможно выбранных букв
    regex = "^" + "".join(letters) + "$"                                                 # создаем регулярное выражение
    possible_words = [w.rstrip() for w in words_ if re.search(regex, w, re.IGNORECASE)]  # выполняем поиск
    return possible_words


if __name__ == '__main__':
    # numbers: str = input()
    numbers = "22736368"
    words: List[str] = my_t9(numbers)
    print(*words, sep='\n')
