from ClasseStudent import Student

aluno = Student("Arthur Medrado", [88, 77, 100])

print("=" * 40)
print("\n   Sistema de Gerenciamento de Cursos   \n")
print("=" * 40)

ordem = 4
while ordem != 0: #loop para painel interativo
    print("\n    *** Terminal ***")
    ordem = int(input("\n1 - Acessar ou Subsutituir pontuação"
                      "\n2 - Realizar consultas individuais"
                      "\n3 - Exibir informações do aluno"
                      "\n0 - Para sair do sistema"
                      "\n\nInforme o comando: "))
    if ordem == 1:
        aluno.consultaPontos()
    elif ordem == 2:
        aluno.obterDados()
    elif ordem == 3:
        aluno.imprimirAluno()
    elif ordem == 0:
        break
    else:
        print("Comando inválido")
    
    print("-" * 30)
