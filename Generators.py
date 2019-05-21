'''Пример использования генераторов с разными функциями'''
import random

def gen():
    while True:
        yield random.random()

def range_my(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def map_my(func, my_list):
    for i in my_list:
        yield func(i)

def enumerate_my(list_my):
    i = 0
    for l in list_my:
        yield (i, l)
        i += 1

def my_zip(l1, l2):
    l_len = len(l1)
    for i in range(l_len):
        yield (l1[i], l2[i])

rangemy = range_my(0, 10, 1)
print(list(rangemy))

print(list(range_my(0, 10, 1)))
