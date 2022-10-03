def swap(lyst, i, j):
    aux = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = aux
    
def swapReverse(lyst):
    tam = len(lyst) - 1
    limit = tam//2
    for i in range(tam):
        aux = lyst[i]
        lyst[i] = lyst[tam - i]
        lyst[tam - i] = aux
        if i == limit:
            break

def selectionSort(lyst, reverse = None):
    i = 0
    while i < len(lyst) - 1: # Faz n - 1 pesquisas
        minIndex = i # pelo menor
        j = i + 1
        while j < len(lyst): # Inicia uma pesquisa
            if lyst[j] < lyst[minIndex]:
                swap(lyst, minIndex, j)
            j += 1
        i += 1
    if reverse == 1:
        swapReverse(lyst)
    
    
lyst = [0, 45, 23, -3, 1, 4, 2, -1]
selectionSort(lyst)
print(lyst)
print("-"*25)
selectionSort(lyst, 1)
print(lyst)

# Complexidade Computacional
# - Melhor caso: O(n^2)
# - Médio caso: O(n^2)
# - Pior caso: O(n^2)
