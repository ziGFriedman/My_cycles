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
    return left
    
