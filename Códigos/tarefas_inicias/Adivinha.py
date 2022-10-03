import random
import math


print("\n***BEM-VINDO AO JOGO DE ADVINHA ***")
user = int(input("\nDigite um número para o jogo: "))
print("\nPara a tentativa do computador informe:")
min = int(input("O valor minimo: "))
max = int(input("O valor máximo: "))

pc = random.randrange(min, max)
chance = math.ceil((math.log(2, 10) * (max - min))) + 1 #Arredonda as chances para um número inteiro
count = 0

while count != chance: #testa os valores até que seja atingido o número de tentativas
    print("Seu número é: ", pc)
    resp = str(input("Entre com =, < ou >: "))  
    if resp == "<":
        newTry = random.randrange(min, pc) #Refaz o limite que gera o número aleátorio
        pc = newTry
        count += 1
    elif resp == ">":
        newTry = random.randrange(pc, max)
        pc = newTry
        count += 1
    elif resp == "=":
        count += 1
        print(f"\nUau! Acertei com {count} tentativa(s)!")
        break
    
if count == chance: #Confere e exibe a resposta caso o limite de tentativas seja atingido
    if pc == user:
        print("Seu número é: ", pc)
        resp = str(input("Entre com =, < ou >: "))
        if resp == "=": 
            count += 1
            print(f"\nUau! Acertei com {count} tentativa(s)!")
    else:
        print("\nVocê excedeu o número de tentativas") 
    

"""print("Seu número é: ", pc)
resp = str(input("Entre com =, < ou >: "))  
if pc == user:
    count += 1
    print(f"Uau! Acertei com {count} tentativa(s)!")"""