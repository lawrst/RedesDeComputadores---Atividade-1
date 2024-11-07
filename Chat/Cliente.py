from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import sys

# Função para receber mensagens do servidor
def receber_mensagens(s):
    while True:
        try:
            mensagem = s.recv(1500).decode()
            
            # Limpa a linha de entrada atual do servidor
            sys.stdout.write('\r' + ' ' * 80 + '\r')  # Apaga a linha atual
            print(f'Servidor: {mensagem}')
            
            # Exibe o prompt de entrada de novo para o servidor
            sys.stdout.write("Você (Cliente): ")
            sys.stdout.flush()
        except:
            print('Conexão com o servidor foi encerrada.')
            s.close()
            break

# Função para enviar mensagens ao servidor
def enviar_mensagens(s):
    while True:
        mensagem = input("Você (Cliente): ")
        s.send(f'{mensagem}'.encode())

# Configura o socket do cliente
s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 8000))
print('Conectado ao servidor na porta 8000')

# Inicia as threads de envio e recepção de mensagens
Thread(target=receber_mensagens, args=(s,)).start()
Thread(target=enviar_mensagens, args=(s,)).start()
