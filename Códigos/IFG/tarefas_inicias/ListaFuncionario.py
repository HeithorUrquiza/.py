print("\t\n*** Relátorio de Pagamentos ***")
relat = str(input("\nInsira o nome do arquivo que deseja abrir e sua exntenção: "))
print(" ")
with open(relat, 'r') as arquivo:
    for value in arquivo:
        print(value)

'''arquivo = open("salario_funcionario.txt", "r")
print(arquivo.readlines())'''