# os - библиотека для работы с консолью
# random - библиотека для работы со случайными данными

import os
import random

# Зададим цвет шрифта консоли
os.system('COLOR B')

LEFT = 0  # LEFT - левая граница
RIGHT = 20  # RIGHT - правая граница
TYPE_COUNT = 10  # TYPE_COUNT - количество типов данных
MULTIPLIER = 100  # MULTIPLIER - множитель

LEFT0 = ord('A')  # LEFT0 - код символа A
RIGHT0 = ord('Z')  # RIGHT0 - код символа Z
LEFT1 = ord('a')  # LEFT1 - код символа a
RIGHT1 = ord('z')  # RIGHT1 - код символа z
LEFT2 = ord('А')  # LEFT2 - код символа А
RIGHT2 = ord('я')  # RIGHT2 - код символа я

# Типы данных:
# int, float, complex, str, bool
# list, tuple, dict, set, frozenset

RANGE = random.randint(LEFT, RIGHT)  # RANGE - диапозон
INTERVAL = random.randint(LEFT, RIGHT)  # INTERVAL - интервал


def rand():
    return random.random()
    # Выводим случайное значение от 0 до 1


def get_info():
    integer = random.randint(LEFT, RIGHT)
    # integer - целочисленное число
    double = random.random() * MULTIPLIER
    # double - вещественное число
    comp = MULTIPLIER * complex(rand(), rand())
    # comp - комплексное число
    boolean = bool(random.choice([0, 1]))
    # boolean - логическое значение
    string = ''.join([random.choice([
        random.choice([
            chr(random.randint(LEFT0, RIGHT0)),
            chr(random.randint(LEFT1, RIGHT1))
        ]),
        chr(random.randint(LEFT2, RIGHT2)),
        ' ',
        '.',
        ';',
        ',']
    )  # string - строка
        for _ in range(RANGE)])

    info = [integer, double, comp, string, boolean]
    # info - список различных данных

    return info


def get_data():
    info = get_info()
    # info - список обычных типов данных
    lis = list([random.choice(info) for _ in range(RANGE)])
    # lis - список различных данных
    tup = tuple([random.choice(info) for _ in range(RANGE)])
    # tup - кортеж различных данных
    last = len(info) - 2  # last - индекс последнего символа
    dictionary = dict(
        (random.choice(info[:last]), random.choice(info)) for _ in range(RANGE)
    )
    # dictionary - словарь различных данных
    sets = set([random.choice(info) for _ in range(RANGE)])
    # sets - множество различных данных
    frozensets = frozenset([random.choice(info) for _ in range(RANGE)])
    # frozensets - фиксированное множество различных данных

    data = []
    data.extend(info)
    # data - список различных типов и структур данных
    new = [lis, tup, dictionary, sets, frozensets]
    # new - список различных структур данных
    data.extend(new)
    return data


def generate_dict(dictionary, interval=2):
    INTERVAL = interval

    for i in range(INTERVAL):
        info = get_info()
        data = get_data()
        last = len(info) - 2
        # last - индекс последнего значения ключа
        new_info = info[:last]
        # new_info - сокращённый список
        key = random.choice(new_info)  # key - ключ
        value = random.choice(data)  # value - значение
        dictionary[key] = value  # заполняем словарь

    return dictionary


def generate_set(set_s, interval=2):
    INTERVAL = interval

    for i in range(INTERVAL):
        info = get_info()
        # info - список различных данных

        value = random.choice(info)

        while value in set_s:
            value = random.choice(info)

        # value - уникальное значение

        set_s.add(value)  # заполняем множество

    return set_s


# Выведем информацию о словаре и множестве
print('\nИНФОРМАЦИЯ О СЛОВАРЕ И МНОЖЕСТВЕ\n')

my_dict = {}
# Создадим словарь
my_dict = generate_dict(my_dict, INTERVAL)
# my_dict - словарь
print('Словарь:', my_dict, end='.\n')
my_dict = generate_dict(my_dict)  # Обновляем словарь
# Найдём существующий элемент словаря
END = len(my_dict) - 1
# END - конец словаря
index = random.randint(LEFT, END)
# index- случайный индекс
keyss = list(my_dict.keys())
# keyss - ключи словаря
exist = keyss[index]
# exist - существующий элемент словаря
print('Существующий элемент словаря:', exist, end='.\n')
# Найдём отсутствующий элемент словаря
none = keyss[index]
# none - отсутствующий элемент словаря

while none in my_dict.values():
    data = get_data()
    none = random.choice(data)

print('Отсутствующий элемент словаря:', none, end='.\n')
print('Обновлённый словарь:', my_dict, end='.\n')
# Удалим элемент из словаря
delete = keyss[index]
# delete  - ключ случайного элемента словаря
element = my_dict[delete]
del my_dict[delete]
print('Сокращённый словарь:', my_dict, end='.\n')
print('Удалённое значение словаря:', element, end='.\n\n')
del element

my_set = set()
# my_set - множество
# Создадим множество
my_set = generate_set(my_set, INTERVAL)
print('Множество:', my_set, end='.\n')
my_set = generate_set(my_set)  # Обновим множество
print('Обновлённое множество:', my_set, end='.\n')
# Удалим существующий элемент из множества
l = list(my_set)
# l - список множества
element = random.choice(l)
# element - элемент списка l
my_set.discard(element)
print('Сокращённое множество:', my_set, end='.\n\n')
del element

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли
