def reverseList(lyst):
    tam = len(lyst) - 1
    limit = tam//2
    for i in range(tam):
        aux = lyst[i]
        lyst[i] = lyst[tam - i]
        lyst[tam - i] = aux
        if i == limit:
            break
    print(lyst)
    
lista = [10, 9, 8, 8, 7, 6, 5, 4, 3, 3, 3, 2, 1, 1, 0]
reverseList(lista)


# Complexidade Computacional
# - Melhor caso: O(n)
# - Médio caso: O(n)
# - Pior caso: O(n)
