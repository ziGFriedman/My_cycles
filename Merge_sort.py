'''Метод сортировки слиянием через алгоритмы'''
def merge(A:list, B:list):
    C = [0] * (len(A) + len(B))
    i = k = n = 0   # i элемент А, k = элемент B, n - элемент С
    while i < len(A) and k < len(B):    # Выбирем первым из А, чтобы сортировка была устойчивой (не меняет порядок равных элементов)
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k +=1
            n +=1

    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1

    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1

    return C

def merge_sort (A):
    if len(A) <= 1:
        return

    middle = len(A) // 2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]

    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]
