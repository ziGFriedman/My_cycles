'''Наибольшая возрастающая подпоследовательность'''
#F[i] -  НВП для части A[0: i], которая заканчивается  исодержит элемент ai = A[i-1]
def gis(A):
    F = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        max = 0
        for j in range(0, i):
            if A[i] > A[j] and F[j] > max:
                max = F[j]
        F[i] = max + 1
    return F[len(A)]
