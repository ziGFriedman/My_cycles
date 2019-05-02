'''Проверка простоты числа перебором делителей'''
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True

print(is_prime(103))
