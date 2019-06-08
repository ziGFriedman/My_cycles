'''Сортировка Тони Хоара QuicSort'''
def hoar_sort(A):
    if len(A) <= 1:
        return

    barrier = A[0]
    L = []      # L = M = R - нельзя писать, в питоне ссылочная модель присваивания
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)

    hoar_sort(L)
    hoar_sort(R)

    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1

'''Проверка отсортированности за O(len(A))'''
def check_sorted(A, ascending=True):
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0, N - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
            break
    return flag
