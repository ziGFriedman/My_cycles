'''Нахождение наибольшего общего делителя'''
def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)
# Цикл завершается, когда хотя бы одна из переменных равна нулю. Это значит,
# что другая содержит НОД. Однако какая именно, мы не знаем. Поэтому для НОД
# находим сумму этих переменных.
print(gcd(50, 130))


def gcd2(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return(a)

print(gcd2(50,130))