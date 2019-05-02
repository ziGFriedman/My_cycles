'''Решето Эратосфена - алгоритм определения простых чисел, до заданного'''
def sieve_erat(n):
    a = []
    for i in range(n + 1):     # список заполняется значениями от 0 до n
        a.append(i)
    a[1] = 0     # 1-ца не простое число
    i = 2
    while i <= n:     # # Если значение ячейки до этого не было обнулено, в этой ячейке содержится простое число.
        if a[i] != 0:     # первое кратное ему будет в два раза больше
            j = i + i
            while j <= n:     # это число составное, поэтому заменяем его нулем
                a[j] = 0     # переходим к следующему числу, которое кратно i (оно на i больше)
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    return a

print(sieve_erat(23))
