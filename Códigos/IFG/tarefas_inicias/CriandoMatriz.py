def crie_matriz(linhas, colunas, valor):

    matriz = [] # lista vazia	    
    for i in range(linhas): # cria a linha i
        linha = [] # lista vazia
        for j in range(colunas):
            linha.append(valor)
        matriz.append(linha)
        
    return matriz

a = crie_matriz(3, 3, 0)
print(a)