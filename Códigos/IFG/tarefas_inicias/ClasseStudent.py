
class Student:
    def __init__(self, name, list):
        self.name = name
        self.list = list
        
    def consultaPontos(self): #consulta e alteração de pontos
        cod = int(input("\n1 - Acessar pontuação" 
                        "\n2 - Alterar pontuação "
                        "\n\nInforme o comando: "))
        if cod == 1:
            x = int(input("Informe a posição ou número da pontuação: ")) #informa o valor do ponto solicitado
            print(f"\nPonto {x+1}: {self.list[x]}")
        elif cod == 2:
            x = int(input("Informe a posição ou número da pontuação: "))
            point = float(input("Digite o novo valor: "))
            print(f"\nAntigo valor {self.list[x]} \nNovo valor: {point}") #altera o valor e exibe uma comparação
            self.list[x] = point
        else:
            print("\nComando inválido!!")
    
    def obterDados(self):
        cod = int(input("\n1 - Número de pontuações "
                        "\n2 - Pontuação mais alta "
                        "\n3 - Pontuação média "
                        "\n4 - Nome do Aluno "
                        "\n\nInforme o comando: "))
        if cod == 1:
            print(f"\nHá um total de {len(self.list)} pontos") #mostra quantos pontos há
        elif cod == 2:
            print(f"\nO maior valor é {max(float(big) for big in self.list)}") #mostra o maior valor
        elif cod == 3:
            sum = 0
            for x in self.list:
                sum += x
            print(f"\nA pontuação média é {round(sum/len(self.list), 2)}") #exibe a média dos pontos
        elif cod == 4:
            print(f"\nNome: {self.name}") #impime o nome do aluno
        else:
            print("\nComando inválido!!")
            
    def imprimirAluno(self): #função para exibir todos os dados do aluno
        print(f"\nNome: {self.name}")
        n = 0
        for x in self.list:
            n += 1
            print(f"Ponto {n}: {x}")
        
        