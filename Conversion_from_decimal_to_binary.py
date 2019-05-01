def to_binary(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b

print(to_binary(8))

'''Стандартная python функция перевода'''
print(bin(8))
