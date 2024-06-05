# os - library for working with the console
# random - library for working with random data

import os
import random

# Setting the font color of the console
os.system('COLOR B')

LEFT = 0  # LEFT - the left border
RIGHT = 20  # RIGHT - the right border
TYPE_COUNT = 10  # TYPE_COUNT - number of data types
MULTIPLIER = 100  # MULTIPLIER - multiplier

LEFT0 = ord('A')  # LEFT0 - character code A
RIGHT0 = ord('Z')  # RIGHT0 - The Z character code
LEFT1 = ord('a')  # LEFT1 - character code a
RIGHT1 = ord('z')  # RIGHT1 - The z character code
LEFT2 = ord('А')  # LEFT2 - The code of the symbol A
RIGHT2 = ord('я')  # RIGHT2 - The code of the symbol I

# Types of data:
# int, float, complex, str, bool
# list, tuple, dict, set, frozenset

RANGE = random.randint(LEFT, RIGHT)  # RANGE - range
INTERVAL = random.randint(LEFT, RIGHT)  # INTERVAL - interval


def rand():
    return random.random()
    # Output a random value from 0 to 1


def get_info():
    integer = random.randint(LEFT, RIGHT)
    # integer - an integer number
    double = random.random() * MULTIPLIER
    # double - a real number
    comp = MULTIPLIER * complex(rand(), rand())
    # comp - a complex number
    boolean = bool(random.choice([0, 1]))
    # boolean - logical value
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
    )  # string - line
        for _ in range(RANGE)])

    info = [integer, double, comp, string, boolean]
    # info - list of various data

    return info


def get_data():
    info = get_info()
    # info - list of common data types
    lis = list([random.choice(info) for _ in range(RANGE)])
    # lis - list of various data
    tup = tuple([random.choice(info) for _ in range(RANGE)])
    # tup - a tuple of different data
    last = len(info) - 2  # last - index of the last character
    dictionary = dict(
        (random.choice(info[:last]), random.choice(info)) for _ in range(RANGE)
    )
    # dictionary - dictionary of various data
    sets = set([random.choice(info) for _ in range(RANGE)])
    # sets - lots of different data
    frozensets = frozenset([random.choice(info) for _ in range(RANGE)])
    # frozensets - a fixed set of different data

    data = []
    data.extend(info)
    # data - a list of different data types and structures
    new = [lis, tup, dictionary, sets, frozensets]
    # new - list of different data structures
    data.extend(new)
    return data


def generate_dict(dictionary, interval=2):
    INTERVAL = interval

    for i in range(INTERVAL):
        info = get_info()
        data = get_data()
        last = len(info) - 2
        # last - index of the last key value
        new_info = info[:last]
        # new_info - the abbreviated list
        key = random.choice(new_info)  # key - key
        value = random.choice(data)  # value - meaning
        dictionary[key] = value  # filling in the dictionary

    return dictionary


def generate_set(set_s, interval=2):
    INTERVAL = interval

    for i in range(INTERVAL):
        info = get_info()
        # info - list of various data

        value = random.choice(info)

        while value in set_s:
            value = random.choice(info)

        # value - unique value

        set_s.add(value)  # filling in the set

    return set_s


# Let's output information about the dictionary and the set
print('\nINFORMATION ABOUT THE DICTIONARY AND THE SET\n')

my_dict = {}
# Let's create a dictionary
my_dict = generate_dict(my_dict, INTERVAL)
# my_dict - dictionary
print('Dictionary:', my_dict, end='.\n')
my_dict = generate_dict(my_dict)  # Updating the dictionary
# Find an existing dictionary element
END = len(my_dict) - 1
# END - end of the dictionary
index = random.randint(LEFT, END)
# index - random index
keyss = list(my_dict.keys())
# keyss - dictionary keys
exist = keyss[index]
# exist - an existing dictionary element
print('An existing dictionary element:', exist, end='.\n')
# Find the missing dictionary element
none = keyss[index]
# none - missing dictionary element

while none in my_dict.values():
    data = get_data()
    none = random.choice(data)

print('Missing dictionary element:', none, end='.\n')
print('Updated dictionary:', my_dict, end='.\n')
# Removing an element from the dictionary
delete = keyss[index]
# delete  - the key of a random dictionary element
element = my_dict[delete]
del my_dict[delete]
print('Abbreviated Dictionary:', my_dict, end='.\n')
print('Deleted Dictionary value:', element, end='.\n\n')
del element

my_set = set()
# my_set - plenty
# Let's create a set
my_set = generate_set(my_set, INTERVAL)
print('Plenty:', my_set, end='.\n')
my_set = generate_set(my_set)  # Let's update the set
print('Updated set:', my_set, end='.\n')
# Remove an existing element from the set
l = list(my_set)
# l - list of the set
element = random.choice(l)
# element - list item l
my_set.discard(element)
print('An abbreviated set:', my_set, end='.\n\n')
del element

try:
    os.system('PAUSE')  # Stopping the program
    os.system('CLS')  # Clearing the console screen
except:
    os.system('CLS')  # Clearing the console screen
