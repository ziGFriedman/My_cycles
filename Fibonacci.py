'''Показывает число, стоящее под номером n в последовательности фибоначчи (Динамическое программирование)'''
def fibonachchi(n):
    fib = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        #print(fib[i-2], end=', ') #- выдаст все числа Фибоначчи
    return fib[n]

print(fibonachchi(10))


'''Выводит ряд Фибоначчи'''
def fib():
    '''генератор'''
    a, b = 0, 1
    while True:
        yield a     # выводит a (подобие return)
        a, b = b, a + b

x = fib()   # объявление генератора
y = 11
for i in range(0, y):
    print(next(x), end = ' ')
