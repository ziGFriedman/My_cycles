'''Бинарный поиск в отсортированном массиве'''
def left_borrd(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    if key in A:
        return (left + 1)

print(left_borrd([6, 9, 13, 16, 22], 16))
