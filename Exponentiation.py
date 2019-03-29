'''Возведение числа в степень'''
def pow(a: float, n: int):
    if n == 0:
        return 1
    elif n % 2 == 1:    # нечёт
        return pow(a, n - 1) * a
    else:   # n - чётное
        return pow(a ** 2, n // 2)

a = int(input("Введите число: "))
n = int(input("Введите степень числа: "))

print(pow(a, n))
