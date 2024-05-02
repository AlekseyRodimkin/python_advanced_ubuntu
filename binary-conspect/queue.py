# Двусторонняя очередь в Python
# Класс collections.deque() это обобщение стеков и очередей и представляет собой двустороннюю очередь.
# Двусторонняя очередь deque() поддерживает поточно-ориентированные,
# эффективные по памяти операции добавления и извлечения элементов последовательности
# с любой стороны с примерно одинаковой производительностью O(1) в любом направлении.
#
# Списки поддерживают аналогичные операции, но они оптимизирован только для быстрых операций с
# последовательностями фиксированной длины и требуют затрат O(n)
# на перемещение памяти для операций pop(0) и insert(0, v), которые изменяют как размер,
# так и положение базового представления данных.

# Синтаксис:
import collections

dq = collections.deque([iterable[, maxlen]])
# Параметры:
# iterable - итерируемая последовательность,
# maxlen - int, максимальное кол-во хранимых записей.
# Возвращаемое значение:
# новый объект Deque.

# Описание:
# Класс deque() модуля collections возвращает новый объект deque(),
# инициализированный слева направо данными из итерируемой последовательности iterable.

# При создании объекта очереди класс использует метод dq.append() для добавления элементов из итерации iterable.
# Если итерация не указана, новая очередь deque() будет пуста.

>>> from collections import deque
>>> dq = deque('ghi')
>>> dq
# deque(['g', 'h', 'i'])
# Если аргумент maxlen не указан или равен None, количество хранимых записей в объекте deque()
# может увеличиваться до произвольной длины.
# В противном случае, объект deque() ограничивает количество хранимых элементов в своем контейнере
# максимальной длиной maxlen.
#
# При добавлении новых элементов, когда заполнение очереди deque() становится больше значения maxlen,
# избыточное количество элементов удаляется/сбрасывается с противоположного конца.
# Заполнение очереди на определенную длину обеспечивают функциональность, аналогичную команде bash tail в Unix.
# Такое поведение полезно для отслеживания транзакций и других пулов данных,
# где интерес представляют только самые последние изменения или действия.


Объект Deque, атрибуты и методы:

Deque.append(x):
Метод Deque.append() добавляет x к правой стороне (в конец) контейнера deque().

>>> dq.append('j')
>>> dq
# deque(['g', 'h', 'i', 'j'])

Deque.appendleft(x):
Метод Deque.appendleft() добавляет x к левой стороне (в начало) контейнера deque().

>>> dq.appendleft('f')
>>> dq
# deque(['f', 'g', 'h', 'i', 'j'])

Deque.copy():
Метод Deque.copy() создает мелкую копию контейнера deque().

>>> cp_dq = dq.copy()
>>> cp_dq
# deque(['f', 'g', 'h', 'i', 'j'])

Deque.clear():
Метод Deque.clear() удаляет все элементы из контейнера deque(), оставляя его длиной 0.

>>> cp_dq.clear()
>>> cp_dq
# deque([])
>>> dq
# deque(['f', 'g', 'h', 'i', 'j'])

Deque.count(x):
Метод Deque.count() подсчитывает количество элементов контейнера deque(), равное значению x.

>>> dq.append('g')
>>> dq.count('g')
# 2
>>> dq
# deque(['f', 'g', 'h', 'i', 'j', 'g'])

Deque.extend(iterable):
Метод Deque.extend() расширяет правую сторону (с конца) контейнера deque(), добавляя элементы из итерируемого аргумента iterable.

>>> dq.extend('jkl')
>>> dq
# deque(['f', 'g', 'h', 'i', 'j', 'g', 'j', 'k', 'l'])

Deque.extendleft(iterable):
Метод Deque.extendleft() расширяет левую сторону (с начала) контейнера deque(), добавляя элементы из итерируемого аргумента iterable.

Обратите внимание, что ряд последовательных добавлений в начало контейнера приводит к изменению порядка элементов в аргументе iterable.

