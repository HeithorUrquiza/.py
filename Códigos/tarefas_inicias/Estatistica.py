import Stats

lista = [0, 0, 0, 0, 0, 0, 0]
for x in range(7):
    value = float(input("Informe os valores para a lista: "))
    lista[x] = value


Stats.med(lista)
Stats.mediana(lista)
Stats.moda(lista)

