# UDPPingerClient.py
import time
from socket import *

# Configurações do servidor
serverName = 'localhost'
serverPort = 12000

# Cria um socket UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Define timeout para recebimento de pacote
clientSocket.settimeout(1)

# Número de pacotes a serem enviados
numPackets = 10

# Loop para enviar pacotes
for i in range(numPackets):
    # Define o tempo de envio do pacote
    sendTime = time.time()
    
    # Prepara mensagem para envio
    message = f'Ping {i+1}'.encode()
    
    try:
        # Envia mensagem para o servidor
        clientSocket.sendto(message, (serverName, serverPort))
        
        # Recebe resposta do servidor
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        
        # Calcula tempo de resposta em segundos
        receiveTime = time.time()
        rtt = receiveTime - sendTime
        
        # Exibe resposta e tempo de resposta
        print(f'Resposta do servidor: {modifiedMessage.decode()}')
        print(f'Tempo de resposta: {rtt:.6f} segundos\n')
        
    except timeout:
        # Exibe mensagem de pacote perdido
        print(f'Pacote {i+1} perdido\n')

# Encerra conexão
clientSocket.close()
