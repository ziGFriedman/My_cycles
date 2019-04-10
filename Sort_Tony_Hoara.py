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

def check_sorted(A, ascending = True):
'''Проверка отсортированности за O(len(A))'''
    flag = True
    
