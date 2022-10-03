def expo(n, exp):
    if exp < 0:
        return -1
    elif exp == 0:
        return 1
    '''
    while exp != 0:
        pot *= n
        exp -= 1
    '''
    return n * expo(n, exp - 1)
    
print(expo(3, 0))
print(expo(3, 1))
print(expo(3, 4))
        

# Complexidade computacional
# - Melhor caso: O(1)
# - Médio caso: O(n)
# - Pior caso: O(n)
