from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import sys

def receber_mensagens(cliente_socket, endereco_cliente):
    while True:
        try:

            mensagem = cliente_socket.recv(1500).decode()
            
            sys.stdout.write('\r' + ' ' * 80 + '\r')  # Apaga a linha atual
            print(f'Cliente ({endereco_cliente}): {mensagem}')
            
            # Exibe o prompt de entrada de novo para o servidor
            sys.stdout.write("Você (Servidor): ")
            sys.stdout.flush()

        except:

            sys.stdout.write('\r' + ' ' * 80 + '\r')  # Apaga a linha atual
            print(f'Conexão com o cliente {endereco_cliente} foi encerrada.')
            cliente_socket.close()
            break

def enviar_mensagens(cliente_socket):
    while True:
        mensagem = input("Você (Servidor): ")
        cliente_socket.send(mensagem.encode())

def conexao_cliente(cliente_socket, endereco_cliente):
    print(f'Conexão estabelecida com {endereco_cliente}')
    Thread(target=receber_mensagens, args=(cliente_socket, endereco_cliente)).start()
    Thread(target=enviar_mensagens, args=(cliente_socket,)).start()

# Configura o socket do servidor
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8000))
server_socket.listen()

print('Aguardando novas conexões na porta 8000')

# Aceita conexões de clientes
while True:
    cliente_socket, endereco_cliente = server_socket.accept()
    Thread(target=conexao_cliente, args=(cliente_socket, endereco_cliente)).start()
