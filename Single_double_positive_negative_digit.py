'''Какое число: однозначное или двухзначное, положительное или отрицательное?'''
def digit(n):
    if n == 0:
        print('Ноль - однозначное число')
    else:
        if n > 0:
            print('Положительное', end = ' ')
        else:
            print('Отрицательное', end = ' ')
        if abs(n) < 10:
            print("однозначное число")
        elif (10 <= abs(n) < 100):
            print('двузначное число')
        else:
            print('трехзначное или более число')

digit(378)
