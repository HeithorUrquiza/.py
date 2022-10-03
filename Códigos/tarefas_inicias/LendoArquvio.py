import linecache
print("\t\n !! NAVEGANDO PELAS LINHAS !!")

arq = str(input("\nInforme o nome do arquivo que deseja abrir e sua extensão: "))

arquivo = open(arq, "r")
resp = 1
count = 0
content = arquivo.read()
contList = content.split("\n")

for i in contList: #loop para a contagem de linhas
    if i:
        count += 1
print(f"\nNúmero de linhas do arquivo: {count}")

while resp != 0: #loop para a leitura de linhas
    line = int(input("Informe a linha que deseja obter: "))
    lines = linecache.getline(arq, line) #recolhe o valor da linha especificada
    print(f"\n* Linha {line}: {lines}")
    resp = int(input("Deseja encerrar? [0 - Sim / 1 - Não]: "))
    print(" ")



