'''Показывает число, стоящее под номером n в последовательности фибоначчи (Динамическое программирование)'''
def fibonacci(n):
    fib = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        # print(fib[i-2], end=' ') #- выдаст все числа Фибоначчи
    return fib[n - 1]

print(fibonacci(10))


'''Выводит ряд Фибоначчи'''
def fibon():
    '''генератор'''
    a, b = 0, 1
    while True:
        yield a    # выводит a (подобие return, но не заканчивает функцию)
        a, b = b, a + b

fib = fibon()    # объявление генератора
for i in range(0, 10):
    print(next(fib), end=' ')


'''Рекурсия'''
def f(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return f(n-1) + f(n-2)

print('\n', f(10))