>>> dq.extendleft('ab')
>>> dq
# deque(['b', 'a', 'f', 'g', 'h', 'i', 'j', 'g', 'j', 'k', 'l'])

Deque.index(x[, start[, stop]]):
Метод Deque.index() вернет позицию (индекс) первого совпадения значения аргумента x в контейнере deque(), расположенного после необязательного аргумента start и до необязательного аргумента stop.

Вызывает исключение ValueError, если значения аргумента x не найдено.

>>> dq.index('g', 2)
# 3
>>> dq.index('b', 2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: 'b' is not in deque

Deque.insert(i, x):
Метод Deque.insert() вставляет значение аргумента x в позицию i контейнера deque().

Если вставка значение аргумента x приведет к тому, что ограниченный контейнер deque() выйдет за пределы maxlen, будет вызвано исключение IndexError.

>>> dq.insert(2, 'c')
>>> dq
# deque(['b', 'a', 'c', 'f', 'g', 'h', 'i', 'j', 'g', 'j', 'k', 'l'])

Deque.pop():
Метод Deque.pop() удаляет и возвращает элемент с правой стороны (с конца) контейнера deque(). Если элементы отсутствуют, возникает ошибка IndexError.

>>> dq.pop()
# 'i'

Deque.popleft():
Метод Deque.popleft() удаляет и возвращает элемент с левой стороны (с начала) контейнера deque(). Если элементы отсутствуют, возникает ошибка IndexError.

>>> dq.popleft()
# 'b'

Deque.remove(value):
Метод Deque.remove() удаляет первое вхождение значения value в контейнер deque(). Если значение value не найдено, возникает ошибка IndexError.

>>> dq.remove('g')
>>> dq
# deque(['a', 'c', 'f', 'h', 'i', 'j', 'g', 'j', 'k'])

Deque.reverse():
Метод Deque.reverse() разворачивает элементы контейнера deque() на месте и возвращает None.

>>> dq.reverse()
>>> dq
# deque(['k', 'j', 'g', 'j', 'i', 'h', 'f', 'c', 'a'])

Deque.rotate(n=1):
Метод Deque.rotate() разворачивает контейнер deque() на n шагов вправо. Если аргумент n имеет отрицательное значение, то разворачивает контейнер налево.

Когда контейнер не пуст, вращение на один шаг вправо эквивалентно dq.appendleft(d.pop()), а вращение на один шаг влево эквивалентно dq.append(d.popleft()).

>>> dq.rotate(2)
>>> dq
# deque(['c', 'a', 'k', 'j', 'g', 'j', 'i', 'h', 'f'])
>>> dq.rotate(-4)
>>> dq
# deque(['g', 'j', 'i', 'h', 'f', 'c', 'a', 'k', 'j'])

Deque.maxlen:
Свойство Deque.maxlen() возвращает максимальный размер maxlen контейнера deque(), если параметр maxlen не задан, то возвращает None.


Примеры использования класса deque():
Имитация поведения, аналогичного команде bash tail в Unix:

from collections import deque

def tail(filename, n=10):
    "Вернуть последние 'n' строк файла"
    with open(filename) as f:
        return deque(f, n)
Еще один подход в использовании двусторонней очереди - это сохранять недавно добавленные элементы в контейнере, добавляя их справа, а устаревшие значения сбрасывается слева. Например функция "Скользящая средняя", которая используется для сглаживания краткосрочных колебаний временных рядов

from collections import deque

def moving_average(iterable, n=3):
    "moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0"
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n
Циклический планировщик с очередями задач может быть реализован при помощи итераторов, хранящимися в очереди deque(). Значения выводятся из активного итератора в нулевой позиции. Если активный итератор исчерпан, его можно удалить с помощью dg.popleft(). В противном случае его можно циклически вернуть в конец при помощи метода dq.rotate():

def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            # Remove an exhausted iterator.
            iterators.popleft()