def expoRecursive(n, exp):
    #Caso base
    if exp == 0:
        pot = 1
        #Caso recursivo
    elif exp > 0:
        if exp % 2 != 0:
            pot = n * expoRecursive(n, exp - 1)
        elif exp % 2 == 0:
            pot = expoRecursive(n, exp/2) * expoRecursive(n, exp/2)
    return pot
    
print(expoRecursive(2, 0))
print(expoRecursive(2, 12))
print(expoRecursive(3, 4))
print(expoRecursive(3, 0))


# Complexidade computacional
# - Melhor caso: O(1)
# - Médio caso: O(n)
# - Pior caso: O(n)
