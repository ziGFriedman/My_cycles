'''Число способов допрыгнуть в точку N, с запрещенными клетками (шаг +1 +2 +3)'''
def count_trajectories(N, allowed: list):
    K = [0, 1, int(allowed[2]) + [0] * (N-3)]
    for i in range(3, N+1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] + K[i-3]

'''Минимальная стоимость достижения клетки N (шаг +1 и +2)'''
# price[i] - цена за посещение клетки i
# C[i] - cost, min, миннимальная суммарная стоимость достижения клетками i
def count_min_cost(N, price: list):
    C = [None, price[1], price[1] + price[2]] + [0] * [N-2]
    for i in range(3, N+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
    return C[N]
    
