'''Факториал числа n'''
def factorial(n):
    '''Нахождение факториала рекурсией'''
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(4))


def factor(n):
    '''Нахождение факториала циклом for'''
    factor = 1
    if n == 0:
        return 1
    for i in range(2, n + 1):
        factor *= i
    return factor

print(factor(4))


def fact(n):
    '''Нахождение факториала циклом while'''
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact

print(fact(4))
