"""
    - import this -> Zen do Python
    - Camel Case para nome de classes
    - letras minúsculas e underline para nomes de variáveis e funções
    
    _________________________________________________________________________________________________________________________________
    
    DIR -> Apresenta todos os atributos e funções/métodos disponíveis para determinado tipo de dado ou variável
    
    - dir(tipo de dados/variável)
    
    HELP -> Apresenta a documentação/como utilizar os atributos/propriedades e funções/métodos deisponíveis para determinado tipo de dado ou variável
    
    - help(tipo de dado/variável.propriedade)
    
    _________________________________________________________________________________________________________________________________
    
    RECEBENDO DADOS DO USUÁRIO
    
    nome = input(str("Qual o seu nome? "))  #Entrada de dados
    print(f"Seja Bem-vindo(a) {nome}") #Saída de dados
    
    - Exemplos de PRINT
    print('Seja bem-vindo %s' % nome)    
    print('Seja bem-vindo {0}'.fromat(nome))    
    print(f'Seja bem-vindo {nome}')
    
    * CAST -> conversão de um tipo de dado para outro    
    
    _________________________________________________________________________________________________________________________________
    
    TIPOS DE DADOS
    
    > type() => mostra qual é o tipo do dado
    
    - Numérico: 1, 100, 1_000_000
    - Float/Real/Decimal: 1.2, 3.99, 1_000.00 
    - Complex: basta adicionar j ao final (ex: 5j)
    - Booleano: True ou False | NOT: not + variável => inverte o valor lógico da variável
    - String: Todo dado envolvido por aspas simples('') ou duplas("") | Slice de String -- ex: print(nome[0:5]) | [::-1] -> Comece do primeiro elemtno, vá até o último e inverta
"""