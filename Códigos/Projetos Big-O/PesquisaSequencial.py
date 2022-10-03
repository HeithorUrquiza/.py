def sequencialSearch(target, lyst):
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1

lyst = [2, 34, 7, -1, 0, 10]
a = sequencialSearch(7, lyst)
print(a)


# Complexidade computacional Big-O
# - Melhor caso: O(1) com o alvo na primeira posição
# - Pior caso: O(n) com o alvo ao final da lista ou ainda fora dela
# - Médio caso: O(n) com o alvo no meio da lista

