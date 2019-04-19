'''Создание рандомного числа'''
import random

for i in range(10):
    print(random.randint(1, 100)) # от 1 до 100 включительно

from random import randint      # * - если нужно импортировать весь модуль
for i in range(10):
    print(randint(1, 10), end=' ' )
