"""
    LISTAS
    
    --> Funcionam como arrays com a diferença de serem DINÂMICOS e podermos colocar QUALQUER tipo de dado, além de repeti-los
    --> Representação: []
    
    listaInt = [1, 22, 3, 0, 1, 4]
    listaString = ['a', 'b', 'c', 'd', 'e']
    listaVazia = []
    listaRange = list(range(1, 10))
    usandoList = list('alfabeto')

    -- Checando valores
    print(8 in listaRange)
    print('h' in listaString)


    -- Ordenando uma lista
    listaInt.sort()
    print(listaInt)

    usandoList.sort() #Ordenando strings
    print(usandoList)
    
    
    -- Contando número de ocorrências
    print(usandoList.count('a'))
    
    
    -- Adicionando elementos ao final da lista (Apenas 1 item por vez)
    print(listaInt)
    listaInt.append(22)
    listaInt.append([12, 2, 3]) #Podemos passar qualquer valor como parâmetro
    listaInt.extend([-1, -2, -3]) #Repassa os valores da lista 1 a 1
    print(listaInt)


    -- Adicionando em uma posição específica
    listaInt.insert(2, 13)
    print(listaInt)


    -- Juntando duas listas
    novaLista = listaInt + listaString
    print(novaLista)    
    
    
    -- Revertendo uma lista
    print(listaString[::-1])
    listaInt.reverse()
    print(listaInt)


    -- Obtendo o tamanho de uma lista
    print(len(listaInt))
    
    
    -- Removendo o último item da lista diretamente ou pelo índice
    listaInt.pop()
    print(listaInt)
    listaInt.pop(2)
    print(listaInt)
    
    
    -- Divindo uma String para um lista
    curso = 'Programação em Python'
    curso = curso.split()
    print(curso)


    -- Convertendo uma lista em String
    listaTeste = ['Programação', 'em', 'Python']
    curse = ' '.join(listaTeste)
    print(curse)
"""
#Pode apagar depois
listaInt = [1, 22, 3, 0, 1, 4]
listaString = ['a', 'b', 'c', 'd', 'e']
listaVazia = []
listaRange = list(range(1, 10))
usandoList = list('alfabeto')




