'''Наибольшая общая подпоследовательность'''
def lcs(A, B):
    F = [[0] * (len(B)+1) for i in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[-1][-1]

# A, B - массивы чисел
# len(A) == N
# len(B) == M
# Fij - длина наибольшей возможной подпоследовательности частей A, B
# Ai = A[0: i] - часть A, первые i элементы
# Bj = B[0: j] - часть B, первые j элементы
#        {1 + F(i-1)(j-1), ai = bj
# Fij = {
#        {max(Fi(j-1), F(i-1)j), ai != bj
# Foj = 0, Fi0 = 0
